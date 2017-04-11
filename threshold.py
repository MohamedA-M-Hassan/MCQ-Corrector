import cv2


def threshold(img):
    thresh = img
    cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU, thresh)
    return thresh
