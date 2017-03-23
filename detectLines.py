import cv2
import numpy as np

def detectLines(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray, 100, 250)
	lines = cv2.HoughLinesP(edges, 1, np.pi/180, 25, minLineLength=100, maxLineGap=50)

	hough = img

	length = []
	i=0
	for line in lines:
	    x1, y1, x2, y2 = line[0]
	    length.append([np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2)),x1,y1,x2,y2])
	    i=i+1
	    #cv2.line(hough, (x1, y1), (x2, y2), (0, 255, 0), 2)
	    #length.append(np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2)))  

	length = sorted(length,key=lambda l:l[0], reverse=True)
	for  j in range(0,8):
		cv2.line(hough, (length[j][1], length[j][2]), (length[j][3],length[j][4]), (0, 255, 0), 2)
	return hough