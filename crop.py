import cv2
from circhoughtrans import getCircles


def crop(src):
    blurred = cv2.medianBlur(src, 5)
    circles = getCircles(blurred,40,60)
    x = circles[0,0][1]
    y = circles[0,0][0]
    cropped = src[x-800:x-145, y-35:y+825]
    return cropped
