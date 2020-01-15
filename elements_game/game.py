from tkinter import *
from tkinter import messagebox
import json
import random

#Global Vars
elements = {}
answer = ""
answer_name = ""
atomic_no = 0
incorrect_attempts = 5
#Game Functions
def generate_no():
    global incorrect_attempts
    global answer
    global atomic_no
    global answer_name
    global ano
    incorrect_attempts = 5
    atomic_no = random.randint(1,118)
    answer = elements[atomic_no-1]['symbol']
    answer_name = elements[atomic_no-1]['name']
    ano.config(text=atomic_no)

def getans():
    messagebox.showinfo("Answer","The element's name was "+answer_name+". It's symbol was "+answer+" with atomic number "+str(atomic_no))
    generate_no()

def checkans():
    global noentry
    global incorrect_attempts
    global game
    tans = noentry.get()
    if tans == answer:
        messagebox.showinfo("Correct Answer!","Correct Answer!! The element's name was "+answer_name+". It's symbol was "+answer)
        generate_no()
        noentry.delete(0, 'end')
    else:
        incorrect_attempts = incorrect_attempts - 1
        if incorrect_attempts <= 0 :
            messagebox.showinfo("Game over!","Game over! you have answered wrongly more than 5 times! The element's name was "+answer_name+". It's symbol was "+answer)
            game.destroy()
            home()
        elif incorrect_attempts <= 3:
            messagebox.showinfo("Wrong Answer!","Wrong Answer!! Try again. You have "+str(incorrect_attempts)+" attempts left\nHINT: Coming Soon")
            noentry.delete(0, 'end')
        else:
            messagebox.showinfo("Wrong Answer!","Wrong Answer!! Try again. You have "+str(incorrect_attempts)+" attempts left")
            noentry.delete(0, 'end')

def stopgame():
    global game
    res = messagebox.askyesno("Quit Game?","Are you sure you would like to quit the game?")
    if res == True:
        game.destroy()
        home()

def loadjson():
    global elements
    try:
        f = open("elements.json","r")
        elements = json.loads(f.read())
    except:
        print("Unable to load elements.json file. Game quitting")
        exit(1)

def startgame():
    global game
    global ano
    global noentry
    menu.destroy()
    game = Tk()
    game.title("Elements game")
    game.minsize(800,500)
    game.maxsize(800,500)
    alabel = Label(text="Find the Symbol of:", font=("Helvetica", 55)) 
    alabel.place(x=400, y=100, anchor="center")
    ano = Label(game,font=("Helvetica", 200))
    generate_no() 
    ano.place(x=400, y=250, anchor="center")
    noentry = Entry(text="Atomic number",font=('Helvetica',25))
    noentry.place(x=350, y=400, anchor="center")
    submit = Button(game, text='Submit', font=('Helvetica',25), command=checkans)
    submit.place(x=570, y=400, anchor="center")
    stop = Button(game, text='Stop Game', font=('Helvetica',25),command=stopgame)
    stop.place(x=200, y=450, anchor="center")
    generateno = Button(game, text='Generate New no', font=('Helvetica',25),command=generate_no)
    generateno.place(x=390, y=450, anchor="center")
    generateno = Button(game, text='Get Answer', font=('Helvetica',25), command=getans)
    generateno.place(x=580, y=450, anchor="center")
    game.mainloop()

#Menu Screen Functions
def test():
    messagebox.showinfo("Help", "This is a Periodic Table of elements game. You will be given an atomic no. You will have to guess the element's symbol from it")

def home():
    global menu
    menu = Tk()
    menu.title("Elements game")
    menu.minsize(800,500)
    menu.maxsize(800,500)
    label = Label(text="Periodic Table of Elements Game", font=("Helvetica", 30))
    label.place(x=400, y=25, anchor="center")
    start = Button(menu, text='Start Game', width=35, height=6 ,font='Times 20 bold', command=startgame)
    start.place(x=200, y=250, anchor="center")
    help = Button(menu, text='Help', width=35, height=6 ,font='Times 20 bold', command=test)
    help.place(x=600, y=250, anchor="center")
    menu.mainloop()
loadjson()
home()