__author__ = 'ziming3'
from tkinter import *
from random import randrange
import time


class SnakeGame:
    def __init__(self):
        self.root = Tk()
        self.Run = False

        self.width = 50
        self.height = 50
        self.bsize = 10
        self.size = 6
        self.speed = 300

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

        self.button = Button(self.frame, text="RUN!", command=self.start)
        self.button.pack() #grid(row=0, column=4)

        self.root.mainloop()

    def start(self):
        self.time = 0
        self.Run = True
        self.points = 0

        self.body = []
        self.chunks = []
        self.di = "E"
        new_w = eval(self.wentry.get())
        new_h = eval(self.hentry.get())
        if new_w != self.width or new_h != self.height:
            self.width = new_w
            self.height = new_h
            self.canvas.config(width=self.width*self.bsize, height=self.height*self.bsize)
        self.head = (self.width // 2, self.height // 2)
        for i in range(self.size):
            self.chunks.append((self.head[0]-i, self.head[1]))
        for i in range(self.size):
            self.body.append(self.canvas.create_rectangle(t2coord(self.chunks[i], self.bsize), width=0, fill="yellow"))

        self.create_food()
        self.canvas.create_rectangle(t2coord(self.food, self.bsize), width=0, fill="green")

        self.root.bind("<Up>", lambda event: self.turn("N"))
        self.root.bind("<Down>", lambda event: self.turn("S"))
        self.root.bind("<Left>", lambda event: self.turn("W"))
        self.root.bind("<Right>", lambda event: self.turn("E"))

        self.game_begin()

    def game_begin(self):
        if self.Run is True:
            self.time += self.speed
            self.move()
            self.paint()
            self.root.after(self.speed, self.game_begin)

    def move(self):
        if self.di == "E" and self.head[0] != self.width:
            self.head = (self.head[0] + 1, self.head[1])
        elif self.di == "W" and self.head[0] != 0:
            self.head = (self.head[0] - 1, self.head[1])
        elif self.di == "N" and self.head[1] != self.height:
            self.head = (self.head[0], self.head[1] - 1)
        elif self.di == "S" and self.head[1] != 0:
            self.head = (self.head[0], self.head[1] + 1)
        else:
            self.end()
            return
        if self.head in self.chunks:
            self.end()
            return
        self.chunks.insert(0, self.head)
        if self.head != self.food:
            self.chunks.pop()
        else:
            self.create_food()
            self.size += 1
            print(self.size)

    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(t2coord(self.food, self.bsize), width=0, fill="green")
        for i in range(self.size):
            self.body.append(self.canvas.create_rectangle(t2coord(self.chunks[i], self.bsize), width=0, fill="yellow"))

    def end(self):
        self.Run = False

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
        while self.food in self.chunks:
            self.food = (randrange(self.width), randrange(self.height))
        #self.canvas.create_rectangle(t2coord(self.food, self.bsize), width=0, fill="green")


def t2coord(tp, bsize):
    return tp[0]*bsize, tp[1]*bsize, (tp[0]+1)*bsize, (tp[1]+1)*bsize

app = SnakeGame()