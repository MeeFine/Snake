__author__ = 'ziming3'
from tkinter import *
from random import randrange
import time
from copy import deepcopy


class SnakeGame:
    def __init__(self):
        self.root = Tk()
        self.Run = False
        self.refresh = 0

        self.width = 10
        self.height = 10
        self.bsize = 10

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

        self.button = Button(self.frame, text="Run / Restart", command=self.start)
        self.button.pack()

        self.root.mainloop()

    def start(self):
        self.refresh += 1
        self.Run = True
        # self.points = 0
        self.speed = 10
        self.size = 6
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

        '''self.root.bind("<Up>", lambda event: self.turn("N"))
        self.root.bind("<Down>", lambda event: self.turn("S"))
        self.root.bind("<Left>", lambda event: self.turn("W"))
        self.root.bind("<Right>", lambda event: self.turn("E"))'''

        # self.refresh = False
        self.game_begin(self.refresh)

    def game_begin(self, currentLoop):
        if self.refresh > currentLoop:
            return
        if self.Run is True:
            '''self.Run = self.move()
            if self.Run is True:
                self.paint()'''
            newmove = self.find_move()
            if newmove != "":
                self.di = newmove
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
            self.root.after(self.speed, lambda cur=currentLoop: self.game_begin(cur))
        else:
            self.canvas.create_text(self.width // 2 * self.bsize, self.height // 2 * self.bsize, fill="red", font=("Helvetica", self.width // 2), text="Game Over")

    '''def move(self, direct, snake):
        head = snake[0]
        if direct == "E" and head[0] != self.width:
            head = (head[0] + 1, self.head[1])
        elif direct == "W" and self.head[0] != 0:
            head = (head[0] - 1, self.head[1])
        elif direct == "N" and self.head[1] != 0:
            head = (head[0], self.head[1] - 1)
        elif direct == "S" and self.head[1] != self.height:
            head = (head[0], self.head[1] + 1)
        else:
            return False
        if head in snake:
            return False
        snake.insert(0, head)
        if head != self.food:
            snake.pop()
        else:
            self.create_food()
            self.tempsize += 1'''

    def test_move(self, head, direct):
        if direct == "E" and head[0] < self.width-1:
            head = (head[0] + 1, head[1])
        elif direct == "W" and head[0] > 0:
            head = (head[0] - 1, head[1])
        elif direct == "N" and head[1] > 0:
            head = (head[0], head[1] - 1)
        elif direct == "S" and head[1] < self.height-1:
            head = (head[0], head[1] + 1)
        return head

    def find_move(self):
        self.board = {(i, j): (self.width + 1) * (self.height + 1) for i in range(self.width) for j in range(self.height)}
        self.board_reset(self.snake, self.board)
        if self.can_get_food(self.snake, self.board):
            self.virtual_move()
            if self.is_tail_inside():
                move = self.shortest_move(self.snake, self.board)
            else:
                move = self.follow_tail()
        else:
            move = self.follow_tail()
        if move == "":
            move = self.any_possible_move()
        return move

    def is_tail_inside(self):
        self.tempb[self.temps[-1]] = 0
        self.tempb[self.food] = 2 * (self.width + 1) * (self.height + 1)
        result = self.can_get_food(self.temps, self.tempb)
        for i in ["N", "S", "W", "E"]:
            if self.is_safe(self.temps[0], i) and self.test_move(self.temps[0], i) == self.temps[-1] \
                    and len(self.temps) > 3:
                result = False
        return result

    def follow_tail(self):
        self.temps = deepcopy(self.snake)
        self.board_reset(self.temps, self.tempb)
        self.tempb[self.temps[-1]] = 0
        self.tempb[self.food] = 2 * (self.width + 1) * (self.height + 1)
        self.can_get_food(self.temps, self.tempb)
        self.tempb[self.temps[-1]] = 2 * (self.width + 1) * (self.height + 1)

        return self.longest_move(self.temps, self.tempb)

    def any_possible_move(self):
        move = ""
        self.board_reset(self.snake, self.board)
        self.can_get_food(self.snake, self.board)
        min = 2 * (self.width + 1) * (self.height + 1)

        for i in ["N", "S", "W", "E"]:
            if self.is_safe(self.temps[0], i) and self.board[self.test_move(self.temps[0], i)] < min:
                min = self.board[self.test_move(self.temps[0], i)]
                move = i
        return move

    def board_reset(self, snake, board):
        for i in range(self.width):
            for j in range(self.height):
                temp = (i, j)
                if self.food == temp:
                    board[temp] = 0
                elif temp not in snake:
                    board[temp] = (self.width + 1) * (self.height + 1)
                else:
                    board[temp] = 2 * (self.width + 1) * (self.height + 1)

    def virtual_move(self):
        self.temps = deepcopy(self.snake)
        self.tempb = deepcopy(self.board)
        self.board_reset(self.temps, self.tempb)

        food_eaten = False
        while not food_eaten:
            self.can_get_food(self.temps, self.tempb)
            move = self.shortest_move(self.temps, self.tempb)
            temphead = self.test_move(self.temps[0], move)
            self.temps.insert(0, temphead)
            if temphead == self.food:
                self.board_reset(self.temps, self.tempb)
                self.tempb[self.food] = 2 * (self.width + 1) * (self.height + 1)
                food_eaten = True
            else:
                tail = self.temps.pop()
                self.tempb[tail] = (self.width + 1) * (self.height + 1)
                self.tempb[temphead] = 2 * (self.width + 1) * (self.height + 1)

    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(t2coord(self.food, self.bsize), width=0, fill="green")
        for i in range(self.size):
            self.canvas.create_rectangle(t2coord(self.snake[i], self.bsize), width=0, fill="yellow")

    def turn(self, direct):
        bol = True
        if self.di == "E" and direct == "W": bol = False
        if self.di == "W" and direct == "E": bol = False
        if self.di == "N" and direct == "S": bol = False
        if self.di == "S" and direct == "N": bol = False
        if bol:
            self.di = direct

    def create_food(self):
        self.food = (randrange(self.width), randrange(self.height))
        while self.food in self.snake:
            self.food = (randrange(self.width), randrange(self.height))

    def is_safe(self, first, move):
        can_move = False
        if move == "W":
            can_move = True if first[0] > 0 else False
        elif move == "E":
            can_move = True if first[0] < self.width-1 else False
        elif move == "N":
            can_move = True if first[1] > 0 else False
        elif move == "S":
            can_move = True if first[1] < self.height-1 else False
        return can_move

    def can_get_food(self, snake, board):
        OPEN = []
        OPEN.append(self.food)
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
                    if cur not in self.snake:
                        if board[cur] > board[first] + 1:
                            board[cur] = board[first] + 1
                        if discovered[cur] == 0:
                            OPEN.append(cur)
        return found

    def shortest_move(self, snake, board):
        best_move = self.di
        minMove = 2 * (self.width + 1) * (self.height + 1)
        for i in ["N", "S", "W", "E"]:
            if self.is_safe(snake[0], i) and board[self.test_move(snake[0], i)]< minMove:
                minMove = board[self.test_move(snake[0], i)]
                best_move = i
        return best_move

    def longest_move(self, snake, board):
        best_move = self.di
        maxMove = 2 * (self.width + 1) * (self.height + 1)
        for i in ["N", "S", "W", "E"]:
            if self.is_safe(snake[0], i) and board[self.test_move(snake[0], i)] > maxMove:
                maxMove = board[self.test_move(snake[0], i)]
                best_move = i
        return best_move

def t2coord(tp, bsize):
    return tp[0]*bsize, tp[1]*bsize, (tp[0]+1)*bsize, (tp[1]+1)*bsize

app = SnakeGame()