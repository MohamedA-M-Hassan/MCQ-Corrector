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
edges = cv2.Canny(gray, 100, 250)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 25, minLineLength=100, maxLineGap=50)

#hough = np.zeros(img.shape, np.uint8)

hough = img

rows = 3000
columns= 5
length = [[0 for x in range(columns)] for x in range(rows)]

i=0
for line in lines:
    x1, y1, x2, y2 = line[0]
    length[i][0]=np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2))
    length[i][1]=x1
    length[i][2]=y1
    length[i][3]=x2
    length[i][4]=y2
    i=i+1
    #cv2.line(hough, (x1, y1), (x2, y2), (0, 255, 0), 2)
    #length.append(np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2)))  

length = sorted(length,key=lambda l:l[0], reverse=True)
for  j in range(0,8):
	cv2.line(hough, (length[j][1], length[j][2]), (length[j][3],length[j][4]), (0, 255, 0), 2)
cv2.imwrite('hough.jpg', hough)

cv2.namedWindow('hough.jpg', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('hough.jpg', hough)
cv2.waitKey(0)
cv2.destroyAllWindows()
