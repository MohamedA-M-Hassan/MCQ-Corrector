import numpy as np
import cv2


def detect_ans(img, contours):
    best_idx = 0
    best_count = 0
    for idx in range(len(contours)):
        # mask is a black image with a white circle on the current contour
        mask = np.zeros(img.shape, dtype='uint8')
        cv2.circle(mask, (contours[idx][0], contours[idx][1]), contours[idx][2], 255, -1)

        result = cv2.bitwise_and(img, mask)
        count = cv2.countNonZero(result)
        if count > best_count:
            best_count = count
            best_idx = idx
    return best_idx
