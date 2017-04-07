import numpy as np
import cv2
from rotate import rotate
from circhoughtrans import getAlignmentAngle

img = cv2.imread('sample.png', 0)

rotation_angle = getAlignmentAngle(img)
rotated = rotate(img, rotation_angle)
cropped = rotated[748:1406, 176:1034]
result = cropped
cv2.imwrite('result.png', result)

window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
