#new user controlled snake game

import curses
import time
import random
import sys
from copy import copy, deepcopy

# for the transparency purposes
steps = []
screen = curses.initscr()
screen.keypad(1)
curses.noecho()
curses.curs_set(0)
dims = screen.getmaxyx()
highestScore = 0

HEIGHT = 20
WIDTH = 30
FIELD_SIZE = HEIGHT * WIDTH

HEAD = 0
APPLE = 0
UNDEFINED = (HEIGHT + 1) * (WIDTH + 1)
SNAKE = 2 * UNDEFINED

LEFT = -1
RIGHT = 1
UP = -WIDTH
DOWN = WIDTH

BOARD = [0]*FIELD_SIZE
originalLength = 3

def make_move():
    return ''