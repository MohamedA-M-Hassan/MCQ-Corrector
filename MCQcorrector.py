import numpy as np
import cv2

img = cv2.imread('S_1_hppscan1.png')

# rotation
rows,cols,ch = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),35,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.namedWindow('image', cv2.WINDOW_NORMAL) #show normal window
cv2.namedWindow('image2', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('image',img)
cv2.imshow('image2',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()