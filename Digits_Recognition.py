# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2 as cv
from Defeinitions import *
import numpy as np


def minMSE (arr):
	mseArr = np.zeros((10))
	for i in range (0,10):
		mseArr[i] = np.mean((arr-DIGITS_LOOKUP[i])**2)
	return np.argmin(mseArr)

def recognize_digit(digit_img):
	digit_img=cv.resize(digit_img,(500,500))
	gray = cv.cvtColor(digit_img,cv.COLOR_BGR2GRAY)
	#gray = digit_img
	threshold_value,thresh = cv.threshold(gray,155,255,cv.THRESH_BINARY)
	#kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (1, 5))
	#thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
	cv.imshow('thresh',thresh)
	cv.waitKey(500)
	cnts = cv.findContours(thresh.copy(), cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	digitCnts = contours.sort_contours(cnts,method="left-to-right")[0]
	max=0
	maxcont = cnts[0]
	for c in digitCnts:
		# compute the bounding box of the contour
		(x, y, w, h) = cv.boundingRect(c)
		# if the contour is sufficiently large, it must be a digit
		if w*h>max:
			maxcont = c
	c=maxcont
	(x, y, w, h) = cv.boundingRect(c)
	roi = thresh[y:y + h, x:x + w]

	roi = cv.bitwise_not(roi)
	cv.imshow('roi',roi)
	cv.waitKey(500)
	(roiH, roiW) = roi.shape
	#features:
	#1.total on pixels
	#2.cut in the midle x and count how many on lines
	#3.cut in the midle y and count how many on lines

	#1
	total_on = cv.countNonZero(roi)/365
	#2
	middle_x_line = roi[0:roiW-1,roiH//2]
	total_middle_x = cv.countNonZero(middle_x_line)
	#3
	middle_y_line = roi[roiW//2,0:roiH-1]
	total_middle_y = cv.countNonZero(middle_y_line)

	digit = minMSE([total_on,total_middle_x,total_middle_y])
	return digit


