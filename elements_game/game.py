from tkinter import *
from tkinter import messagebox
import json
import random
import os 

#Global Vars
elements = {}
answer = ""
answer_name = ""
atomic_no = 0
incorrect_attempts = 5
hval = 1

nonmetal = [1,5,14,32,33,51,52,84]
alkalimetal = [3,11,19,37,55,87]
alkaliearth = [4,12,20,88]
transmetal = [21,39,22,40,72,104,23,41,73,105,24,42,74,106,25,43,75,107,26,44,76,108,27,45,77,109,28,46,78,110,29,47,79,111,30,48,80,112]
basicmetal = [13,31,49,81,113,50,82,114,83,115,116]
semimetal = [5,14,32,33,51,52,84]
halogen = [9,17,35,53,85,117]
noblegas = [2,10,18,36,54,86,118]
lanthanide = [57,58,59,60,61,62,63,64,65,66,67,68,69,70,71]
actinide = [89,90,91,92,93,94,95,96,97,98,99,100,101,102,103]
liquid22 = [80,35]
liquid30 = [55,87,31]
gas = [1,2,7,8,9,10,17,18,36,54,86]

#Game Functions
def generate_hint(atomno):
   global hval
   if hval == 3:
      hval = 1
   else:
      hval = hval+1

   if hval == 1:
      fcr = answer_name[0]
      return "The First letter of the name starts with "+fcr
   elif hval == 2:
      if atomno in nonmetal:
         return "It is a Non Metal"
      elif atomno in alkalimetal:
         return "It is an Alakali Metal"
      elif atomno in alkaliearth:
         return "It is an Alakaline Earth"
      elif atomno in transmetal:
         return "It is a Transition Metal"
      elif atomno in basicmetal:
         return "It is a basic Metal"
      elif atomno in semimetal:
         return "It is a Semimetal"
      elif atomno in halogen:
         return "It is a Halogen"
      elif atomno in noblegas:
         return "It is a noble gas"
      elif atomno in lanthanide:
         return "It is a Lanthanide"
      elif atomno in actinide:
         return "It is an Actinide"
   elif hval == 3:
      if atomno in liquid22:
         return "It is a liquid at 22 C"
      elif atomno in liquid30:
         return "It is a liquid at 30 C"
      elif atomno in gas:
         return "It is a gas at 22 C"
      else:
         return "It is a solid at 22 C"

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
        elif incorrect_attempts <= 4:
            messagebox.showinfo("Wrong Answer!","Wrong Answer!! Try again. You have "+str(incorrect_attempts)+" attempts left\nHINT: "+generate_hint(atomic_no))
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
        dir = os.path.dirname(os.path.realpath(__file__))
        f = open(dir+"/elements.json","r")
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

    f1 = Frame(game)
    f1.pack()
    f2 = Frame(game)
    f2.pack()
    f3 = Frame(game)
    f3.pack()
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
    menu.maxsize(800,500)
    menu.minsize(800,500)
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