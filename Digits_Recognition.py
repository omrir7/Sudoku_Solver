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
	#gray = digit_img
	threshold_value, thresh = cv.threshold(gray, 155, 255, cv.THRESH_BINARY)
	# kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (1, 5))
	# thresh = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
	#cv.imshow('thresh', thresh)
	#cv.waitKey(500)
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
def maxCorr(roi,ref_images):
	corr = np.zeros((10))
	for k in range(0, 10):
		#cv.imshow('ref',ref_images[k])
		#cv.waitKey(500)
		roi_ref = gen_roi_of_digit(ref_images[k])
		roi_ref = cv.resize(roi_ref,(roi.shape[1],roi.shape[0]))
		#cv.imshow('roiref',roi_ref)
		#cv.waitKey(500)
		#cv.imshow('roi',roi)
		#cv.waitKey(500)
		#cv.imshow('roi',roi)
		#cv.waitKey(0)
		#cv.imshow('roiref', roi_ref)
		#cv.waitKey(50)
		corr[k] = np.sum(roi == roi_ref) / roi.size
	if np.count_nonzero(roi) == 0:
		return 0
	else:
		return np.argmax(corr)

def recognize_digit(digit_img,ref_images):
	roi = gen_roi_of_digit(digit_img)
	features = extract(roi,digit_img)
	digit = maxCorr(roi,ref_images)
	#distinguish between 3,8, according to right-left ratio
	if digit == 8:
		left_right_ratio = np.count_nonzero(roi[:,0:roi.shape[1]//2])/np.count_nonzero(roi[:,roi.shape[1]//2::])
		if left_right_ratio<0.8:
			digit=3
	#distinguish between 1,4, according to number of bottom on bits
	if digit == 4:
		strip=150
		botton_off_bits = np.count_nonzero(roi[roi.shape[0]-strip:roi.shape[0]-1,:])
		#print(botton_off_bits)
		if botton_off_bits<10000:
			digit=1

	return digit


