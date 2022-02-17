import cv2 as cv
from cv2 import VideoCapture
import numpy as np
import os
from time import time


#Captures video
wincap = VideoCapture('Machine Learning\WIN_20220215_17_21_51_Pro.mp4')
#Sets loop-time to time
loop_time = time()
#For running each frame
lower_green = np.array([220, 220, 220])
upper_green = np.array([255, 255, 255])
while(True):
    isTrue, frame = wincap.read()
    
    cv.imshow('Unprocessed', frame)
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    mask = cv.inRange(frame, lower_green, upper_green)
    #Prints FPS
    print('FPS {}'. format(1/(time() - loop_time)))
    loop_time = time()
    #Sets key to waitkey
    cv.imwrite("Machine Learning\Positive\{}.jpg".format(loop_time), mask)
    key = cv.waitKey(200)
    #When q is pressed, window closes
    if key == ord('q'):
        cv.destroyAllWindows
        break
    #When f is pressed, it saves a screenshot to the positive folder
    elif key == ord('f'):
        cv.imwrite("Machine Learning\Positive\{}.jpg".format(loop_time), frame)
    #When d is pressed, it saves a screenshot to the negative folder
    elif key == ord('d'):
        cv.imwrite("Machine Learning\\Negative\\{}.jpg".format(loop_time), frame)

print('Done.')
