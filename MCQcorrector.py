import cv2
from rotate import rotate

window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
img = cv2.imread('sample.png', 0)
dst = rotate(img, 3)
cv2.imshow('result', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
