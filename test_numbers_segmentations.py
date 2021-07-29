import imutils
import cv2 as cv
from imutils import contours
from Defeinitions import *
import pandas as pd
import numpy as np


img = [0] * 9
features_values = np.zeros((10,FEATURES_NUMBER))
counter = 0
for k in range(1,10):
	img[k-1] = cv.imread("Soduko_Images/only/"+str(k)+".png")
	img[k-1]=cv.resize(img[k-1],(500,500))
	#threshold_value,thresh = cv.threshold(img[k],155,255,cv.THRESH_BINARY)
	gray = cv.cvtColor(img[k-1],cv.COLOR_BGR2GRAY)
	cnts = cv.findContours(gray.copy(), cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	# sort the contours from left-to-right, then initialize the
	# actual digits themselves
	digitCnts = contours.sort_contours(cnts,method="left-to-right")[0]
	digits = []
	# loop over each of the digits
	max=0
	maxcont = cnts[0]
	for c in digitCnts:
		# compute the bounding box of the contour
		(x, y, w, h) = cv.boundingRect(c)
		# if the contour is sufficiently large, it must be a digit
		if w*h>max:
			maxcont = c
	# extract the digit ROI
	c=maxcont
	(x, y, w, h) = cv.boundingRect(c)
	roi = gray[y:y + h, x:x + w]

	# compute the width and height of each of the 7 segments
	# we are going to examine
	(roiH, roiW) = roi.shape
	# define the set of 7 segments
	roi = cv.bitwise_not(roi)
	total = cv.countNonZero(roi)
	#2
	middle_x_line = roi[0:roiW-1,roiH//2]
	total_middle_x = cv.countNonZero(middle_x_line)
	#3
	middle_y_line = roi[roiW//2,0:roiH-1]
	total_middle_y = cv.countNonZero(middle_y_line)

	features_values[k,0] = total/365
	features_values[k,1] = total_middle_x
	features_values[k,2] = total_middle_y

features_values[0,0] = 0
features_values[0,1] = 0
features_values[0,2] = 0

dataframe = pd.DataFrame(features_values)
dataframe.to_csv(r"C:/Users/omrir/PycharmProjects/SodukoSolver/Single_dig_Features.csv")
#for i in range (0,10):
#	print(str(i)+": "+str(features_values[i]))