# Python program to save a 
# video using OpenCV

 
import cv2
import time

 
# Create an object to read 
# from camera
video = cv2.VideoCapture(0)

x = time.strftime("%Y_%m_%d_%H%M%S", time.localtime())

# We need to check if camera
# is opened previously or not
if (video.isOpened() == False): 
    print("Error reading video file")

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))
 
size = (frame_width, frame_height)
 
# Below VideoWriter object will create
# a frame of above defined The output 
# is stored in 'filename.avi' file.

started = False
result = cv2.VideoWriter(f"./videos/{x}.mp4", cv2.VideoWriter_fourcc(*'MP4V'), 10, [frame_height,frame_width])

while(True):
    ret, frame = video.read()
    
    for i in range(0, 3):
        ret, frame = video.read()

    rotatedFrame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE) 

    if ret == True: 

        # Write the frame into the
        # file 'filename.avi'
        if started:
            result.write(rotatedFrame)

        # Display the frame
        # saved in the file
        cv2.imshow('Frame', rotatedFrame)

        # Press S on keyboard 
        # to stop the process
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        if cv2.waitKey(1) & 0xFF == ord('w'):
            started= True
            print("recording")

    # Break the loop
    else:
        break

# When everything done, release 
# the video capture and video 
# write objects
video.release()
result.release()
  
# Closes all the frames
cv2.destroyAllWindows()
 
print("The video was successfully saved")