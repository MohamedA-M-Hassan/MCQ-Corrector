import cv2
import numpy as np


#** dilate
def dilation(img):
    # img = cv2.medianBlur(img, 5) #wrong don't use it
    ret, thresh = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((3,3), np.uint8)
    dilatedImg = cv2.dilate(thresh, kernel, iterations=3)
    return dilatedImg

# ** this function return a list contains all lines detected in the img and sorted with the length
def detect_lines(img):
    edges = cv2.Canny(img, 100, 250)
    lines = cv2.HoughLinesP(edges, 10, np.pi/180, 100, minLineLength=100, maxLineGap=5)

    length = []
	# check not empty
    for line in lines:
        x1, y1, x2, y2 = line[0]
        length.append([np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2)),x1,y1,x2,y2])
    length = sorted(length,key=lambda l:l[0], reverse=True)
    # how to draw lines given 2 points (x1,y1) , (x2,y2)
    hough = img
    for j in range(0,2):
        cv2.line(hough, (length[j][1], length[j][2]), (length[j][3],length[j][4]), (192, 192, 192), 3)
        cv2.putText(img=hough,text= "hi", org= ( length[j][1], length[j][2]), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=.3, color=0)
    return hough


