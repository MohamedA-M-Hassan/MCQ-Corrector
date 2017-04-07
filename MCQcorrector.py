import numpy as np
import cv2
from rotate import rotate
from circhoughtrans import getAlignmentAngle
from crop import crop

img = cv2.imread('sample.png', 0)

rotation_angle = getAlignmentAngle(img)
rotated = rotate(img, rotation_angle)
cropped = crop(rotated)
result = cropped

window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
