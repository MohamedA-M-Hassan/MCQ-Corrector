import cv2
import numpy as np
from rotate import rotate
from detectLines import detectLines

img = cv2.imread('S_2_hppscan111.png')

cv2.namedWindow('image', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('image',img)


test = detectLines(img)

#cv2.imwrite('hough.jpg', test)

cv2.namedWindow('hough.jpg', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('hough.jpg', test)

cv2.waitKey(0)
cv2.destroyAllWindows()