import numpy as np
import cv2
from rotate import rotate
from circhoughtrans import getAlignmentAngle

window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
img = cv2.imread('sample.png', 0)
rotation_angle = getAlignmentAngle(img)
print(rotation_angle)
dst = rotate(img, rotation_angle)
cv2.imshow('result', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
