#==========================================
# Title:  Game Collection - Main Menu
# Author: Megaterion
#==========================================

import tkinter
import spaceinvaders_main

main = tkinter.Tk()
main.title("Game Collection")

titel = tkinter.Label(main, text ='Game Collection')  
titel.pack()

mframe = tkinter.Frame(main)
mframe.pack()
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
    chess_start_button = tkinter.Button(mframe, command=win1, text="Schach")
    spaceInvaders_start_button = tkinter.Button(mframe, command=win2, text="Space Invaders")
    quit_button = tkinter.Button(mframe, command=close_window, text="Quit")
    
    chess_start_button.pack(fill=tkinter.X)
    spaceInvaders_start_button.pack(fill=tkinter.X)
    quit_button.pack(pady=50)

def win1(event=None):
    #Schach Sub-Window
    clearwin()
    label1 = tkinter.Label(mframe, text='Willst du ein Spiel starten oder einem Spiel beitreten?')
    label1.pack()
    chess_host_button = tkinter.Button(mframe, command=win0, text="Host")
    chess_client_button = tkinter.Button(mframe, command=win0, text="Join")
    chess_host_button.pack(side=tkinter.LEFT, fill=tkinter.X)
    chess_client_button.pack(side=tkinter.RIGHT, fill=tkinter.X)

    back = tkinter.Button(bottomframe, command=win0, text='Back')
    back.pack()

def win2(event=None):
    #Space Invaders starten
    clearwin()
    label1 = tkinter.Label(mframe, text='Space Invaders gestartet')
    label1.pack()
    back = tkinter.Button(mframe, command=win0, text='Back')
    back.pack()
    spaceinvaders_main.main_menu
    
def close_window():
    main.destroy()

win0()

main.mainloop()
