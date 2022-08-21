# pip install deepface, cv2
import cv2 
from deepface import DeepFace
image_path = 'image.jpg'
image = cv2.imread(image_path)
analyze = DeepFace.analyze(image, actions = ['gender'])
result = f'gender : {analyze["gender"]}'
analyzed_image = cv2.putText(image, result,
(35,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.imshow('image',analyzed_image)
cv2.waitKey(0)