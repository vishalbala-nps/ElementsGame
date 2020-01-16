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
    game.minsize(800,550)
    game.maxsize(800,550)

    f1 = Frame(game)
    f1.pack()
    f2 = Frame(game)
    f2.pack()
    f3 = Frame(game)
    f3.pack(pady=25)
    f4 = Frame(game)
    f4.pack()

    alabel = Label(f1,text="Find the Symbol of:", font=("Helvetica", 55)) 
    alabel.pack()

    ano = Label(f2,font=("Helvetica", 130))
    generate_no() 
    ano.pack()

    noentry = Entry(f3,text="Atomic number",font=('Helvetica',25))
    noentry.pack(side=LEFT,padx=10)
    submit = Button(f3, text='Submit', font=('Helvetica',25), command=checkans)
    submit.pack(side=LEFT,padx=10)

    stop = Button(f4, text='Stop Game', font=('Helvetica',25),command=stopgame)
    stop.pack(side=LEFT,padx=10)
    generateno = Button(f4, text='Generate New no', font=('Helvetica',25),command=generate_no)
    generateno.pack(side=LEFT,padx=10)
    ansbtn = Button(f4, text='Get Answer', font=('Helvetica',25), command=getans)
    ansbtn.pack(side=LEFT,padx=10)
    game.mainloop()

#Menu Screen Functions
def test():
    messagebox.showinfo("Help", "This is a Periodic Table of elements game. You will be given an atomic no. You will have to guess the element's symbol from it")

def home():
    global menu
    menu = Tk()
    menu.title("Elements game")
    menu.maxsize(800,550)
    menu.minsize(800,550)
    tframe = Frame(menu)
    tframe.pack()
    bframe = Frame(menu)
    bframe.pack(side=BOTTOM,pady=150)
    label = Label(tframe,text="Periodic Table of Elements Game", font=("Helvetica", 30))
    start = Button(bframe,text='Start Game',font='Times 20 bold', width=25, height=6, command=startgame)
    help = Button(bframe,text='Help',font='Times 20 bold', width=25, height=6, command=test)
    label.pack()
    start.pack(side=LEFT, padx=10)
    help.pack(side=RIGHT, padx=10)

    menu.mainloop()
loadjson()
home()