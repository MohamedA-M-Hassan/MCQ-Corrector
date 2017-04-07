import cv2
from circhoughtrans import getCircles


def crop(src):
    blurred = cv2.medianBlur(src, 5)
    circles = getCircles(blurred, 40, 60)
    left_circle = circles[0, 0]
    if left_circle[0] > circles[0, 1, 0]:
        left_circle = circles[0, 1]
    x = int(left_circle[1])
    y = int(left_circle[0])
    cropped = src[x-800:x-145, y-35:y+825]
    return cropped
