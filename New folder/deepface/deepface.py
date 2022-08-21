# pip install deepface

import cv2
from cv2 import FONT_HERSHEY_SIMPLEX
from deepface import DeepFace
import numpy as np
image_path = 'img.jpg'
image = cv2.imread(image_path)
analyze = DeepFace.analyze(image, actions=['emotion'])
analyzed_image = cv2.putText(image, analyze['dominant_emotion'],
(380,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
cv2.imshow('Recognize emotions', analyzed_image)
cv2.waitKey(0)