import curses
import time
import random
import sys
from copy import copy

screen = curses.initscr()
dims = screen.getmaxyx()
def game():
    screen.nodelay(1)
    head = [1, 1]
    score = 0
    #default body size = 3
    body = copy(head)
    body = body * 3

    screen.border()
    previous = copy(body[-1])
    direction = 0 # 0: right, 1: down, 2: left, 3: up
    gameOver = False

    while not gameOver:
        if (previous not in body):
            screen.addch(previous[0], previous[1], ' ')
        screen.addch(head[0], head[1], '*')
        if (direction == 0):
            head[1] += 1
        elif (direction == 1):
            head[0] += 1
        elif (direction == 2):
            head[1] -= 1
        elif (direction == 3):
            head[0] -= 1

        previousBody = copy(body[-1])
        for i in range(len(body)-1, 0, -1):
            body[i] = copy(body[i-1])
        # if it touches something other than the space, then game over
        if screen.inch(head[0], head[1]) != ord(' '):
            gameOver = True
        screen.refresh()
        time.sleep(0.1)

game()
curses.endwin()