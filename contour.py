import cv2
import numpy as np

def threshold(img):
    return cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

def dilate(img):
    thresh = threshold(img)
    kernel = np.ones((2, 2), np.uint8)
    return cv2.dilate(thresh, kernel, iterations=1)

def contour(img):
    dilation = dilate(img)
    cnts = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[1]
    rad_center_of_circle = []

    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour, then use the
        # bounding box to derive the aspect ratio
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)

        # in order to label the contour as a question, region
        # should be sufficiently wide, sufficiently tall, and
        # have an aspect ratio approximately equal to 1
        if w >= 5 and h >= 5 and ar >= 0.7 and ar <= 1.3:
            x_center = int(x + int(w / 2))
            y_center = int(y + int(w / 2))
            rad = int(w / 2)
            rad_center_of_circle.append([x_center,y_center,rad])
    return rad_center_of_circle
