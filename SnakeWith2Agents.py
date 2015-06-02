__author__ = 'ziming3'
from tkinter import *
from random import randrange, choice
import time


class SnakeGame:
    def __init__(self):
        self.root = Tk()
        self.Run = False

        self.width = 50
        self.height = 50
        self.bsize = 10
        self.size = 6
        self.speed = 100

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
        self.button.pack() #grid(row=0, column=4)

        self.root.mainloop()

    def start(self):
        self.time = 0
        self.Run1 = True
        self.Run2 = True

        self.body1 = []
        self.body2 = []
        self.chunks1 = []
        self.chunks2 = []
        self.di1 = choice(["E", "N", "W", "S"])
        self.di2 = choice(["E", "N", "W", "S"])

        self.points1 = 0
        self.points2 = 0

        new_w = eval(self.wentry.get())
        new_h = eval(self.hentry.get())
        if new_w != self.width or new_h != self.height:
            self.width = new_w
            self.height = new_h
            self.canvas.config(width=self.width*self.bsize, height=self.height*self.bsize)
        self.head1 = (randrange(self.width), randrange(self.height))
        for i in range(self.size):
            self.chunks1.append((self.head1[0]-i, self.head1[1]))
        for i in range(self.size):
            self.body1.append(self.canvas.create_rectangle(t2coord(self.chunks1[i], self.bsize), width=0, fill="yellow"))

        self.head2 = (randrange(self.width), randrange(self.height))
        while self.head2 in self.chunks1 or self.radius(self.chunks1, self.head2):
            self.head2 = (randrange(self.width), randrange(self.height))
        for i in range(self.size):
            self.chunks2.append((self.head1[0]-i, self.head1[1]))
        for i in range(self.size):
            self.body2.append(self.canvas.create_rectangle(t2coord(self.chunks2[i], self.bsize), width=0, fill="blue"))

        self.foods = []
        self.create_foods(3)
        for i in self.foods:
            self.canvas.create_rectangle(t2coord(i, self.bsize), width=0, fill="green")

        self.root.bind("<Up>", lambda event: self.turn1("N"))
        self.root.bind("<Down>", lambda event: self.turn1("S"))
        self.root.bind("<Left>", lambda event: self.turn1("W"))
        self.root.bind("<Right>", lambda event: self.turn1("E"))

        self.root.bind("w", lambda event: self.turn2("N"))
        self.root.bind("s", lambda event: self.turn2("S"))
        self.root.bind("a", lambda event: self.turn2("W"))
        self.root.bind("d", lambda event: self.turn2("E"))

        self.game_begin()

    def radius(self, snake1, head2):
        for i in snake1:
            if (head2[0] - i[0]) ** 2 + (head2[1] - i[1]) ** 2 < 50:
                return False
        return True

    def game_begin(self):
        if self.Run1 is True or self.Run2 is True:
            self.time += self.speed
            self.move()
            if self.Run is True:
                self.paint()
            self.root.after(self.speed, self.game_begin)
        else:
            self.canvas.create_text(self.width // 2 * self.bsize, self.height // 2 * self.bsize, fill="red", font=("Helvetica", 30), text="Game Over")

    def move(self):
        if self.di1 == "E" and self.head1[0] != self.width:
            self.head1 = (self.head1[0] + 1, self.head1[1])
        elif self.di1 == "W" and self.head1[0] != 0:
            self.head1 = (self.head1[0] - 1, self.head1[1])
        elif self.di1 == "N" and self.head1[1] != self.height:
            self.head1 = (self.head1[0], self.head1[1] - 1)
        elif self.di1 == "S" and self.head1[1] != 0:
            self.head1 = (self.head1[0], self.head1[1] + 1)
        else:
            self.points1 = 0
            return
        if self.head1 in self.chunks1 or self.head1 in self.chunks2:
            self.points1 = 0
        self.chunks1.insert(0, self.head1)
        if self.head1 != self.foods:
            self.chunks1.pop()
        else:
            self.create_foods(1)
            self.size += 1
            self.points1 += 10

        if self.di2 == "E" and self.head2[0] != self.width:
            self.head2 = (self.head2[0] + 1, self.head2[1])
        elif self.di2 == "W" and self.head2[0] != 0:
            self.head2 = (self.head2[0] - 1, self.head2[1])
        elif self.di2 == "N" and self.head2[1] != self.height:
            self.head2 = (self.head2[0], self.head2[1] - 1)
        elif self.di2 == "S" and self.head2[1] != 0:
            self.head2 = (self.head2[0], self.head2[1] + 1)
        else:
            self.points2 = 0
        if self.head2 in self.chunks1 or self.head2 in self.chunks2:
            self.points2 = 0
        self.chunks1.insert(0, self.head2)
        if self.head2 != self.foods:
            self.chunks1.pop()
        else:
            self.create_foods(1)
            self.size += 1
            self.points2 += 10

    def paint(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(t2coord(self.foods, self.bsize), width=0, fill="green")
        for i in range(self.size):
            self.body1.append(self.canvas.create_rectangle(t2coord(self.chunks1[i], self.bsize), width=0, fill="yellow"))
            s

    def end(self):
        self.Run = False

    def turn1(self, direct):
        bol = True
        if self.di1 == "E" and direct == "W": bol = False
        if self.di1 == "W" and direct == "E": bol = False
        if self.di1 == "N" and direct == "S": bol = False
        if self.di1 == "S" and direct == "N": bol = False
        if bol:
            self.di1 = direct

    def turn2(self, direct):
        bol = True
        if self.di2 == "E" and direct == "W": bol = False
        if self.di2 == "W" and direct == "E": bol = False
        if self.di2 == "N" and direct == "S": bol = False
        if self.di2 == "S" and direct == "N": bol = False
        if bol:
            self.di2 = direct

    def create_foods(self, number):
        for i in range(number):
            temp = (randrange(self.width), randrange(self.height))
            while temp in self.chunks1 and temp in self.chunks2 and temp in self.foods:
                temp = (randrange(self.width), randrange(self.height))
            self.foods.append(temp)


def t2coord(tp, bsize):
    return tp[0]*bsize, tp[1]*bsize, (tp[0]+1)*bsize, (tp[1]+1)*bsize

app = SnakeGame()