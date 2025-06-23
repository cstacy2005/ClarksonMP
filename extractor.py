# Importing all necessary libraries
import argparse
import cv2
import os
import sys


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized  
  

def create_folder(vid_name_without_ext,dest_path):
    
    try:
        # creating a folder named data
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
            
        if not os.path.exists(os.path.join(dest_path,vid_name_without_ext)):
            #os.makedirs('extracted/RiverTraining'+vid_name_without_ext)
            os.makedirs(os.path.join(dest_path,vid_name_without_ext))
    
        # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')



def extract_images_from_video(vid_path,dest_path,resize,noview,flip=False):
    vid_name = os.path.basename(vid_path)
    vid_name_without_ext = os.path.splitext(vid_name)[0]
    create_folder(vid_name_without_ext,dest_path)

    print("Extracting images from video: ",vid_path)
    # Read the video from specified path
    #vid_name = "2022-06-15-064219"
    cam = cv2.VideoCapture(vid_path)
    # frame
    currentframe = 0
    
    while(True):
        
        # reading from frame
        ret,frame = cam.read()
    
        if ret:
            # if video is still left continue creating images
            name = dest_path+vid_name_without_ext+"/"+vid_name_without_ext +"_"+str(currentframe) + '.png'
            print ('Creating...' + name)
            
            if resize is True:
                #frame = image_resize(frame,width=1920,height=1080)
                frame = image_resize(frame,width=640)
                #frame = cv2.resize(frame, (1280,736), interpolation = cv2.INTER_AREA)

            if flip is True:
                frame = cv2.flip(frame, 1)  # flip left-right

            # take 5fps video image
            #if currentframe % 12 == 0:
            # writing the extracted images
            #cv2.imwrite(name, frame,[cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite(name, frame,[cv2.IMWRITE_PNG_COMPRESSION, 0])
            #cv2.imwrite(name, frame)
    
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (50, 50)
            fontScale = 1
            # Blue color in BGR
            color = (255, 0, 0)
            thickness = 2
            
            if noview is False:
                frame = cv2.putText(frame, str(currentframe), org, font, fontScale, color, thickness, cv2.LINE_AA) 
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
        else:
            
            
            break
    
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source',  type=str, help='camera soruce')
    parser.add_argument('--dest',default="extracted/",  type=str, help='camera soruce')
    parser.add_argument('--resize', action="store_true", help='Resize or not')
    parser.add_argument('--flip', action="store_true", help='Flip horizontal or not')
    parser.add_argument('--noview', action="store_true", help='View or not')
    opt = parser.parse_args()
    vid_path = opt.source 
    resize = opt.resize
    noview = opt.noview
    flip = opt.flip
    dest_path = opt.dest

    
    print("Source: ",vid_path)
    if not os.path.exists(vid_path):
        print("Path do not exist: ",vid_path)
        exit()  
 
    if os.path.isfile(vid_path):
        extract_images_from_video(vid_path,dest_path,resize,noview,flip)
    elif os.path.isdir(vid_path):
        for file in os.listdir(vid_path):
            if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".MP4") or file.endswith(".mkv"):
                extract_images_from_video(vid_path+"/"+file,dest_path,resize,noview,flip)
# python extractor.py --source video.mp4 --resize 640 