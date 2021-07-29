import cv2 as cv
import numpy as np
from Defeinitions import *
#features:
    #1.total on pixels
    #2.cut in the midle x and count how many on lines
    #3.cut in the midle y and count how many on lines
def extract(roi):
    roi = cv.bitwise_not(roi)
    (roiH, roiW) = roi.shape
    total_on = cv.countNonZero(roi)/365
    #2
    middle_x_line = roi[0:roiW-1,roiH//2]
    total_middle_x = cv.countNonZero(middle_x_line)
    #3
    middle_y_line = roi[roiW//2,0:roiH-1]
    total_middle_y = cv.countNonZero(middle_y_line)

    features_values = np.zeros((10,FEATURES_NUMBER))
    features_values[0] = total_on/365
    features_values[1] = total_middle_x
    features_values[2] = total_middle_y
