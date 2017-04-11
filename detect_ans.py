import numpy as np
import cv2


def detect_ans(img, contours):
    best_idx = 0
    best_count = 0
    counts = []
    for idx in range(len(contours)):
        # mask is a black image with a white circle on the current contour
        mask = np.zeros(img.shape, dtype='uint8')
        cv2.circle(mask, (contours[idx][0], contours[idx][1]), contours[idx][2], 255, -1)

        result = cv2.bitwise_and(img, mask)
        count = cv2.countNonZero(result)
        counts.append(count)

    total = sum(counts)
    max_count = max(counts)
    max_idx = counts.index(max_count)

    print('vvvv')
    print(1.0*max_count/(total+1), counts, max_idx)
    print('^^^^')

    if total>0 and 1.0*max_count/total > 0.6 and max_count>50:
        return max_idx
    else:
        # represents error
        return 4
