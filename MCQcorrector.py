from calendar import different_locale
import cv2
import numpy as np
from rotate import rotate
from detectLines import detectLines
from detectLines import dilation
import os
from circhoughtrans import getAlignmentAngle
from crop import crop

img = cv2.imread('S_2_hppscan111.png')
test = dilation(img)
test2 = detectLines(test)
cv2.namedWindow('lines.jpg', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('lines.jpg', test)


#cv2.imwrite('thershold.jpg',thresh2)
#cv2.imwrite('thershold_dilation.jpg',dilation)

window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
directory = 'dataset/test/'

for fn in os.listdir(directory):
    name = directory + fn
    img = cv2.imread(name, 0)
    rotation_angle = getAlignmentAngle(img)
    rotated = rotate(img, rotation_angle)
    # cropped = crop(rotated)
    result = rotated
    cv2.imshow('result', result)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break

cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()

