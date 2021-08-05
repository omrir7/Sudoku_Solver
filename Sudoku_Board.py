import cv2

import Digits_Recognition
import Spliting
from Spliting import *
from Digits_Recognition import *

def read_ref_images():
	img = [0] * 10


	#img[0] = np.zeros((500, 500,3))
	for k in range(1, 10):
		img[k] = cv.imread("Soduko_Images/only/" + str(k) + ".png")
		img[k] = cv.resize(img[k], (500, 500))
	img[0] = img[1]*0
	return img

class Sudoku_Board():
	def __init__(self,path):
		ref_images = read_ref_images()
		self.board_matrix = [[0 for x in range(Sudoku_Size)] for y in range(Sudoku_Size)]
		digits = Spliting.split(path)
		i=0
		for col in range(0,Sudoku_Size):
			for row in range(0,Sudoku_Size):
				self.board_matrix[row][col] = Digits_Recognition.recognize_digit(digits[i],ref_images)
				i+=1
		#print(DIGITS_LOOKUP)
		print("Sudoku Board: ")
		for row in range(0,Sudoku_Size):
			print(str(self.board_matrix[row]))

sod1 = Sudoku_Board("Soduko_Images/8.png")
