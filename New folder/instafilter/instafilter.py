# pip install instafilter

from instafilter import Instafilter

model = Instafilter("Lo-fi")
new_image = model("myimage.jpg")

# to save the image use cv2 
import cv2  
cv2.imwrite("modified_image.jpg", new_image)