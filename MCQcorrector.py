import cv2
import numpy as np
from rotate import rotate
from detectLines import detectLines

img = cv2.imread('S_2_hppscan111.png')
cv2.namedWindow('original11', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('original11', img)


img = cv2.medianBlur(img,5)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,225,255,cv2.THRESH_BINARY_INV)
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
 #           cv2.THRESH_BINARY,11,2)


kernel = np.ones((20,20),np.uint8)
dilation = cv2.dilate(thresh2,kernel,iterations = 2)

#test = detectLines(img)
cv2.namedWindow('thershold_dilation.jpg', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('thershold_dilation.jpg', dilation)
cv2.namedWindow('original', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('original', thresh2)
cv2.imwrite('thershold.jpg',thresh2)
cv2.imwrite('thershold_dilation.jpg',dilation)


cv2.waitKey(0)
cv2.destroyAllWindows()