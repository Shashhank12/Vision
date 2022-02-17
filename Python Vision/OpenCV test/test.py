import cv2 as cv
from cv2 import BORDER_DEFAULT
import numpy as np

img = cv.imread('Photos\950(2.1).jpg')
cv.imshow('Original non cropped', img)

cropped = img[00:400, 0:1900]
cv.imshow('Original', cropped)

lower_bound = np.array([230, 230, 230])   
upper_bound = np.array([255, 255, 255])

mask = cv.inRange(cropped, lower_bound, upper_bound)
cv.imshow('Test', mask)

kernel = np.ones((7,7),np.uint8)

mask = cv.morphologyEx(kernel, cv.MORPH_CLOSE, kernel)
mask = cv.morphologyEx(kernel, cv.MORPH_OPEN, kernel)
cv.imshow('Test 2', mask)



cv.waitKey(0)