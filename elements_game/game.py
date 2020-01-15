from tkinter import *
from tkinter import messagebox

#Global Vars
menu = ""

#Game Functions
def startgame():
    menu.destroy()
    game = Tk()
    game.title("Elements game")
    game.geometry("800x500")
    alabel = Label(text="Find the Symbol of:", font=("Helvetica", 70)) 
    alabel.place(x=400, y=100, anchor="center")
    atomicno = Label(text="118", font=("Helvetica", 200)) 
    atomicno.place(x=400, y=250, anchor="center")
    noentry = Entry(text="Atomic number",font=('Verdana',25))
    noentry.place(x=350, y=400, anchor="center")
    submit = Button(game, text='Submit', font=('Verdana',25))
    submit.place(x=570, y=400, anchor="center")
    stop = Button(game, text='Stop Game', font=('Verdana',25))
    stop.place(x=200, y=450, anchor="center")
    generateno = Button(game, text='Generate New no', font=('Verdana',25))
    generateno.place(x=390, y=450, anchor="center")
    generateno = Button(game, text='Get Answer', font=('Verdana',25))
    generateno.place(x=580, y=450, anchor="center")
    game.mainloop()

#Menu Screen Functions
def test():
    messagebox.showinfo("Help", "This is a Periodic Table of elements game. You will be given an atomic no. You will have to guess the element's symbol from it")

def home():
    global menu
    menu = Tk()
    menu.title("Elements game")
    menu.geometry("800x500")
    label = Label(text="Periodic Table of Elements Game", font=("Helvetica", 30))
    label.place(x=400, y=25, anchor="center")
    start = Button(menu, text='Start Game', width=35, height=6 ,font='Times 20 bold', command=startgame)
    start.place(x=200, y=250, anchor="center")
    help = Button(menu, text='Help', width=35, height=6 ,font='Times 20 bold', command=test)
    help.place(x=600, y=250, anchor="center")
    menu.mainloop()

home()