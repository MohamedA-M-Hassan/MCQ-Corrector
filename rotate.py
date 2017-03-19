import numpy as np
import cv2

def rotate(src, angle):
    rows,cols = src.shape
    rotationMatrix = cv2.getRotationMatrix2D((cols/2,rows/2), angle, 1)
    white = (255, 255, 255)
    return cv2.warpAffine(src, rotationMatrix, (cols,rows), borderValue=white)

