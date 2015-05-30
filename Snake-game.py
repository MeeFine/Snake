import curses
import time
import random
import sys

screen = curses.initscr()
dims = screen.getmaxyx()
def game():
    screen.nodelay(1)
    head = [1, 1]
    score = 0
    body = [head[:]]*5

    screen.border()

    direction = 0 # 0: right, 1: down, 2: left, 3: up
    gameOver = False

    while not gameOver:
        screen.addch(head[0], head[1], '*')
        if (direction == 0):
            head[1] += 1
        elif (direction == 1):
            head[0] += 1
        elif (direction == 2):
            head[1] -= 1
        elif (direction == 3):
            head[0] -= 1

        for z in range(0, len(body)-1, 1):
            body[z] = body[z-1]
        # if it touches something other than the space, then game over
        if screen.inch(head[0], head[1]) != ord(' '):
            gameOver = True
        screen.refresh()
        time.sleep(0.1)

game()
curses.endwin()