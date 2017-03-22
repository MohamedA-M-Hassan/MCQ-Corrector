import cv2


def rotate(src, angle):
    # Angle is in degrees
    rows, cols = src.shape
    rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    white = (255, 255, 255)
    return cv2.warpAffine(src, rotation_matrix, (cols, rows), borderValue=white)

