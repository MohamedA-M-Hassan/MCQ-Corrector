import numpy as np
import cv2
import math
from rotate import rotate

img = cv2.imread('sample.png',0)
screen_res =1280.,1280.
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)
cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst_rt', window_width, window_height)

img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=40,maxRadius=60)
#circles = np.uint16(np.around(circles))

#for i in circles[0,:]:
  # draw the outer circle
  #cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
  # draw the center of the circle
  #cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

delta_y=circles[0,1][1]-circles[0,0][1]
delta_x=circles[0,1][0]-circles[0,0][0]
print(delta_y,delta_x)
angle=math.atan2(delta_y,delta_x)
print(cimg.shape)
cimg=rotate(img,angle*180/math.pi)
cv2.imshow('dst_rt', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
