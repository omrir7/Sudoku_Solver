import Digits_Recognition
import Spliting
from Spliting import *
from Digits_Recognition import *
class Sudoku_Board():
	def __init__(self,path):
		board_matrix = [[0 for x in range(Sudoku_Size)] for y in range(Sudoku_Size)]
		digits = Spliting.split(path)
		i=0
		for col in range(0,Sudoku_Size):
			for row in range(0,Sudoku_Size):
				board_matrix[row][col] = Digits_Recognition.recognize_digit(digits[i])
				i+=1
		for row in range(0,Sudoku_Size):
			print(str(board_matrix[row]))

sod1 = Sudoku_Board("Soduko_Images/4.png")
