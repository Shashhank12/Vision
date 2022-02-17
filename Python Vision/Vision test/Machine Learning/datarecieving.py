import cv2 as cv
from cv2 import VideoCapture
import numpy as np
import os
from time import time


#Captures video
wincap = VideoCapture(0)
#Sets loop-time to time
loop_time = time()
#For running each frame
while(True):
    isTrue, frame = wincap.read()
    
    cv.imshow('Unprocessed', frame)
    #Prints FPS
    print('FPS {}'. format(1/(time() - loop_time)))
    loop_time = time()
    #Sets key to waitkey
    key = cv.waitKey(1)
    #When q is pressed, window closes
    if key == ord('q'):
        cv.destroyAllWindows
        break
    #When f is pressed, it saves a screenshot to the positive folder
    elif key == ord('f'):
        cv.imwrite("Machine Learning\Positive\{}.jpg".format(loop_time), frame)
    #When d is pressed, it saves a screenshot to the negative folder
    elif key == ord('d'):
        cv.imwrite("Machine Learning\Negative\{}.jpg".format(loop_time), frame)

print('Done.')
