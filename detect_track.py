from collections import defaultdict

import cv2

from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

import csv

import math
import statistics

video_path = "videos/RiverTraining/3mm_river_1mp_sw3.mp4"
csv_path = "videos/RiverTraining/3mm_river_1mp_sw3.csv"

# Initialize CSV file
header = ['frame', 'fps', 'x_center', 'y_center', 'distance_1f', 'velocity_1f', 'MP_count','distance_5f',
          'velocity_5f', 'velocity_avg', "velocity_avg_cm", "size", "size_5f", "size_avg"]
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

data = []

# Dictionary to store tracking history with default empty lists
track_history = defaultdict(lambda: [])

# Load the YOLO model with segmentation capabilities
model = YOLO("runs/detect/train30/weights/best.pt")

# Open the video file
cap = cv2.VideoCapture(video_path)

# Retrieve video properties: width, height, and frames per second
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Horizontal line at 1/4 of the frame height
line = [0, int(h / 4), w, int(h / 4)]  

total_MP = 0
prev_frame = None
frame_count = 0
size = None
size_5f = None
distance_5f = None
velocity_5f = None

# Conversion factor from pixels to centimeters
FRAME_CM = 31.9  

while True:
    # Read a frame from the video
    ret, im0 = cap.read()
    if not ret:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    # Inference
    imageresults = model(im0)

    # Annotator object
    annotator = Annotator(im0, line_width=2)

    # Process detections
    for result in imageresults:
        boxes = result.boxes

        for box in boxes:
            conf = float(box.conf)
            if conf < 0.5:
                continue
            cls_id = int(box.cls)
            label = model.names[cls_id]
            xyxy = box.xyxy[0].tolist()  # [x1, y1, x2, y2]
            
            x1, y1, x2, y2 = map(int, xyxy)            
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            
            print("PRINT CENTER",center_x, center_y, label, conf)
            
            # Annotate image with bounding box and label
            annotator.box_label(xyxy, f'{label} {conf:.2f}', color=(255, 0, 0))
            
            # Update MP count when new MP crosses the line
            if prev_frame is None or (frame_count - prev_frame >= 90):
                if center_y > line[1]:
                    total_MP += 1
                    prev_frame = frame_count
            
            current_data = [frame_count, fps, center_x, center_y, "", "", "", "", "", "", "", size, size_5f]
            
            # Calculate size (mm) for the current frame
            size = ((y2 - y1) / h) * FRAME_CM * 10
            current_data = [frame_count, fps, center_x, center_y, "", "", "", "", "", "", "", size, size_5f]
            
            # Calculate avg size (mm) for the last 5 frames
            if len(data) >= 5 and (frame_count - data[-4][0] <= 10):
                sizes = []
                for row in data[-5:]:
                    sizes.append(row[11])
                size_5f = statistics.mean(sizes)
                current_data = [frame_count, fps, center_x, center_y, distance_1f, velocity_1f, total_MP, distance_5f, velocity_5f, "", "", size, size_5f]
            
            # Calculate distance and velocity for the last frame
            if len(data) > 0 and (frame_count - data[-1][0] <= 10):
                distance_1f = math.sqrt((center_x - data[-1][2]) ** 2 + (center_y - data[-1][3]) ** 2)
                velocity_1f = distance_1f * fps  
                current_data = [frame_count, fps, center_x, center_y, distance_1f, velocity_1f, total_MP, "", "", "", "", size, size_5f]
            
            # Calculate average velocity and distance for the last 5 frames
            if len(data) >= 6 and (frame_count - data[-4][0] <= 10):
                velocities = []
                for row in data[-5:]:
                    velocities.append(row[5])
                velocity_5f = statistics.mean(velocities)
                current_data = [frame_count, fps, center_x, center_y, distance_1f, velocity_1f, total_MP, distance_5f, velocity_5f, "", "", size, size_5f] 
        
            data.append(current_data)
            
    # Show the result
    annotated_frame = annotator.result()
    cv2.imshow("Detection", annotated_frame)

    # Break loop with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    frame_count += 1

# Calculate average velocity
all_velocities = []
for row in data[1:]:
    all_velocities.append(row[5])
velocity_avg = statistics.mean(all_velocities)
velocity_avg_cm = velocity_avg * (FRAME_CM/h)  # Convert to cm/s 

# Calculate average size
all_sizes = []
for row in data[1:]:
    all_sizes.append(row[11])
size_avg = statistics.mean(all_sizes)

data.append(["","","", "", "", "", "", "", "", velocity_avg, velocity_avg_cm, "", "", size_avg])

# Write data to CSV file   
with open(csv_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)    

# Clean up
cap.release()
cv2.destroyAllWindows()
