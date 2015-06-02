from tkinter import *
from random import *
import time

width = 100
height = 100
boxsize = 5
speed = 100

class SnakeGame:
    def __init__(self):
        self.master = Tk()
        self.RUN = False
        # Control Center
        inputs = Frame(self.master)
        label_hei = Label(inputs, text="Height")
        label_wid = Label(inputs, text="Width")
        self.entry_wid = Entry(inputs)
        self.entry_hei = Entry(inputs)
        self.entry_wid.insert(0, "100")
        self.entry_hei.insert(0, "100")
        label_wid.grid(row=0, column=0)
        self.entry_wid.grid(row=0, column=1)
        label_hei.grid(row=0, column=2)
        self.entry_hei.grid(row=0, column=3)
        # --------------Game Board-------------------
        self.gameFrame = Frame(self.master)
        self.board = Canvas(self.gameFrame, bg="black", width=width*boxsize, height=height*boxsize)
        self.snake = Snake(self.board)

        inputs.pack(side="top")
        self.gameFrame.pack()
        self.board.pack()
        button = Button(inputs, text="Run", command=self.start)
        button.grid(row=0, column=4)
        self.master.mainloop()

    def start(self):
        global width, height
        neww = eval(self.entry_wid.get())
        newh = eval(self.entry_hei.get())
        assert (newh > 10 and neww > 10)
        # print("Width = " + str(neww) + " and Height = " + str(newh))
        if newh != height or neww != width:
            width = neww
            height = newh
            self.board.delete(ALL)
            self.board.config(width=width*boxsize, height=height*boxsize)
            self.snake = Snake(self.board)
        self.RUN = True
        self.master.bind("<Up>", lambda event: self.snake.turn("n"))
        self.master.bind("<Down>", lambda event: self.snake.turn("s"))
        self.master.bind("<Left>", lambda event: self.snake.turn("w"))
        self.master.bind("<Right>", lambda event: self.snake.turn("e"))
        self.runGame()

    def runGame(self):
        if self.RUN:
            self.RUN = self.snake.move(self.board)
            self.master.after(speed, self.runGame())


class Snake:
    def __init__(self, board):
        self.body = []
        self.length = 4
        self.direction = "e"
        self.head = (width // 2, height // 2)
        # board.create_rectangle(500, 500, 600, 600, width=0, fill="yellow")
        for i in range(self.length):
            self.body.append(board.create_rectangle((self.head[0]-i) * boxsize, self.head[1] * boxsize,
                                           (self.head[0]-i+1) * boxsize, (self.head[1]+1) * boxsize, width=0, fill="yellow"))

    def move(self, board):
        # board.delete(ALL)
        if self.direction == "e" and self.head[0] != width:
            self.head = (self.head[0] + 1, self.head[1])
        elif self.direction == "w" and self.head[0] != 0:
            self.head = (self.head[0] - 1, self.head[1])
        elif self.direction == "n" and self.head[1] != height:
            self.head = (self.head[0], self.head[1] + 1)
        elif self.direction == "s" and self.head[1] != 0:
            self.head = (self.head[0], self.head[1] - 1)
        else:
            return False
        self.body.insert(0, board.create_rectangle(self.head[0] * boxsize, self.head[1] * boxsize,
                                                   (self.head[0]+1) * boxsize, (self.head[1]+1) * boxsize, width=0, fill="yellow"))
        #board.delete(self.body[-1])
        #self.body.pop()
        return True

    def turn(self, direct):
        bol = True
        if self.direction == "e" and direct == "w": bol = False
        if self.direction == "w" and direct == "e": bol = False
        if self.direction == "n" and direct == "s": bol = False
        if self.direction == "s" and direct == "n": bol = False
        if bol:
            self.direction = direct


if __name__ == '__main__':
    app = SnakeGame()