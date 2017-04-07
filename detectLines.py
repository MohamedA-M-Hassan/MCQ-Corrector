import cv2
import numpy as np


#** dilate
def dilation(img):
	img = cv2.medianBlur(img, 5)
	ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
	ret, thresh2 = cv2.threshold(img, 225, 255, cv2.THRESH_BINARY_INV)
	kernel = np.ones((5, 5), np.uint8)
	dilatedImg = cv2.dilate(thresh2, kernel, iterations=1)
	return dilatedImg

# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
	# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
	#           cv2.THRESH_BINARY,11,2)


#** this function return a list contains all lines detected in the img and sorted with the length
def detectLines(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray, 100, 250)
	lines = cv2.HoughLinesP(edges, 1, np.pi/180, 25, minLineLength=100, maxLineGap=50)



	length = []
	for line in lines:
	    x1, y1, x2, y2 = line[0]
	    length.append([np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2)),x1,y1,x2,y2])
	    #cv2.line(hough, (x1, y1), (x2, y2), (0, 255, 0), 2)
	    #length.append(np.sqrt(np.power((x1-x2),2)+np.power((y1-y2),2)))  

	length = sorted(length,key=lambda l:l[0], reverse=True)
	# how to draw lines given 2 points (x1,y1) , (x2,y2)
	"""
	hough = img
	for  j in range(0,150):
		cv2.line(hough, (length[j][1], length[j][2]), (length[j][3],length[j][4]), (0, 0, 255), 3)
	"""
	return length

#def selectImportantLines(list_have_length_2points):

