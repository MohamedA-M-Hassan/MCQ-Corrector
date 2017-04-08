import cv2
import os
from rotate import rotate
import numpy as np
from circhoughtrans import getAlignmentAngle
from crop import crop
from crop import vertical_crop
from contour import contour


window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
directory = 'dataset/test/'

for fn in os.listdir(directory):
    name = directory + fn
    img = cv2.imread(name, 0)
    rotation_angle = getAlignmentAngle(img)
    rotated = rotate(img, rotation_angle)
    cropped = crop(rotated)
    first, second, third = vertical_crop(cropped)
    the_list = contour(first)
    for element in the_list:
        cv2.circle(first, (element[0], element[1]), element[2], (192,192,192), -1)


    """
    thresh = cv2.threshold(first, 230, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    kernel = np.ones((2, 2), np.uint8)
    dilation = cv2.dilate(thresh, kernel, iterations=1)
    cv2.imshow('canny', edges)
    cv2.imshow('dilation', dilation)

    cnts = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[1]
    questionCnts = []

    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour, then use the
        # bounding box to derive the aspect ratio
        (x, y, w, h) = cv2.boundingRect(c)
        print(x, " ", y, " ", w, " ", h)
        ar = w / float(h)

        # in order to label the contour as a question, region
        # should be sufficiently wide, sufficiently tall, and
        # have an aspect ratio approximately equal to 1
        if w >= 5  and h >= 5 and ar >= 0.7 and ar <= 1.3:
            questionCnts.append(c)
            cv2.circle(thresh, (x+int(w/2), y+int(w/2)), int(w/2), (192, 192, 192), -1)

    print("length :",len(questionCnts))
    """
    cv2.imshow('result1', first)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
    result = second
    cv2.imshow('result2', result)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
    result = third
    cv2.imshow('result3', result)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
