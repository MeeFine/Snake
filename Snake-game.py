import curses
import time
import random
import sys
from copy import copy, deepcopy


screen = curses.initscr()
screen.keypad(1)
curses.noecho()
curses.curs_set(0)
dims = screen.getmaxyx()
highestScore = 0
def game(highestScore):
    screen.clear()
    originalLength = 3
    screen.nodelay(1)
    head = [5, 2]
    headCopy = deepcopy(head)
    foodMade = False
    currentScore = 0
    #default body size = 3
    count = 0
    body = []
    for i in range(originalLength):
        body.append(head)
    screen.border()
    previousBody = copy(body[-1])
    #print(previous)
    direction = 0 # 0: right, 1: down, 2: left, 3: up
    gameOver = False

    while not gameOver:
        if(count < originalLength+2):
            count += 1
        # randomly generates the food
        while not foodMade:
            y, x = random.randrange(1, dims[0] -1),random.randrange(1, dims[1] -1)
            if screen.inch(y,x) == ord(' '):
                foodMade = True
                screen.addch(y,x, '@')
        if (count == originalLength+1):
            screen.addch(headCopy[0], headCopy[1], ' ')
        # get rid of the previous body
        if (previousBody not in body):
            #screen.addch(5, 2, ' ')
            screen.addch(previousBody[0], previousBody[1], ' ')


        screen.addch(head[0], head[1], '*')
        #get the keypad input from the user
        action = screen.getch()

        if ((action == curses.KEY_UP or action == ord('w')) and direction != 1):
            direction = 3
        elif ((action == curses.KEY_DOWN or action == ord('s')) and direction != 3):
            direction = 1
        elif ((action == curses.KEY_RIGHT or action == ord('d')) and direction != 2):
            direction = 0
        elif ((action == curses.KEY_LEFT or action == ord('a')) and direction != 0):
            direction = 2
        # updates the snake head
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

        body[0] = copy(head)
        # if it touches something other than the space, then game over
        if screen.inch(head[0], head[1]) != ord(' '):
            if screen.inch(head[0], head[1]) == ord('@'):
                foodMade = False
                body.append(body[-1])
            else:
                gameOver = True
        screen.refresh()
        time.sleep(0.1)
    currentScore = len(body)-originalLength
    # keep track of the maximum score
    if(currentScore > highestScore):
        highestScore = currentScore
    screen.clear()
    screen.nodelay(0)
    # some messages at the game over page
    message1 = 'Game over'
    stringMessage = ''
    if currentScore <= 1:
        stringMessage += ' point. '
    elif currentScore > 1:
        stringMessage += ' points. '
    currentScoreString = str(currentScore)
    highestScoreString = str(highestScore)
    message2 = 'You got ' + currentScoreString + stringMessage
    message3 = 'Highest score: ' + highestScoreString
    message4 = 'Press enter to quit'
    message5 = 'press space to play again. '
    screen.addstr(dims[0]//2 - 3, (dims[1]-len(message1))//2, message1)
    screen.addstr(dims[0]//2 - 2, (dims[1]-len(message2))//2, message2)
    screen.addstr(dims[0]//2 - 1, (dims[1]-len(message3))//2, message3)
    screen.addstr(dims[0]//2, (dims[1]-len(message4))//2, message4)
    screen.addstr(dims[0]//2 + 1, (dims[1]-len(message5))//2, message5)

    screen.refresh()
    q = 0
    #32 - space; 10 - enter
    while q not in [32, 10]:
        q = screen.getch()
    if q == 32:
        #screen.clear()
        game(highestScore)
def menu():
    screen.nodelay(0)
    screen.clear()
    selection = -1
    option = 0
    while (selection < 0):
        graphics = [0]*3
        graphics[option] = curses.A_REVERSE
        welcomeString = 'Welcome to the Snake game.'
        screen.addstr(5, (dims[1]-len(welcomeString))//2, welcomeString)
        screen.addstr(dims[0]//2 - 2, dims[1]//2 - 12, 'User Controlled Play Mode', graphics[0])
        screen.addstr(dims[0]//2 - 1, dims[1]//2 - 8, 'Auto Play Mode', graphics[1])
        screen.addstr(dims[0]//2 , dims[1]//2 - 5, 'Exit', graphics[2])
        screen.refresh()
        action = screen.getch()
        if (action == curses.KEY_UP):
            option = (option -1) % 3
        elif (action == curses.KEY_DOWN):
            option = (option + 1) % 3
        elif action == ord('\n'):
            selection = option

    if (selection == 0):
        game(highestScore)
        screen.clear()


        # screen.addstr(dims[0]/2 - 2, dims[1]/2-2, , graphics[0])
        # screen.addstr(dims[0]/2 - 2, dims[1]/2-2, , graphics[0])
menu()
#game(highestScore)
curses.endwin()