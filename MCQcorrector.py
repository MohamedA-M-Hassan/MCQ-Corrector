import cv2
from rotate import rotate

img = cv2.imread('sample.png', 0)

rotated = rotate(img, 2)
cropped = rotated[748:1406, 176:1034]
result = cropped
#result = rotated
cv2.imwrite('result.png', result)

window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
