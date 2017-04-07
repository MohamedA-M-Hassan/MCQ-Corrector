from calendar import different_locale

import cv2
import numpy as np
from rotate import rotate
from detectLines import detectLines
from detectLines import dilation

img = cv2.imread('S_2_hppscan111.png')

test = dilation(img)
test2 = detectLines(test)
cv2.namedWindow('lines.jpg', cv2.WINDOW_NORMAL) #show normal window
cv2.imshow('lines.jpg', test)

#cv2.imwrite('thershold.jpg',thresh2)
#cv2.imwrite('thershold_dilation.jpg',dilation)


cv2.waitKey(0)
cv2.destroyAllWindows()