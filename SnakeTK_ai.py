'''Create by Ziming Guo and Weiyou Dai'''
from tkinter import *
from random import randrange
from copy import deepcopy


class SnakeGame():
    def __init__(self):
        self.root = Tk()
        self.Run = False
        self.refresh = 0

        self.width = 10
        self.height = 10
        self.bsize = 10
        #creates a tkinter user interface
        self.frame = Frame()
        self.frame.pack()

        self.canvas = Canvas(self.frame, bg="black", width=self.width*self.bsize, height=self.height*self.bsize)
        self.canvas.pack()

        self.wlabel = Label(self.frame, fg="black", text="Width")
        self.wlabel.pack(side="left")
        self.wentry = Entry(self.frame)
        self.wentry.pack(side="left")
        self.wentry.insert(0, str(self.width))
        self.hlabel = Label(self.frame, fg="black", text="Height")
        self.hlabel.pack(side="left")
        self.hentry = Entry(self.frame)
        self.hentry.pack(side="left")
        self.hentry.insert(0, str(self.height))
        #creates a buttom for the user to choose to run by themselves
        self.button = Button(self.frame, text="Run / Restart", command=self.start_human)
        self.button.pack()
        #creates a buttom for the user to choose to auto-run
        self.button = Button(self.frame, text="AutoRun", command=self.start_ai)
        self.button.pack()

        self.root.mainloop()

    # agent start function
    def start_ai(self):
        self.refresh += 1
        self.Run = True
        #set up the speed of the agent snake
        self.speed = 5
        self.size = 6
        self.originalSize = 6
        #represents the snake as an array
        self.snake = []
        # set up the initial direction to east
        self.di = "E"
        # write the data to a text file for transparency purpose
        file = open("snake_data.txt", "w")
        # gets the user input as width
        new_w = eval(self.wentry.get())
        # gets the user input as height
        new_h = eval(self.hentry.get())
        if new_w != self.width or new_h != self.height:
            # judges if the user input and default setting are the same
            self.width = new_w
            self.height = new_h
            self.canvas.config(width=self.width*self.bsize, height=self.height*self.bsize)
        # defines the snake head
        self.head = (self.width // 2, self.height // 2)
        for i in range(self.size):
             # initializes the snake
            self.snake.append((self.head[0]-i, self.head[1]))
        # initializes the snake on the GUI
        for i in range(self.size):
            self.canvas.create_rectangle(t2coord(self.snake[i], self.bsize), width=0, fill="yellow")
        self.nexthead = self.test_move(self.snake[0], self.di)

        self.create_food()
        self.canvas.create_rectangle(t2coord(self.food, self.bsize), width=0, fill="green")

        # self.refresh = False
        self.game_begin_ai(self.refresh, file)

    def game_begin_ai(self, currentLoop, file):
        if self.refresh > currentLoop:
            return
        if self.Run is True:
            self.snake.insert(0, self.nexthead)
            if self.nexthead != self.food:
                self.snake.pop()
            else:
                self.create_food()
                self.size += 1
            newmove = self.find_move()
            if newmove != "":
                self.di = newmove
            # write the current head position and the direction it moves to to the terminal and the text file
            file.write("next: ")
            currentState = "Current head position: "+ str(self.nexthead)+ ", Now move to: " + self.di
            file.write(currentState)
            print(currentState)
            # snake moves
            self.nexthead = self.test_move(self.snake[0], self.di)
            if self.nexthead in self.snake:
                self.Run = False
            self.paint_ai()
            # acts like a while loop
            self.root.after(self.speed, lambda: self.game_begin_ai(currentLoop, file))
        else:
            file.close()
            if self.size == self.width * self.height:
                self.canvas.create_text(self.width // 2 * self.bsize, self.height // 2 * self.bsize, fill="red",
                                    font=("Helvetica", self.width // 2), text="Congratulations! Game Complete!")
            else:
                self.canvas.create_text(self.width // 2 * self.bsize, self.height // 2 * self.bsize, fill="red",
                                    font=("Helvetica", self.width // 2), text="Game Over")

    def start_human(self):
        self.refresh += 1
        self.Run = True
        # self.points = 0
        self.speed = 150
        self.size = 3
        self.snake = []
        self.di = "E"

        new_w = eval(self.wentry.get())
        new_h = eval(self.hentry.get())
        if new_w != self.width or new_h != self.height:
            self.width = new_w
            self.height = new_h
            self.canvas.config(width=self.width*self.bsize, height=self.height*self.bsize)
        self.head = (self.width // 2, self.height // 2)
        for i in range(self.size):
            self.snake.append((self.head[0]-i, self.head[1]))
        for i in range(self.size):
            self.canvas.create_rectangle(t2coord(self.snake[i], self.bsize), width=0, fill="yellow")

        self.create_food()
        self.canvas.create_rectangle(t2coord(self.food, self.bsize), width=0, fill="green")

        self.root.bind("<Up>", lambda event: self.turn("N"))
        self.root.bind("<Down>", lambda event: self.turn("S"))
        self.root.bind("<Left>", lambda event: self.turn("W"))
        self.root.bind("<Right>", lambda event: self.turn("E"))

        self.game_begin_human(self.refresh)

    def game_begin_human(self, currentLoop):
        if self.refresh > currentLoop:
            return
        if self.Run is True:
            temphead = self.test_move(self.snake[0], self.di)
            if temphead in self.snake:
                self.Run = False
            if self.Run is True:
                self.snake.insert(0, temphead)
                if temphead != self.food:
                    self.snake.pop()
                else:
                    self.create_food()
                    self.size += 1
                self.paint()
            self.root.after(self.speed, lambda cur=currentLoop: self.game_begin_human(cur))
        else:
            if self.size == self.width * self.height:
                self.canvas.create_text(self.width // 2 * self.bsize, self.height // 2 * self.bsize, fill="red",
                                    font=("Helvetica", self.width // 2), text="Congratulations! Game Complete!")
            else:
                self.canvas.create_text(self.width // 2 * self.bsize, self.height // 2 * self.bsize, fill="red",
                                        font=("Helvetica", self.width ), text="Game Over")
    # move the snake head
    def test_move(self, head, direct):
        if direct == "E" and head[0] < self.width-1:
            # if does not run into the border, move to the east direction
            head = (head[0] + 1, head[1])
        elif direct == "W" and head[0] > 0:
            # if does not run into the border, move to the west direction
            head = (head[0] - 1, head[1])
        elif direct == "N" and head[1] > 0:
            # if does not run into the border, move to the north direction
            head = (head[0], head[1] - 1)
        elif direct == "S" and head[1] < self.height-1:
            # if does not run into the border, move to the south direction
            head = (head[0], head[1] + 1)
        return head
    # finds the next valid move
    def find_move(self):
        # initializes the board the snake is running in
        self.board = {(i, j): (self.width + 1) * (self.height + 1) for i in range(self.width) for j in range(self.height)}
        # resets the board for the virtual exploration purposes
        self.reset_board(self.snake, len(self.snake), self.board)
        # gets the distances from the grid to the apple
        if self.can_get_food(self.food, self.snake, self.board):
            # first virtually move to the next position
            self.virtual_move()
            if self.virtual_explore():
                #if it is valid to do the virtual move
                return self.shortest_move(self.snake, self.board)
            else:
                # otherwise just follow the snake's tail to survive longer
                return self.follow_tail()
        else:
            # can not get the food, just follows the snake's tail
            move = self.follow_tail()
        if move == "":
            # if the food is not visable to the snake's head, randomly move to a safe position until the snake's head see
            # the food
            move = self.randomly_move()
        return move

    # sees if the virtual move is valid
    def virtual_explore(self):
        self.tempb[self.temps[-1]] = 0
        self.tempb[self.food] = 2 * (self.width + 1) * (self.height + 1)
        result = self.can_get_food(self.temps[-1], self.temps, self.tempb)

        for i in ["N", "S", "W", "E"]:
            if self.is_safe(self.temps[0], i) and self.test_move(self.temps[0], i) == self.temps[-1] \
                    and len(self.temps) > 3:
                result = False
        return result
    # follows its tail
    def follow_tail(self):
        self.temps = deepcopy(self.snake)
        self.reset_board(self.temps, len(self.temps), self.tempb)
        self.tempb[self.temps[-1]] = 0
        self.tempb[self.food] = 2 * (self.width + 1) * (self.height + 1)
        self.can_get_food(self.temps[-1], self.temps, self.tempb)
        self.tempb[self.temps[-1]] = 2 * (self.width + 1) * (self.height + 1)

        return self.longest_move(self.temps, self.tempb)

    # if the food is not visable to the snake's head, randomly move to a safe position until the snake's head see
            # the food
    def randomly_move(self):
        move = ""
        self.reset_board(self.snake, len(self.snake), self.board)
        self.can_get_food(self.food, self.snake, self.board)
        min = 2 * (self.width + 1) * (self.height + 1)

        for i in ["N", "S", "W", "E"]:
            if self.is_safe(self.snake[0], i) and self.board[self.test_move(self.snake[0], i)] < min:

                min = self.board[self.test_move(self.snake[0], i)]
                move = i
        return move
    # needs to reset the board to go back to the state before virtual move
    def reset_board(self, snake, size, board):
        for i in range(self.width):
            for j in range(self.height):
                temp = (i, j)
                if temp == self.food:
                    board[temp] = 0
                elif temp not in snake[:size]:
                    board[temp] = (self.width + 1) * (self.height + 1)
                else:
                    board[temp] = 2 * (self.width + 1) * (self.height + 1)
    # has another virtual snake to run to see if it will survive after eating the apple
    def virtual_move(self):
        self.temps = deepcopy(self.snake)
        self.tempb = deepcopy(self.board)
        self.reset_board(self.temps, len(self.temps), self.tempb)

        food_eaten = False
        while food_eaten is not True:
            self.can_get_food(self.food, self.temps, self.tempb)
            move = self.shortest_move(self.temps, self.tempb)
            temphead = self.test_move(self.temps[0], move)
            self.temps.insert(0, temphead)
            self.tempb[temphead] = 2 * (self.width + 1) * (self.height + 1)
            if temphead == self.food:
                self.reset_board(self.temps, len(self.temps), self.tempb)
                food_eaten = True
            else:
                #tail = self.temps.pop()
                self.tempb[self.temps[-1]] = (self.width + 1) * (self.height + 1)

    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(t2coord(self.food, self.bsize), width=0, fill="red")
        for i in range(self.size):
            self.canvas.create_rectangle(t2coord(self.snake[i], self.bsize), width=0, fill="yellow")
    # paints the snake and food
    def paint_ai(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(t2coord(self.food, self.bsize), width=0, fill="red")
        for i in range(self.size):
            self.canvas.create_rectangle(t2coord(self.snake[i], self.bsize), width=0, fill="yellow")
        self.canvas.create_rectangle(t2coord(self.nexthead, self.bsize), width=0, fill="RoyalBlue2")
    # sees if it is valid to move
    def turn(self, direct):
        bol = True
        if self.di == "E" and direct == "W": bol = False
        if self.di == "W" and direct == "E": bol = False
        if self.di == "N" and direct == "S": bol = False
        if self.di == "S" and direct == "N": bol = False
        if bol:
            self.di = direct
    # randomly generate a food
    def create_food(self):
        self.food = (randrange(self.width), randrange(self.height))
        while self.food in self.snake and len(self.snake) != self.width * self.height:
            self.food = (randrange(self.width), randrange(self.height))

    def is_safe(self, first, move):
        can_move = False
        #can_move = True if first not in self.snake else False
        if move == "W":
            can_move = True if first[0] > 0 else False
        elif move == "E":
            can_move = True if first[0] < self.width-1 else False
        elif move == "N":
            can_move = True if first[1] > 0 else False
        elif move == "S":
            can_move = True if first[1] < self.height-1 else False

        return can_move
    # runs the BFS to search through the entire board and calculates the distances from every grid to the food
    def can_get_food(self, pfood, snake, board):
        OPEN = []
        OPEN.append(pfood)
        discovered = {(i, j): 0 for i in range(self.width) for j in range(self.height)}
        found = False

        while len(OPEN) != 0:
            first = OPEN.pop(0)
            if discovered[first] != 0: continue
            discovered[first] = 1
            for i in ["N", "S", "W", "E"]:
                if self.is_safe(first, i):
                    cur = self.test_move(first, i)
                    if cur == snake[0]:
                        found = True
                    if cur not in snake:
                        #calculates the distances from every grid to the food
                        if board[cur] > board[first] + 1:
                            board[cur] = board[first] + 1
                        if discovered[cur] == 0:
                            OPEN.append(cur)
        return found
    # finds the shorest move from the snake head to the food
    def shortest_move(self, snake, board):
        best_move = ""
        minMove = 2 * (self.width + 1) * (self.height + 1)
        for i in ["N", "S", "W", "E"]:
            if self.is_safe(snake[0], i) and board[self.test_move(snake[0], i)]< minMove:
                minMove = board[self.test_move(snake[0], i)]
                best_move = i
        return best_move
    # finds the longest move from the snake head to the food
    def longest_move(self, snake, board):
        best_move = ""
        maxMove = 0
        for i in ["N", "S", "W", "E"]:
            if self.is_safe(snake[0], i) and board[self.test_move(snake[0], i)] > maxMove and board[self.test_move(snake[0], i)] < (self.width + 1) * (self.height + 1):
                maxMove = board[self.test_move(snake[0], i)]
                best_move = i
        return best_move




def t2coord(tp, bsize):
    return tp[0]*bsize, tp[1]*bsize, (tp[0]+1)*bsize, (tp[1]+1)*bsize


app = SnakeGame()