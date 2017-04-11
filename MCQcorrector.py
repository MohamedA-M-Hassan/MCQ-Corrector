import cv2
import os
from rotate import rotate
from circhoughtrans import getAlignmentAngle
from crop import crop
import csv
import numpy as np
from crop import vertical_crop
from contour import specific_contours,contour
from detect_ans import detect_ans
from threshold import threshold
import re

model_ans =['b','c','a','a','d','a','c','c'
           ,'a','c','a','b','c','c','b','a'
           ,'d','b','c','b','d','c','d','b'
           ,'d','c','d','d','b','c','b','b'
           ,'d','c','b','c','b','c','c','a'
           ,'b','b','c','c','b']

# List of lists that will be written to .csv file
csv_data = [['FileName','Mark']]
# window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
directory = 'dataset/test/'

def sort_humanly( l ):
  """ Sort the given list in the way that humans expect.
  """
  convert = lambda text: int(text) if text.isdigit() else text
  alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
  l.sort( key=alphanum_key )
  return l
files = sort_humanly(os.listdir(directory))

for file_name in files:
    name = directory + file_name
    img = cv2.imread(name, 0)
    rotation_angle = getAlignmentAngle(img)
    rotated = rotate(img, rotation_angle)
    cropped = crop(rotated)
    vertical_crops = vertical_crop(cropped)

    choice = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
    ans = []

    for column in vertical_crops:
        contours = specific_contours(column)
        thresh = threshold(column)
        kernel = np.ones((3,3), np.uint8)
        eroded = cv2.erode(thresh, kernel, iterations = 1)

        for i in range(15):
            line_contours = contours[i*4:(i+1)*4]
            idx = detect_ans(eroded, line_contours)
            ans.append(choice[idx])
            if idx < 4:
                cv2.circle(column, (contours[i*4+idx][0], contours[i*4+idx][1]), contours[i*4+idx][2], 200, 5)

    # print(ans)
    '''
    cv2.imshow('result1', vertical_crops[0])
    cv2.imshow('result2', vertical_crops[1])
    cv2.imshow('result3', vertical_crops[2])
    # result = cropped
    # cv2.imshow('result', result)
    """
    for c in spe_contours:
        print("spe: ", c[1])
    """

    key = cv2.waitKey(0)
    if key == ord('q'):
        break
    # ans represents the choices of each student
    # ans = model_ans
    # Compare the student's choices to the model answer
    '''
    grade = sum([model_ans[index]==ans[index]
                for index in range(len(ans))])
    print(file_name,' ',grade)
    # Add new row to csv file data
    csv_data.append([file_name, grade])

# Write data to grades.csv
with open('grades.csv', 'wb') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

cv2.destroyAllWindows()
