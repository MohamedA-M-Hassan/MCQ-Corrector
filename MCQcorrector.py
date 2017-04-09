import cv2
import os
from rotate import rotate
from circhoughtrans import getAlignmentAngle
from crop import crop
import csv
from crop import vertical_crop
from contour import contour


model_ans =['b','c','a','a','d','a','c','c'
           ,'a','c','a','b','c','c','b','a'
           ,'d','b','c','b','d','c','d','b'
           ,'d','c','d','d','b','c','b','b'
           ,'d','c','b','c','b','c','c','a'
           ,'b','b','c','c','b']

# List of lists that will be written to .csv file
csv_data = [['FileName','Mark']]
window = cv2.namedWindow('result',  flags=cv2.WINDOW_NORMAL)
directory = 'dataset/test/'

for file_name in os.listdir(directory):
    name = directory + file_name
    img = cv2.imread(name, 0)
    rotation_angle = getAlignmentAngle(img)
    rotated = rotate(img, rotation_angle)
    cropped = crop(rotated)
    first, second, third = vertical_crop(cropped)

    contours = contour(first)
    for element in contours:
        cv2.circle(first, (element[0], element[1]), element[2], (192,192,192), -1)

    cv2.imshow('result1', first)
    cv2.imshow('result2', second)
    cv2.imshow('result3', third)
    result = cropped
    cv2.imshow('result', result)
    key = cv2.waitKey(0)
    if key == ord('q'):
        break

    # ans represents the choices of each student
    ans = model_ans
    # Compare the student's choices to the model answer
    grade = sum([model_ans[indx]==ans[indx]
                for indx in range(len(ans))])
    # Add new row to csv file data
    csv_data.append([file_name, grade])

# Write data to grades.csv
with open('grades.csv', 'wb') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

cv2.destroyAllWindows()
