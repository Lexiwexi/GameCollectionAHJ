import tkinter
import random
    
top = tkinter.Tk()
top.title("Game Collection")

w = tkinter.Label(top, text ='Game Collection')  
w.pack() 

chess_start_button = tkinter.Button(top, text="Schach")
spaceInvaders_start_button = tkinter.Button(top, text="Space Invaders")

chess_start_button.pack()
spaceInvaders_start_button.pack()



tkinter.mainloop()

