import cv2 as cv
import numpy as np
from Defeinitions import *
import math
#features:
    #1.total on pixels
    #2.cut in the midle x and count how many on lines
    #3.cut in the midle y and count how many on lines
    #4. lower part of image, on pixels relative to area
    #5. left part of image, on pixels relative to area
    #6. upper
    #7. right
    #8 lines cutting
def lines_counting(roi,horizontal,cutting_point):
    last=0
    counter=0
    if horizontal==1:
        strip = roi[:,cutting_point]
    else:
        strip = roi[cutting_point,:]
    if (strip[0] == 0):
        counter = 1
    for pixel in strip:
        if (pixel == 0 and last == 1):
            counter += 1
        last = pixel
    return counter

def extract(roi):
    #roi = cv.bitwise_not(roi)
    (roiW, roiH) = roi.shape
    roi_area = roi.shape[0]*roi.shape[1]
    total_on = cv.countNonZero(roi)/(roiW*roiH)
    #2
    width_of_cut = 5
    middle_x_line = roi[:,math.floor(roiH//2):math.floor(roiH//2)+width_of_cut]
    total_middle_x = cv.countNonZero(middle_x_line)/(width_of_cut*roiW)
    #3
    width_of_cut = 5
    middle_y_line = roi[math.floor(roiW//2):math.floor(roiW//2)+width_of_cut,:]
    total_middle_y = cv.countNonZero(middle_y_line)/(width_of_cut*roiH)
    #4
    lower = roi[:,math.floor(roiH//2)::]
    lower_area = lower.shape[0]*lower.shape[1]
    total_lower = cv.countNonZero(lower)/(lower_area)
    #5
    left = roi[::math.floor(roiW//2),:]
    left_area = left.shape[0]*left.shape[1]
    total_left = cv.countNonZero(left)/(left_area)
    #6
    upper = roi[:,::math.floor(roiH//2)]
    up_area = upper.shape[0]*upper.shape[1]
    total_up = cv.countNonZero(upper)/(up_area)
    #7
    right = roi[math.floor(roiW//2)::,:]
    right_area = right.shape[0]*right.shape[1]
    total_right = cv.countNonZero(right)/(right_area)
    #8
    lines_cut_hor = lines_counting(roi,1,roiH//4)
    #9
    lines_cut_ver = lines_counting(roi,0,roiW//4)

    features_values = np.zeros((FEATURES_NUMBER))
    features_values[0] = total_on
    features_values[1] = total_middle_x
    features_values[2] = total_middle_y
    features_values[3] = total_lower
    features_values[4] = total_left
    features_values[5] = total_up
    features_values[6] = total_right
    features_values[7] = lines_cut_hor/2
    features_values[8] = lines_cut_ver/2

    return features_values
