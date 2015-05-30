import curses
import time
import random
import sys

screen = curses.initscr()
screen.nodelay(1)
head = [1, 1]
body = [head[:]]*5

screen.border()

direction = 0 # 0: right, 1: down, 2: left, 3: up
gameOver = False

while not gameOver:
    addch(head[0], head[1], '*')
    if (direction == 0):
        head[1] += 1
    elif (direction == 1):
        head[0] += 1
    elif (direction == 2):
        head[1] -= 1
    elif (direction == 3):
        head[0] -= 1
# # Initial user interface: Curses
# #initializes curses to use it
# curses.initscr()
# # avoid the need to echo to the screen
# curses.noecho()
# # reacts to the keys instantly without requiring the enter key to be pressed
# curses.cbreak()
# curses.curs_set(0)
#
# height = 20
# width = 50
# begin_x = 0
# begin_y = 0
# #creates a new window of a given size, returning the new window object.
# # win = curses.newwin(height, width, begin_x, begin_y)
# #
# # win.keypad(True)
# # win.border(0)
# # win.nodelay(1)
# # # the location of the apple
# # win.addch(0, 0, '@')
# #event = win.getch()
# #enables the uses of normal and special keys
# #win.keypad(True)
#
# APPLE = 0
# POINT = 0
# board = []
# SNAKE = []

def intro():
    print('Welcome to the Snake game. Before we start, you can customerize the game by seting the board height, width. ')
    print('Please type the height, width, original snake lengths, auto(exit by pressing esc) or manual control here, separated by a space. ')
    print('Press enter if you want the default size. ')
    the_input = input('>>>')
    #print(the_input)
    if the_input:
        input_list = the_input.split( )
        print(input_list)
    else:
        input_list = []
#
# def play() :
#     while (1):
#         win.border(0)
#         win.addch(0, 3, 'P')
#         event = win.getch()

#function to run the snake with BFSS
def runBFS():
    return ""

#curses.endwin()
intro()
# Initial user interface: Curses
#initializes curses to use it
screen = curses.initscr()
screen.addstr(0, 0, 'Hello World!')
# avoid the need to echo to the screen
curses.noecho()
# reacts to the keys instantly without requiring the enter key to be pressed
curses.cbreak()
    curses.curs_set(0)

height = 20
width = 50
begin_x = 0
begin_y = 0
#creates a new window of a given size, returning the new window object.
win = curses.newwin(height, width, begin_x, begin_y)

win.keypad(True)
win.border(0)
win.nodelay(1)
# the location of the apple
win.addch(0, 0, '@')
event = win.getch()
#enables the uses of normal and special keys
win.keypad(True)

APPLE = 0
POINT = 0
board = []
SNAKE = []