# pip install keras numpy pillow scipy h5py matplotlib opencv-python imageai

# import neccesary libraries
from imageai.Detection import ObjectDetection
import os


# using os library to get executing file path 
execution_path = os.getcwd()

# especify model and data   
detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
# download yolo_tiny.h5 from 
# https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5/
detector.setModelPath(os.path.join(execution_path, "yolo_tiny.h5"))
detector.loadModel()

# now give the image name and location to execute to the model  
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "cars.jpg"),
output_image=os.path.join(execution_path, "newdetect.jpg"))


# now filter executable data as we want
cars = [detection for detection in detections if detection['name']=='car']
number_of_cars = len(cars)


print("there are ",number_of_cars," cars in the picture.")