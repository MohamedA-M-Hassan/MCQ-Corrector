from calendar import different_locale
import cv2
import numpy as np
from rotate import rotate
from detectLines import detect_lines
from detectLines import dilation
import os
from circhoughtrans import getAlignmentAngle
from crop import crop

img = cv2.imread('croppingResult.jpg')

# cv2.namedWindow('lines.jpg', cv2.WINDOW_NORMAL) #show normal window
# cv2.imshow('lines.jpg', test2)

window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
directory = 'dataset/test/'

for fn in os.listdir(directory):
    name = directory + fn
    print(fn)
    img = cv2.imread(name, 0)
    rotation_angle = getAlignmentAngle(img)
    rotated = rotate(img, rotation_angle)
    cropped = crop(rotated)
    #ret, thresh = cv2.threshold(cropped, 235, 255, cv2.THRESH_BINARYq)
    result = detect_lines(cropped)
    # cv2.imwrite('croppingResult.jpg', result)
    cv2.imshow('result', result)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()

