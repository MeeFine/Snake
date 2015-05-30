__author__ = 'ziming3'
from tkinter import *
from random import *
import time

width = 0
height = 0


class snakeGame:
    def __init__(self, master):
        inputs = Frame(master)
        label_wid = Label(inputs, text="Width")
        label_hei = Label(inputs, text="Height")
        entry_wid = Entry(inputs)
        entry_hei = Entry(inputs)
        entry_wid.insert(0, "100")
        entry_hei.insert(0, "100")
        label_hei.grid(row=0, column=0)
        entry_hei.grid(row=0, column=1)
        label_wid.grid(row=0, column=2)
        entry_wid.grid(row=0, column=3)
        wi = eval(entry_wid.get())
        hi = eval(entry_hei.get())
        button = Button(inputs, text="Run", command=lambda : self.getInput(wi, hi))
        button.grid(row=0, column=4)

        self.board = Canvas(master, width=width, height=height)
        inputs.pack(side="top")

    def getInput(wi, hi):
        global width, height
        width = wi
        height = hi


if __name__ == '__main__':
    root = Tk()
    app = snakeGame(root)

    root.mainloop()