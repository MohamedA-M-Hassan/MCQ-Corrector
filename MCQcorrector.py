import cv2
import os
from rotate import rotate
from circhoughtrans import getAlignmentAngle
from crop import crop
from crop import vertical_crop

window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
directory = 'dataset/test/'

for fn in os.listdir(directory):
    name = directory + fn
    img = cv2.imread(name, 0)
    rotation_angle = getAlignmentAngle(img)
    rotated = rotate(img, rotation_angle)
    cropped = crop(rotated)
    first, second, third = vertical_crop(cropped)
    result = first
    cv2.imshow('result3', result)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
    result = second
    cv2.imshow('result1', result)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
    result = third
    cv2.imshow('result2', result)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
