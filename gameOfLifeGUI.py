from tkinter import *
from copy import deepcopy

ROWS = 20
COLS = 20
SIZE = 500


class MyButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs,
                        command=lambda: self.click())
        self.alive = False
        self['bg'] = 'white'

    def click(self):
        if self.alive:
            self.setDead()
        else:
            self.setAlive()

    def setAlive(self):
        self.alive = True
        self['bg'] = 'black'

    def setDead(self):
        self.alive = False
        self['bg'] = 'white'


class Window(Frame):

    def __init__(self, master=None):
        self.board = {}
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        for i in range(ROWS):
            self.board[i] = []
            for j in range(COLS):
                exitButton = MyButton(self,
                                      image=white, height=SIZE // ROWS, width=SIZE // COLS)
                self.board[i].append(exitButton)
                exitButton.place(x=i * (SIZE / ROWS),
                                 y=j * (SIZE / COLS) + 30)

        runButton = Button(self, text="Run", command=lambda: self.update())
        runButton.place(x=0, y=0)

    def onBoard(self, i, j):
        return i >= 0 and i < ROWS and j >= 0 and j < COLS

    def update(self):
        prevDay = []
        for i in range(len(self.board)):
            prevDay.append([])
            for j in range(len(self.board[i])):
                prevDay[i].append(self.board[i][j].alive)

        for i in range(ROWS):
            for j in range(COLS):
                count = 0
                count += (self.onBoard(i-1, j-1)
                          and prevDay[i-1][j-1])    # i-1, j-1

                count += (self.onBoard(i-1, j)
                          and prevDay[i-1][j])      # i-1, j

                count += (self.onBoard(i-1, j+1)
                          and prevDay[i-1][j+1])    # i-1, j+1

                count += (self.onBoard(i, j+1) and prevDay[i][j+1])   # i, j+1

                count += (self.onBoard(i+1, j+1)
                          and prevDay[i+1][j+1])   # i+1, j+1

                count += (self.onBoard(i+1, j) and prevDay[i+1][j])   # i+1, j

                count += (self.onBoard(i+1, j-1)
                          and prevDay[i+1][j-1])   # i+1, j-1

                count += (self.onBoard(i, j-1) and prevDay[i][j-1])   # i, j-1

                if count == 3 or (count == 2 and self.board[i][j].alive):
                    self.board[i][j].setAlive()
                else:
                    self.board[i][j].setDead()


root = Tk()
white = PhotoImage("white.jpg")
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("{}x{}".format(SIZE, SIZE + 30))
root.mainloop()
