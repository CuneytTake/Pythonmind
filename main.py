from tkinter import *
import random
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)

        # Set widgets in grid
        self.grid()
        self.create_widgets()

        # set current choice
        self.currentchoice = 1

        # number variable used to skip columns to fill hint cells
        self.blacknumber = 0
        self.whitenumber = 0

        # Set randomly generated code
        self.code = []
        while len(self.code) != 4:
            for x in range(4):
                n = random.randint(1, 6)
                self.code.append(n)
        print(self.code)

        # Indexes the integers in the answer and casts to string
        self.pos1 = str(self.code[0])
        self.pos2 = str(self.code[1])
        self.pos3 = str(self.code[2])
        self.pos4 = str(self.code[3])

        # lists the answer
        self.answer = str(self.pos1) + str(self.pos2) + str(self.pos3) + str(self.pos4)

        # placeholder guess list
        self.guess = []

        # Checklist list
        self.checklist = []
        self.whitecheck = 0
        self.redcheck = 0

        # current row variable
        self.currentrow = 0

    def rules(self):
        popup = Toplevel()
        button = Button(popup, text=contents,
            command=lambda: popup.destroy())
        button.pack()

    def scoreboard(self):
        popup = Toplevel()
        b = Label(popup, text=scoreboard)
        b.pack()

    def getName(self):
        nameGet = self.top = Toplevel()
        self.l = Label(nameGet, text="Congratulations! You've won! Please enter your name so it can be entered into the highscores:")
        self.l.pack()
        self.e = Entry(nameGet)
        self.e.pack()
        self.b = Button(nameGet, text="OK",
                        command=self.cleanup)
        self.b.pack()

    def cleanup(self):
        self.name = self.e.get()
        self.scoreEntry = StringVar()
        self.scoreEntry =  str(self.name) +" "+  str(self.score)
        h.write(self.scoreEntry + "\n")
        self.top.destroy()
        root.destroy()

    def create_widgets(self):
        # Empty cell sprite
        self.emptySprite = PhotoImage(file="Empty.png")

        # colored cell sprites
        self.red = PhotoImage(file="red.png")
        self.blue = PhotoImage(file="blue.png")
        self.green = PhotoImage(file="green.png")
        self.yellow = PhotoImage(file="yellow.png")
        self.gray = PhotoImage(file="gray.png")
        self.violet = PhotoImage(file="violet.png")

        #black and white cell sprites
        self.black = PhotoImage(file="black.png")
        self.white = PhotoImage(file="white.png")

        # Widget dictionary for easy access
        self.widgets = {}

        # Amount of rows and columns variable
        self.row = 8
        self.column = 8

        for i in range(self.row):
            for j in range(self.column):
                b = Label(root, image=self.emptySprite)
                b.grid(row=i, column=j)
                self.widgets[(i, j)] = b

        # Resizes and aligns HintCells
        for o in range(self.column):
            self.widgets[(o, 4)].config(width=30, height=30)
            self.widgets[(o, 4)].grid(sticky=E)
            self.widgets[(o, 5)].config(width=30, height=30)
            self.widgets[(o, 6)].config(width=30, height=30)
            self.widgets[(o, 6)].grid(sticky=W)
            self.widgets[(o, 7)].config(width=30, height=30)
            self.widgets[(o, 7)].grid(sticky=W)

        # sets initial score value
        self.score = 64
        self.name = ""

        # score label
        self.scoreLabel = Label(root, text="Score:  "+str(self.score))
        self.scoreLabel.grid(row=9, column=6, sticky=W)

        # Rules button
        Button(root,
               text="Spelregels",
               command=self.rules
               ).grid(row=8, column=7, sticky= S)

        # Scoreboard button
        Button(root,
               text="Scorebord",
               command=self.scoreboard
               ).grid(row=9, column=7, sticky= N)

        # Colored Cells buttons

        RedCell = Button(root, image=self.red, border=1, command=self.RedCell)
        RedCell.grid(row=i+2, column=0)

        BlueCell = Button(root,image=self.blue, border=1, command = self.BlueCell)
        BlueCell.grid(row=i+2, column=1)

        GreenCell = Button(root, image=self.green, border=1, command = self.GreenCell)
        GreenCell.grid(row=i+2, column=2)

        YellowCell = Button(root, image=self.yellow, border=1, command = self.YellowCell)
        YellowCell.grid(row=i+2, column=3)

        GrayCell = Button(root, image=self.gray, border=1, command = self.GrayCell)
        GrayCell.grid(row=i+2, column=4)

        VioletCell = Button(root, image=self.violet, border=1, command = self.VioletCell)
        VioletCell.grid(row=i+2, column=5)

    def RedCell(self):

        global choice
        choice = 1

        if self.currentchoice == 1:
            self.widgets[(self.row-1-self.currentrow,0)].config(image=self.red)
            self.currentchoice = 2
            self.guess.append(choice)

        elif self.currentchoice == 2:
            self.widgets[(self.row-1-self.currentrow,1)].config(image=self.red)
            self.currentchoice = 3
            self.guess.append(choice)

        elif self.currentchoice == 3:
            self.widgets[(self.row-1-self.currentrow,2)].config(image=self.red)
            self.currentchoice = 4
            self.guess.append(choice)

        elif self.currentchoice == 4:
            self.widgets[(self.row-1-self.currentrow,3)].config(image=self.red)
            self.guess.append(choice)

            self.checkcode()

    def BlueCell(self):
        global choice
        choice = 2
        if self.currentchoice == 1:
            self.widgets[(self.row-1-self.currentrow, 0)].config(image=self.blue)
            self.currentchoice = 2
            self.guess.append(choice)

        elif self.currentchoice == 2:
            self.widgets[(self.row-1-self.currentrow, 1)].config(image=self.blue)
            self.currentchoice = 3
            self.guess.append(choice)

        elif self.currentchoice == 3:
            self.widgets[(self.row-1-self.currentrow, 2)].config(image=self.blue)
            self.currentchoice = 4
            self.guess.append(choice)

        elif self.currentchoice == 4:
            self.widgets[(self.row-1-self.currentrow, 3)].config(image=self.blue)
            self.guess.append(choice)

            self.checkcode()

    def GreenCell(self):
        global choice
        choice = 3
        if self.currentchoice == 1:
            self.widgets[(self.row-1-self.currentrow, 0)].config(image=self.green)
            self.currentchoice = 2
            self.guess.append(choice)

        elif self.currentchoice == 2:
            self.widgets[(self.row-1-self.currentrow, 1)].config(image=self.green)
            self.currentchoice = 3
            self.guess.append(choice)

        elif self.currentchoice == 3:
            self.widgets[(self.row-1-self.currentrow, 2)].config(image=self.green)
            self.currentchoice = 4
            self.guess.append(choice)
        elif self.currentchoice == 4:
            self.widgets[(self.row-1-self.currentrow, 3)].config(image=self.green)
            self.guess.append(choice)

            self.checkcode()

    def YellowCell(self):
        global choice
        choice = 4
        if self.currentchoice == 1:
            self.widgets[(self.row-1-self.currentrow, 0)].config(image=self.yellow)
            self.currentchoice = 2
            self.guess.append(choice)

        elif self.currentchoice == 2:
            self.widgets[(self.row-1-self.currentrow, 1)].config(image=self.yellow)
            self.currentchoice = 3
            self.guess.append(choice)

        elif self.currentchoice == 3:
            self.widgets[(self.row-1-self.currentrow, 2)].config(image=self.yellow)
            self.currentchoice = 4
            self.guess.append(choice)
        elif self.currentchoice == 4:
            self.widgets[(self.row-1-self.currentrow, 3)].config(image=self.yellow)
            self.guess.append(choice)

            self.checkcode()

    def GrayCell(self):
        global choice
        choice = 5
        if self.currentchoice == 1:
            self.widgets[(self.row-1-self.currentrow, 0)].config(image=self.gray)
            self.currentchoice = 2
            self.guess.append(choice)

        elif self.currentchoice == 2:
            self.widgets[(self.row-1-self.currentrow, 1)].config(image=self.gray)
            self.currentchoice = 3
            self.guess.append(choice)

        elif self.currentchoice == 3:
            self.widgets[(self.row-1-self.currentrow, 2)].config(image=self.gray)
            self.currentchoice = 4
            self.guess.append(choice)
        elif self.currentchoice == 4:
            self.widgets[(self.row-1-self.currentrow, 3)].config(image=self.gray)
            self.guess.append(choice)

            self.checkcode()

    def VioletCell(self):
        global choice
        choice = 6
        if self.currentchoice == 1:
            self.widgets[(self.row-1-self.currentrow, 0)].config(image=self.violet)
            self.currentchoice = 2
            self.guess.append(choice)
        elif self.currentchoice == 2:
            self.widgets[(self.row-1-self.currentrow, 1)].config(image=self.violet)
            self.currentchoice = 3
            self.guess.append(choice)
        elif self.currentchoice == 3:
            self.widgets[(self.row-1-self.currentrow, 2)].config(image=self.violet)
            self.currentchoice = 4
            self.guess.append(choice)
        elif self.currentchoice == 4:
            self.widgets[(self.row-1-self.currentrow, 3)].config(image=self.violet)
            self.guess.append(choice)

            self.checkcode()

    def checkcode(self):

        # position guess variables
        self.positionguess1 = str(self.guess[0])
        self.positionguess2 = str(self.guess[1])
        self.positionguess3 = str(self.guess[2])
        self.positionguess4 = str(self.guess[3])

        if self.code == self.guess:
            self.widgets[(self.row - 1 - self.currentrow, 4)].config(image=self.black)
            self.widgets[(self.row - 1 - self.currentrow, 5)].config(image=self.black)
            self.widgets[(self.row - 1 - self.currentrow, 6)].config(image=self.black)
            self.widgets[(self.row - 1 - self.currentrow, 7)].config(image=self.black)

            """ CONGRATULATE + SHOW SCORE """

            self.getName()
        else:

            #Empties list in case of wrong answer
            self.guess = []

            # Redchecks
            if self.positionguess1 == self.pos1:
                self.redcheck += 1
                self.checklist.append(self.positionguess1)

            if self.positionguess2 == self.pos2:
                self.redcheck += 1
                self.checklist.append(self.positionguess2)

            if self.positionguess3 == self.pos3:
                self.redcheck += 1
                self.checklist.append(self.positionguess3)

            if self.positionguess4 == self.pos4:
                self.checklist.append(self.positionguess4)
                self.redcheck += 1

            # Whitechecks
            if self.positionguess1 != self.pos1 and self.positionguess1 in self.answer and self.positionguess1 not in self.checklist:
                self.checklist.append(self.positionguess1)
                self.whitecheck += 1

            if self.positionguess2 != self.pos2 and self.positionguess2 in self.answer and self.positionguess2 not in self.checklist:
                self.checklist.append(self.positionguess2)
                self.whitecheck += 1

            if self.positionguess3 != self.pos3 and self.positionguess3 in self.answer and self.positionguess3 not in self.checklist:
                self.checklist.append(self.positionguess3)
                self.whitecheck += 1

            if self.positionguess4 != self.pos4 and self.positionguess4 in self.answer and self.positionguess4 not in self.checklist:
                self.checklist.append(self.positionguess4)
                self.whitecheck += 1

            for x in range(self.redcheck):
                self.widgets[(self.row - 1 - self.currentrow, self.blacknumber+4)].config(image=self.black)
                self.blacknumber += 1

            self.whitenumber += self.blacknumber


            for x in range(self.whitecheck):
                self.widgets[(self.row - 1 - self.currentrow, self.whitenumber+4)].config(image=self.white)
                self.whitenumber += 1

            # Resets currentchoice in case of wrong answer
            self.currentchoice = 1

            # Updates current row in case of wrong answer
            self.currentrow += 1

            self.score -= 8
            self.scoreLabel.config(text="Score:    " + str(self.score))

            # RESET
            self.redcheck = 0
            self.whitecheck = 0
            self.whitenumber = 0
            self.blacknumber = 0
            self.checklist = []

            if self.currentrow >=8:
                messagebox.showinfo("Too bad!!!", "You lost! Better luck next time.")
                root.destroy()
                root.mainloop()


root = Tk()
root.title("Pythonmind")
root.geometry("")
root.resizable(width=False, height=False)
app = Application(root)
f= open("Rules.txt","r")
if f.mode == "r":
    contents=f.read()

h = open("highscores.txt", "r+")
if h.mode == "r+":
    scoreboard = h.read()


col_count, row_count = root.grid_size()

for col in range(col_count):
    root.grid_columnconfigure(col, minsize=50)

for row in range(row_count):
    root.grid_rowconfigure(row, minsize=50)


def start():
    root.mainloop()


start()


