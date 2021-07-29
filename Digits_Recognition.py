# import the necessary packages
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2 as cv
from Defeinitions import *
import numpy as np
from Features_Extraction import *

def gen_roi_of_digit(digit_img):
	digit_img = cv.resize(digit_img, (500, 500))
	gray = cv.cvtColor(digit_img, cv.COLOR_BGR2GRAY)
	# gray = digit_img
	threshold_value, thresh = cv.threshold(gray, 155, 255, cv.THRESH_BINARY)
	# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (1, 5))
	# thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
	#cv.imshow('thresh', thresh)
	#cv.waitKey(1000)
	thresh = cv.bitwise_not(thresh)
	cnts = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	if (len(cnts) > 0):
		digitCnts = contours.sort_contours(cnts, method="left-to-right")[0]
		max = 0
		maxcont = cnts[0]
		for c in digitCnts:
			# compute the bounding box of the contour
			(x, y, w, h) = cv.boundingRect(c)
			# if the contour is sufficiently large, it must be a digit
			if cv.contourArea(c) > 25000 and cv.contourArea(c) < 50000:
				maxcont = c
		(x, y, w, h) = cv.boundingRect(maxcont)
	else:
		(x, y, w, h) = (0, 0, 500, 500)
	# print(cv.contourArea(maxcont))
	roi = thresh[y:y + h, x:x + w]
	#cv.imshow('roi',roi)
	#cv.waitKey(500)
	return roi

def minMSE (arr):
	mseArr = np.zeros((10))
	for i in range (0,10):
		mseArr[i] = np.mean((arr-DIGITS_LOOKUP[i])**2)
	return np.argmin(mseArr)

def recognize_digit(digit_img):
	roi = gen_roi_of_digit(digit_img)
	#roi = cv.bitwise_not(roi)
	features = extract(roi)
	digit = minMSE(features)
	return digit


