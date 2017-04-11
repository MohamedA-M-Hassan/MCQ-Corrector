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
            avg_l = (w+h)/2.
            x_center = int(x + int(avg_l / 2))
            y_center = int(y + int(avg_l / 2))
            rad = int(avg_l / 2)
            rad_center_of_circle.append([x_center,y_center,rad])
    return rad_center_of_circle


def specific_contours(img):
    detected_contours_list = contour(img)
    detected_contours_list = sorted(detected_contours_list, key=lambda l: l[1], reverse=True)
    actual_contours = []
    y_flag = 0
    isFirst = True
    for row in detected_contours_list:
        # after trials I find that the radius = 11 approximately
        x_first = row[0]
        y_first = row[1]
        rad = row[2]
        # if rad out of our range 10=< rad =< 12 then: don't care (faks y3ny)
        if rad >14 or rad < 10:
            continue

        if abs(y_first-y_flag)<10 and not isFirst:
            continue
        # print(y_flag , y_first)
        # print('Center Pos ',y_first,' Radius ',rad)
        rad = 11
        isFirst = False

        if x_first <= 180 and x_first >= 135:
            actual_contours.append([x_first, y_first, rad])
            actual_contours.append([x_first - 41, y_first, rad])
            actual_contours.append([x_first - (2*41), y_first, rad])
            actual_contours.append([x_first - (3*41), y_first, rad])
        elif x_first <= 135 and x_first >= 95:
            actual_contours.append([x_first + 41, y_first, rad])
            actual_contours.append([x_first, y_first, rad])
            actual_contours.append([x_first - (1*41), y_first, rad])
            actual_contours.append([x_first - (2*41), y_first, rad])
        elif x_first <= 90 and x_first >= 55:
            actual_contours.append([x_first + (2*41), y_first, rad])
            actual_contours.append([x_first + (1*41), y_first, rad])
            actual_contours.append([x_first, y_first, rad])
            actual_contours.append([x_first - 41, y_first, rad])
        elif x_first <= 45 and x_first >= 15:
            actual_contours.append([x_first + (3*41), y_first, rad])
            actual_contours.append([x_first + (2*41), y_first, rad])
            actual_contours.append([x_first + 41, y_first, rad])
            actual_contours.append([x_first, y_first, rad])
        else:
          print('Error')
        y_flag = y_first
    if len(actual_contours)<60:
      avg_y = [592, 552, 511, 471, 430, 389, 349, 309, 268, 227, 187, 145, 105, 64, 24]
      found_y = [False for i in range(15)]
      indx = 0
      i = 0
      limit = len(actual_contours)
      while indx<limit and i<15:
        if abs(actual_contours[indx][1]-avg_y[i])<30:
          found_y[i] = True
          indx += 4
          i += 1
          continue
        else:
          i += 1

      for i in range(15):
        if not found_y[i]:
          rad = 11
          actual_contours.append([actual_contours[0][0], avg_y[i], rad])
          actual_contours.append([actual_contours[1][0], avg_y[i], rad])
          actual_contours.append([actual_contours[2][0], avg_y[i], rad])
          actual_contours.append([actual_contours[3][0], avg_y[i], rad])
    return sorted(actual_contours, key=lambda l: (l[1],l[0]))
