#import libraries
import pygame as p
import sys
import numpy as np

#import classes
from constant import *

#create screen setup
p.init()
screen = p.display.set_mode( (WIDTH, HEIGHT) )
p.display.set_caption("TicTacToe")
screen.fill( BKG_COLOR ) 

class Board:
    
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS)) #based on the amount of rows and cols prints a board with zeroes
        
        
    def mark_square(self, row, col, player):
        #program works by follwing setup:
        #when player(1 or 2) clicks on a square it becomes marked with 1 or 2
        #one is for cross, and 2 for circles
        
        self.squares[row][col] = player #square number is player number.
        
    def empty_square(self, row, col):
        
        return self.squares[row][col] == 0

class Game:
    
    def __init__(self):
        self.board = Board()     #from board class
        self.player = 1          #player1 turn in the beginning
        self.show_lines()
    
    def show_lines(self):
        #vert just took them from a yt video
        p.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        p.draw.line(screen, LINE_COLOR, (WIDTH - SQUARE_SIZE, 0), (WIDTH - SQUARE_SIZE , HEIGHT), LINE_WIDTH)
        
        #horiz
        p.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        p.draw.line(screen, LINE_COLOR, (0, HEIGHT- SQUARE_SIZE), (WIDTH, HEIGHT - SQUARE_SIZE), LINE_WIDTH)

#mainLoop for the game
def main_loop():
    
    #object for game
    game = Game()
    board = game.board  #so i would not write game.board all the time
    
    #mainloop
    while True:

        for event in p.event.get():
            
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
                
            if event.type == p.MOUSEBUTTONDOWN:  #listens for mouseclickevent
                pos = event.pos     #change value for pygame.pos so it would positions for my game
                row = pos[1]  // SQUARE_SIZE
                col = pos[0]  // SQUARE_SIZE
                
                if board.empty_square(row, col):
                    board.mark_square(row, col, 1) #one is for player.
                    print(board.squares)
                
            
                
        p.display.update()  #can also use flip

main_loop()