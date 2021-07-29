import numpy as np

Image_Size = 1000
Sudoku_Size = 9
FEATURES_NUMBER = 3

DIGITS_LOOKUP = np.zeros((10,FEATURES_NUMBER))
DIGITS_LOOKUP[0]= [0,       0,      0]
DIGITS_LOOKUP[1]= [68.42739726 , 0,         54,             ]
DIGITS_LOOKUP[2]= [ 77.89041096, 177,          48,           ]
DIGITS_LOOKUP[3]= [ 96.52328767 ,186,          55,           ]
DIGITS_LOOKUP[4]= [27.05479452, 57,         59,              ]
DIGITS_LOOKUP[5]= [ 99.5890411, 109,         52,             ]
DIGITS_LOOKUP[6]= [21.39452055,  8,         22,              ]
DIGITS_LOOKUP[7]= [ 52.19452055, 111,          50,           ]
DIGITS_LOOKUP[8]= [18.5013698, 20,         10,              ]
DIGITS_LOOKUP[9]= [26.48493151, 15,         24,              ]
