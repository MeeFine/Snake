import curses
# Initial user interface: Curses
#initializes curses to use it
stdscr = curses.initscr()
# avoid the need to echo to the screen
curses.noecho()
# reacts to the keys instantly without requiring the enter key to be pressed
curses.cbreak()
#enables the uses of normal and special keys
stdscr.keypad(True)

height = 10
width = 15
begin_x = 5
begin_y = 5
#creates a new window of a given size, returning the new window object.
win = curses.newwin(height, width, begin_x, begin_y)


#function to run the snake with BFSS
def runBFS():
    return ""