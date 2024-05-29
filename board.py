import pygame as p
import sys
import numpy as np #used to work with arrays and do some mathematic equations

from main import *
from constant import *

class Board:
    
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS)) #based on the amount of rows and cols prints a board with zeroes
        
    def mark_square(self, row, col, player): 
        pass