import cv2 as cv
from Defeinitions import *
import numpy as np
import math

#returns the digits splited digits one by one, up->down and than left->right
def split(path):
    img = cv.imread(path)
    img = cv.resize(img,(Image_Size,Image_Size),interpolation=cv.INTER_CUBIC)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray = cv.bitwise_not(gray)
    blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
    #--------------------------------------------------------------
    _,thresh = cv.threshold(blur,50,255,cv.THRESH_BINARY)
    digits = []
    i=0
    contours, hierarchy = cv.findContours(thresh, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
    img2 = img.copy()
    maxArea=0
    maxFrame = 0
    for cnt in contours:
        approx = cv.approxPolyDP(cnt, .02 * cv.arcLength(cnt, True), True)
        area = cv.contourArea(cnt)
        if len(approx)==4 and area>maxArea:
            maxArea = area
            maxFrame = approx
    a= maxFrame[0,0,1]
    b=maxFrame[3,0,0]
    c=maxFrame[3,0,1]
    d=maxFrame[1,0,1]
    img = img2[a:b,c:d]
    #-------------------------------------------------------------------------------------
    for row in range(0,(Sudoku_Size)):
        for col in range(0, (Sudoku_Size)):
            start_y = math.floor(row*img.shape[1]/(Sudoku_Size))+15
            end_y = math.floor((row+1)*img.shape[1]/(Sudoku_Size))-15
            start_x = math.floor(col*img.shape[0]/(Sudoku_Size))+15
            end_x = math.floor((col+1)*img.shape[0]/(Sudoku_Size))-15
            digits.append(img[start_x:end_x,start_y:end_y])
            #cv.imshow('dig',digits[i])
            i+=1
            #cv.waitKey(500)
    return digits

split("Soduko_Images/1.png")
