import pygame as p
import sys
import numpy as np #used to work with arrays and do some mathematic equations

from main import *
from constant import *

class Board:
    
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS)) #based on the amount of rows and cols prints a board with zeroes
        self.mark_square(1, 1, 2)
        print(self.squares)
        
    def mark_square(self, row, col, player):
        #program works by follwing setup:
        #when player(1 or 2) clicks on a square it becomes marked with 1 or 2
        #one is for cross, and 2 for circles
        
        self.squares[row][col] = player #square number is player number.