import numpy as np
import cv2

img = cv2.imread('S_1_hppscan1.png')

# rotation
rows,cols,ch = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),35,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.namedWindow('image', cv2.WINDOW_NORMAL) #show normal window
cv2.namedWindow('rotate', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('image',img)
cv2.imshow('rotate',dst)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 400, 400)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 25, minLineLength=100, maxLineGap=50)

#hough = np.zeros(img.shape, np.uint8)
hough = img
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(hough, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite('hough.jpg', hough)



cv2.namedWindow('hough.jpg', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('hough.jpg', hough)
cv2.waitKey(0)
cv2.destroyAllWindows()
