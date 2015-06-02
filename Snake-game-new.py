#new user controlled snake game

import curses
import time
import random
import sys
from copy import copy, deepcopy

# for the transparency purposes
steps = []
curses.initscr()

curses.noecho()
curses.curs_set(0)

highestScore = 0

HEIGHT = 20
WIDTH = 30
FIELD_SIZE = HEIGHT * WIDTH
win = curses.newwin(HEIGHT, WIDTH, 0, 0)
win.keypad(1)
dims = win.getmaxyx()
win.nodelay(1)


HEAD = 0
APPLE = 0
UNDEFINED = (HEIGHT + 1) * (WIDTH + 1)
SNAKE = 2 * UNDEFINED

LEFT = -1
RIGHT = 1
UP = -WIDTH
DOWN = WIDTH

MOVE_LIST = [LEFT, RIGHT, UP, DOWN]

BOARD = [0]*FIELD_SIZE
originalLength = 3


def make_move(idx, move, key):
    if (is_move_possible(idx, move)):
        return ''
    return move


def is_move_possible(idx, move):
    flag = False
    if move == LEFT:
        flag = True if idx%WIDTH > 1 else False
    elif move == RIGHT:
        flag = True if idx%WIDTH < (WIDTH-2) else False
    elif move == UP:
        flag = True if idx > (2*WIDTH-1) else False # 即idx/WIDTH > 1
    elif move == DOWN:
        flag = True if idx < (FIELD_SIZE-2*WIDTH) else False # 即idx/WIDTH < HEIGHT-2
    return flag

def play(idx, move, key):
    while (key != 27):
        win.timeout(5)
        win.addch(2, 5, '@')
        keyInput = win.getch()
        key = keyInput
        for i in range(3):
            win.addch(10, i, '*')
        BOARD
        #make_move()

play(30, RIGHT, 1)