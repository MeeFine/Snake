__author__ = 'ziming3'
from tkinter import *
from random import randrange
import time


class SnakeGame:
    def __init__(self):
        self.root = Tk()
        self.Run = False
        self.refresh = 0

        self.width = 50
        self.height = 50
        self.bsize = 10

        self.frame = Frame()
        self.frame.pack()

        self.canvas = Canvas(self.frame, bg="black", width=self.width*self.bsize, height=self.height*self.bsize)
        self.canvas.pack()

        self.wlabel = Label(self.frame, fg="black", text="Width")
        self.wlabel.pack(side="left")
        self.wentry = Entry(self.frame)
        self.wentry.pack(side="left")
        self.wentry.insert(0, "50")
        self.hlabel = Label(self.frame, fg="black", text="Height")
        self.hlabel.pack(side="left")
        self.hentry = Entry(self.frame)
        self.hentry.pack(side="left")
        self.hentry.insert(0, "50")

        self.button = Button(self.frame, text="Run / Restart", command=self.start)
        self.button.pack()

        self.root.mainloop()

    def start(self):
        self.refresh += 1
        self.Run = True
        # self.points = 0
        self.speed = 100
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

        self.root.bind("<Up>", lambda event: self.turn("N"))
        self.root.bind("<Down>", lambda event: self.turn("S"))
        self.root.bind("<Left>", lambda event: self.turn("W"))
        self.root.bind("<Right>", lambda event: self.turn("E"))

        # self.refresh = False
        self.game_begin(self.refresh)

    def game_begin(self, currentLoop):
        if self.refresh > currentLoop:
            return
        if self.Run is True:
            '''self.Run = self.move()
            if self.Run is True:
                self.paint()'''
            temphead = self.test_move(self.snake[0], self.di)
            if temphead in self.snake:
                print("Entered")
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
            self.canvas.create_text(self.width // 2 * self.bsize, self.height // 2 * self.bsize, fill="red", font=("Helvetica", 30), text="Game Over")

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
        if direct == "E" and head[0] != self.width:
            head = (head[0] + 1, head[1])
        elif direct == "W" and head[0] != 0:
            head = (head[0] - 1, head[1])
        elif direct == "N" and head[1] != 0:
            head = (head[0], head[1] - 1)
        elif direct == "S" and head[1] != self.height:
            head = (head[0], head[1] + 1)
        return head

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


def t2coord(tp, bsize):
    return tp[0]*bsize, tp[1]*bsize, (tp[0]+1)*bsize, (tp[1]+1)*bsize

app = SnakeGame()