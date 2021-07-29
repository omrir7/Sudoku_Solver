import numpy as np
from numpy import genfromtxt

Image_Size = 1000
Sudoku_Size = 9
FEATURES_NUMBER = 9

DIGITS_LOOKUP = np.zeros((10,FEATURES_NUMBER))
DIGITS_LOOKUP = genfromtxt('C:/Users/omrir/PycharmProjects/SodukoSolver/Single_dig_Features.csv', delimiter=',')
DIGITS_LOOKUP = np.delete(DIGITS_LOOKUP,0,0)
DIGITS_LOOKUP = np.delete(DIGITS_LOOKUP,0,1)

#print("Reference Digits Features Values:")
#print (DIGITS_LOOKUP)