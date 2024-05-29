#import libraries
import pygame as p
import sys

#import classes
from constant import *

#create screen setup
p.init()
screen = p.display.set_mode( (WIDTH, HEIGHT) )
p.display.set_caption("TicTacToe")
screen.fill( BKG_COLOR ) 

class Board:
    
    def __init__(self):
        pass

class Game:
    
    def __init__(self):
        selg.board = Board()
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
    while True:
        game = Game()

        for event in p.event.get():
            
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
                
        p.display.update()  #can also use flip

main_loop()