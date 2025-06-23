import cv2

# Load the video
video_path = 'videos/RiverTraining/4mm_river_1mp_6.mp4'  # replace with your video file path
cap = cv2.VideoCapture(video_path)

# Check if video was opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the video.")
    exit()

# Set the desired FPS (10 FPS)
fps = 10
delay = int(1000 / fps)  # Delay in milliseconds per frame to achieve 10 FPS

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Display the current frame
    cv2.imshow('Video at 10 FPS', frame)

    # Wait for the key press or the desired delay time
    if cv2.waitKey(delay) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()
