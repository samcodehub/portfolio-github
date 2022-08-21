# pip install opencv-python 
import cv2
import numpy as np

# load the image or video files
video = cv2.VideoCapture("green.mp4")

# background
image = cv2.imread("bg.jpeg")

while True:
    ret, frame = video.read()  # read the file 
    
    frame = cv2.resize(frame, (640, 480))   # resize the image and video to the same size
    image = cv2.resize(image, (640, 480))
    
    u_green = np.array([104, 153, 70])   # load the upper and lower RGB values of the green color
    l_green = np.array([30, 30, 0])
    
    mask = cv2.inRange(frame, l_green, u_green)     # apply the mask and then use bitwise_and
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    f = frame - res     # substract bitwise_and from the original green screen image
    
    f = np.where(f==0, image, f)  # check for matrix value 0 after substracting and replace it by the second img
    
    cv2.imshow("video", frame)   # display the video
    cv2.imshow("mask", f)
    if cv2.waitKey(25)==27:
        break
video.release()
cv2.destroyAllWindows()