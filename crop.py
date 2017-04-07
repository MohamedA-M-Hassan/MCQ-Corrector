import cv2
from circhoughtrans import getCenterOfBottomLeftCircle


def crop(src):
    x,y = getCenterOfBottomLeftCircle(src)
    cropped = src[x-800:x-145, y-35:y+825]
    return cropped
