import cv2 as cv
from cv2 import Canny
from cv2 import erode
import Constants
import numpy as np


def executePhoto():  
    original = cv.imread(Constants.MPRPhoto)
    img = original[0:1080, 0:1920]
    blank = np.zeros(img.shape, dtype = 'uint8')
    # dst = cv.fastNlMeansDenoisingColored(img ,None, 20, 20, 11,29)
    lower_green = np.array([230, 230, 230])
    upper_green = np.array([255, 255, 255])

    mask = cv.inRange(img , lower_green, upper_green)  
    res = cv.bitwise_and( img, img, mask= mask)  

    cv.imshow('mask', res)

    blockSize = 2
    apertureSize = 3
    k = 0.04

    # Detecting corners
    # dst = cv.cornerHarris(img, blockSize, apertureSize, k)

    cv.imshow("original", original)
    cv.waitKey(0)

def executeCamera():
    capture = cv.VideoCapture(Constants.port)

    lower_green = np.array([200,200,200])
    upper_green = np.array([255,255,255])

    while True:
        isTrue, frame = capture.read()
        mask = cv.inRange(frame , lower_green, upper_green)
        cv.imshow('Video', mask)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()
    cv.waitKey(0)