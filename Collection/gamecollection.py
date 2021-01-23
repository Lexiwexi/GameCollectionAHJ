#==========================================
# Title:  Game Collection - Main Menu
# Author: Megaterion
#==========================================

import tkinter
import runpy


main = tkinter.Tk()
main.title("Game Collection")
main.geometry("{0}x{1}+0+0".format(main.winfo_screenwidth(), main.winfo_screenheight()))


titel = tkinter.Label(main, text ="Game Collection")  
titel.pack()

mframe = tkinter.Frame(main)
mframe.pack(fill=tkinter.X)
bottomframe = tkinter.Frame(main)
bottomframe.pack()

def clearwin(event=None):
    #Widgets löschen
    for child in mframe.winfo_children():
        child.destroy()
    for child in bottomframe.winfo_children():
        child.destroy()

def win0(event=None):
    #Hauptfenster erstellen
    clearwin()

    #Verweise zu den Games
    chess_menu_button = tkinter.Button(mframe, command=win1, text="Schach")
    spaceInvaders_menu_button = tkinter.Button(mframe, command=win2, text="Space Invaders")
    tictactoe_menu_button = tkinter.Button(mframe, command=win3, text="Tic-Tac-Toe")
    tron_menu_button = tkinter.Button(mframe, command=win4, text="Tron")
    
    chess_menu_button.pack(fill=tkinter.X)
    spaceInvaders_menu_button.pack(fill=tkinter.X)
    tictactoe_menu_button.pack(fill=tkinter.X)
    tron_menu_button.pack(fill=tkinter.X)

    #Quit-Button
    quit_button = tkinter.Button(bottomframe, command=close_window, text="Quit")
    quit_button.pack()

def win1(event=None):
    #Schach Sub-Window
    clearwin()
    label1 = tkinter.Label(mframe, text="Willst du ein Spiel starten oder einem Spiel beitreten?")
    label1.pack()
    chess_host_button = tkinter.Button(mframe, command=win0, text="Host")
    chess_client_button = tkinter.Button(mframe, command=win0, text="Join")
    chess_host_button.pack(side=tkinter.LEFT, fill=tkinter.X)
    chess_client_button.pack(side=tkinter.RIGHT, fill=tkinter.X)

    back = tkinter.Button(bottomframe, command=win0, text="Back")
    back.pack()

def win2(event=None):
    #Space Invaders starten
    clearwin()
    label1 = tkinter.Label(mframe, text="Space Invaders starten?")
    label1.pack()
    start = tkinter.Button(mframe, command=start_space_Invaders, text="Start")
    start.pack()
    back = tkinter.Button(mframe, command=win0, text="Back")
    back.pack()
    
def win3(event=None):
    #Tic-Tac-Toe
    clearwin()
    label1 = tkinter.Label(mframe, text="Tic-Tac-Toe starten?")
    label1.pack()
    start = tkinter.Button(mframe, command=start_tictactoe, text="Start")
    start.pack()
    back = tkinter.Button(mframe, command=win0, text="Back")
    back.pack()

def win4(event=None):
    #Tron
    clearwin()
    label1 = tkinter.Label(mframe, text="Tron starten?")
    label1.pack()
    start = tkinter.Button(mframe, command=start_tron, text="Start")
    start.pack()
    back = tkinter.Button(mframe, command=win0, text="Back")
    back.pack()
    
def start_space_Invaders():
    runpy.run_path("spaceinvaders_main.py")

def start_tictactoe():
    runpy.run_path("tictactoe_main.py")

def start_tron():
    runpy.run_path("tron_main.py")


    
def close_window():
    main.destroy()

win0()

main.mainloop()
