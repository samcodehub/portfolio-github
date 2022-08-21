import numpy as np
import cv2

# creating a black image with 3 channels rgb and unsigned int datatype
img = np.zeros((400, 400, 3), dtype = "uint8")

# writing text 
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'sam codehub presents...', (50, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('dark', img)

# allowing us to see the img until we close it 
cv2.waitKey(0)
cv2.destroyAllWindows()