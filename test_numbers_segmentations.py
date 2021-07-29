import imutils
import cv2 as cv
from imutils import contours
from Defeinitions import *
import pandas as pd
import numpy as np
from Features_Extraction import *
from Digits_Recognition import *

img = [0] * 9
features_values = np.zeros((10,FEATURES_NUMBER))
counter = 0
for k in range(1,10):
	img[k-1] = cv.imread("Soduko_Images/only/"+str(k)+".png")
	#threshold_value,thresh = cv.threshold(img[k],155,255,cv.THRESH_BINARY)
	roi = gen_roi_of_digit(img[k-1])
	features = extract(roi)
	features_values[k] = features

dataframe = pd.DataFrame(features_values)
dataframe.to_csv(r"C:/Users/omrir/PycharmProjects/SodukoSolver/Single_dig_Features.csv")
#for i in range (0,10):
#	print(str(i)+": "+str(features_values[i]))