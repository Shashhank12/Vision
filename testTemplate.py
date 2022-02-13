import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import Constants

original = cv.imread(Constants.MPRPhoto)
img = original[0:1080, 0:1920]
blank = np.zeros(img.shape, dtype = 'uint8')
# dst = cv.fastNlMeansDenoisingColored(img ,None, 20, 20, 11,29)
lower_green = np.array([230, 230, 230])
upper_green = np.array([255, 255, 255])

mask = cv.inRange(img , lower_green, upper_green)  

#img_rgb = mask
img_gray = cv.cvtColor(mask, cv.COLOR_)
template = cv.imread('Photos/template.png', 0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.1
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(mask, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
#cv.imwrite('res.png',img_rgb)
cv.imshow('lol', mask)
cv.waitKey(0)