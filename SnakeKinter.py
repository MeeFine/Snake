__author__ = 'ziming3'
from tkinter import *
from random import *
import time

width = 100
height = 100

class snakeGame:
    def __init__(self):
        master = Tk()
        self.RUN = False
        # Control Center
        inputs = Frame(master)
        label_wid = Label(inputs, text="Width")
        label_hei = Label(inputs, text="Height")
        self.entry_wid = Entry(inputs)
        self.entry_hei = Entry(inputs)
        self.entry_wid.insert(0, "100")
        self.entry_hei.insert(0, "100")
        label_hei.grid(row=0, column=0)
        self.entry_hei.grid(row=0, column=1)
        label_wid.grid(row=0, column=2)
        self.entry_wid.grid(row=0, column=3)
        #--------------Game Board-------------------
        self.gameFrame = Frame(master)
        self.gameFrame.pack()
        self.board = Canvas(self.gameFrame, bg="black", width=width, height=height)
        self.board.pack()
        button = Button(inputs, text="Run", command=self.start)
        button.grid(row=0, column=4)

        self.board = Canvas(master, width=width, height=height)
        inputs.pack(side="top")
        master.mainloop()

    def start(self):
        global width, height
        neww = eval(self.entry_wid.get())
        newh = eval(self.entry_hei.get())
        if newh != height and neww != width:
            width = neww
            height = newh
            self.board.config(width=width, height=height)
        self.RUN = True
        self.snake = snake()
        runGame()

    def runGame(self):
        self.gameFrame.bind("<Up>", lambda: self.snake.direction="w")
        self.gameFrame.bind("<Up>", lambda: self.snake.direction="w")
        self.gameFrame.bind("<Up>", lambda: self.snake.direction="w")
        self.gameFrame.bind("<Up>", lambda: self.snake.direction="w")
        while self.RUN:



class snake:
    def __init__(self):
        self.body = []
        self.length = 4
        self.head = (width // 2, height // 2)
        self.tail = (width // 2 - self.length - 1, height)
        self.direction = "e"
        for i in range(self.length):
            self.body.append((width // 2 - i, height // 2))

    def move(self):
        assert (self.direction in "nwes")
        headx = self.head[0]
        heady = self.head[1]
        if self.direction == "e" and headx != width:
            self.head = (headx + 1, heady)
        elif self.direction == "w" and headx != 0:
            self.head = (headx - 1, heady)
        elif self.direction == "n" and heady != height:
            self.head = (headx, heady + 1)
        elif self.direction == "s" and heady != 0:
            self.head = (headx, heady - 1)
        else:
            return False
        self.body.insert(0, self.head)
        self.body.pop()
        return True

if __name__ == '__main__':
    app = snakeGame()