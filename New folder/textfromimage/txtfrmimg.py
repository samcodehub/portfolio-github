# Import libraries

import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Sam\AppData\Local\Tesseract-OCR\tesseract'

from PIL import Image


import cv2

img_cv = cv2.imread(r'im.png')

# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))
# OR
img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
print(pytesseract.image_to_string(img_rgb))


