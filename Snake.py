import curses
# Initial user interface: Curses
#initializes curses to use it
curses.initscr()
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

while (1):
    win.border(0)
    win.addch(0, 3, 'P')
    event = win.getch()

#function to run the snake with BFSS
def runBFS():
    return ""

curses.endwin()