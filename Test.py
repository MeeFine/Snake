import curses
import time

screen = curses.initscr()
#screen.nodelay(1)
dims = screen.getmaxyx() #should return (24, 80)
curses.noecho()
screen.keypad(1)
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_CYAN)
curses.curs_set(0)
q = -1
x, y = 1, 1
Ver = 1
Hori = 1
# while(1):
screen.border()
while(q != ord('q')):
    #screen.clear()
    screen.addch(y, x, '@', curses.color_pair(1))
    screen.refresh()
    q = screen.getch()
    screen.addch(y, x, ' ')
    if (q == curses.KEY_UP and y > 1):
        y -= 1
    elif (q == curses.KEY_DOWN and y < dims[0] - 2):
        y += 1
    elif (q == curses.KEY_LEFT and x > 1) :
        x -= 1
    elif (q == curses.KEY_RIGHT and x < dims[1] - 2):
        x += 1


    # y += Ver
    # x += Hori
    # if (y == dims[0] - 1):
    #     Ver = -1
    # elif (y == 0):
    #     Ver = 1
    #
    # if(x == dims[1] - 1 - len('CSE 415')):
    #     Hori = -1
    # elif (x == 0):
    #     Hori = 1
    #q = screen.getch()
    #time.sleep(0.02)
screen.getch()
curses.endwin()