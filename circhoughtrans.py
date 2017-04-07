import cv2
import math
def getCircles(img,minR,maxR):
    '''Returns a list of circles (radius/center) '''
    #circles = np.uint16(np.around(circles))
    ''' Add generated circles to an RGB image (cimg)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)	
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    '''
    return  cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=minR,maxRadius=maxR)

def getAlignmentAngle(img):
    img = cv2.medianBlur(img,5)
    circles=getCircles(img,40,60)
    delta_y=circles[0,1][1]-circles[0,0][1]
    delta_x=circles[0,1][0]-circles[0,0][0]
    angle=math.atan2(delta_y,delta_x)
    return (angle*180)/math.pi
