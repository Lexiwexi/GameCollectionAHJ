#==========================================
# Title:  Schach
# Author: Lexiwexi
#==========================================

aboard = []
charset = "ABCDEFGH"

def linSearch(lys, element):
		for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1

# Generate/Reset board
def boardGen():
    for i in range(8):
        aboard.append([])
        for j in range(8):
            aboard[i].append([0,0])

#Setup Board with pieces
def boardSet():
    for i in range(2):
        for j in range(8):
            aboard[i][j][0] = 1
            aboard[-i-1][j][0] = 2

    #Knight
    aboard[0][1][1] = 1
    aboard[0][-2][1] = 1
    aboard[-1][1][1] = 1
    aboard[-1][-2][1] = 1

    #King     
    aboard[0][4][1] = 2
    aboard[-1][4][1] = 2

    #Queen
    aboard[0][3][1] = 3
    aboard[-1][3][1] = 3

    #Bishop
    aboard[0][2][1] = 4
    aboard[0][-3][1] = 4
    aboard[-1][2][1] = 4
    aboard[-1][-3][1] = 4

    #Rook
    aboard[0][0][1] = 5
    aboard[0][-1][1] = 5
    aboard[-1][0][1] = 5
    aboard[-1][-1][1] = 5
    
    
## Display board in console line by line
def boardDisplay():
    display = ""
    print("x",charset,"x")
    for i in range(len(aboard)):
        print(i+1,"",end="")
        for j in range(len(aboard[i])):
            if aboard[i][j][0] != 0: #if not empty
                if aboard[i][j][0] == 1: #if Black
                    if aboard[i][j][1] == 0:
                        display = "♟"
                    if aboard[i][j][1] == 1:
                        display = "♞"
                    if aboard[i][j][1] == 2:
                        display = "♚"
                    if aboard[i][j][1] == 3:
                        display = "♛"
                    if aboard[i][j][1] == 4:
                        display = "♝"
                    if aboard[i][j][1] == 5:
                        display = "♜"
                if aboard[i][j][0] == 2: #if White
                    if aboard[i][j][1] == 0:
                        display = "♙"
                    if aboard[i][j][1] == 1:
                        display = "♘"
                    if aboard[i][j][1] == 2:
                        display = "♔"
                    if aboard[i][j][1] == 3:
                        display = "♕"
                    if aboard[i][j][1] == 4:
                        display = "♗"
                    if aboard[i][j][1] == 5:
                        display = "♖"
            else:
                display = "□"
                
            print(display,end="")
        print("",i,end="")
        print()
    print("x",charset,"x")
    
#is move x1 y1 to x2 y2 legal?
def isLegalMove(x1,y1,x2,y2,piece,currentcolor):
    c = 1
    if currentcolor != 0:
        if currentcolor == 1:
            c = 1
        if currentcolor == 2:
            c = -1
        print(c)
        #print(aboard[y1][x1][0])
        if ((aboard[y1][x1][0] == currentcolor) and (aboard[y1][x1][1] == piece) ) and (aboard[y2][x2][0] != currentcolor):
            if piece == 0: #Pawn
                if ( ( (x2 == x1) and (y2 == y1+(1*c)) ) and ( aboard[y2][x2] == [0,0] ) ) or ( ( ( (x2==x1+1) or (x2==x1-1) ) and (y2 == y1+1*c ) ) and ( aboard[y2][x2] != [0,0] ) ):
                    return True
                
            if piece == 1: #Knight
                if ( (x2 == x1+2)or(x2 == x1-2) ) and ( (y2 == y1+1*c) or (y2 == y1-1*c) ) or ( (x2 == x1+1)or(x2 == x1-1) ) and ( (y2 == y1+2*c) or (y2 == y1-2*c) ):
                    return True
                
            if piece == 2: #King
                if  ( ( (x2==x1+1)or(x2==x1-1) ) or ( (y2==y1+1*c)or(y2==y1-1*c) ) )  or ( ( (x2==x1+1)or(x2==x1-1) ) and ( (y2==y1+1*c)or(y2==y1-1*c) ) ):
                    return True
                
            if piece == 3: #Queen
                if ( (x2-x1)==(y2-y1) ):
                    return True
                
                if ( ( (x2-x1) == 0) and ( (y2-y1) != 0) ):
                    for n in range( ( (y2-y1)*c )-1 ):
                        if aboard[y1+n+1][x1] != [0,0]:
                            return False
                        
                    return True
                if ( ( (x2-x1) != 0) and ( (y2-y1) == 0) ):
                    for n in range(x2-x1-1):
                        if aboard[y1][x1+n+1] != [0,0]:
                            return False
                    return True
                
            if piece == 4:
                if (x2-x1)==(y2-y1):
                    for n in range( int( (float(x2-x1)**0.5)**2) ):
                        print(n,'n')
                    return True
                
            if piece == 5:
                if ( ( (x2-x1) == 0) and ( (y2-y1) != 0) ):
                    #print(y2-y1*c,"in y")
                    for n in range( ( (y2-y1)*c )-1 ):
                        #print(n)
                        #print(aboard[y1+n+1][x1])
                        if aboard[y1+n+1][x1] != [0,0]:
                            return False
                        
                    return True
                if ( ( (x2-x1) != 0) and ( (y2-y1) == 0) ):
                    #print(x2-x1)
                    for n in range(x2-x1-1):
                        #print(n)
                        if aboard[y1][x1+n+1] != [0,0]:
                            return False
                    return True
                    

'''
...A....E..
___A....E__ -> 4 x .


A.O..E
v
. 
O !
.
.
'''

#move piece from x1,y1 to x2,y2
def boardUpdate(x1,y1,x2,y2):
    aboard[y2][x2]=aboard[y1][x1]
    aboard[y1][x1]=[0,0]

#Output piece Name
def pieceId(array):
    rank = array[0]
    color = array[1]
    outp = ""
    if color > 0:
        if rank == 0:
            outp = "Pawn"
        if rank == 1:
            outp = "Knight" 
        if rank == 2:
            outp = "King"
        if rank == 3:
            outp = "Queen"
        if rank == 4:
            outp = "Bishop"
        if rank == 5:
            outp = "Rook"

    if color == 1:
        outp = "Black " + outp
    if color == 2:
        outp = "White " + outp

    return(outp)

def playerId(player):
    if player == 1:
        return "Black"
    if player == 2:
        return "White"
    else:
        return "???"

#PlayerTurn
def playerMove(Player):
    print("Player",Player,"'s turn:   ")
    """
    x1 = int(input("x1 "))
    y1 = int(input("y1 "))
    x2 = int(input("x2 "))
    y2 = int(input("y1 "))"""

    pos1 = input("Position 1: ")
    
    x1 = linSearch(charset,pos1[0])
    y1 = int(pos1[1])-1

    print(pieceId([aboard[x1+1][y1+1][1] , Player]))
    
    pos2 = input("Position 2: ")

    x2 = linSearch(charset,pos2[0])
    y2 = int(pos2[1])-1
        
    return([x1,y1,x2,y2])

#Main
boardGen()
boardSet()

G = True
Player = 1
while G:
    boardDisplay()
    move = playerMove(Player) #x1,y1,x2,y2
    #print(aboard[move[1]][move[0]][1])
    if isLegalMove(move[0],move[1],move[2],move[3],aboard[move[1]][move[0]][1],Player):
        boardUpdate(move[0],move[1],move[2],move[3])
        print(pieceId([aboard[move[1]-1][move[0]-1][1] , Player]), "moves to", (charset[move[2]]+str(move[3]) ) )
        if Player == 1:
            Player = 2
        else:
            Player = 1
    else:
        print("!!!Move is not legal!!!")
        print()
        print("Select another move")
    
#==========================================
Tkinter pygame stuff
from tkinter import *
import pygame

#Tkinter fenster
fenster=Tk()
fenster.geometry("500x450")
#label Schach
lbl1=Label(fenster,text='Schach')
#label Player
lblp=Label(fenster,text='Am Zug:')
lblp.place(x=10, y=80)
#Buttonnewgame
btn_erstellen=Button(fenster,text="New Game",command=erstellen)
btn_erstellen.pack(anchor=S,padx=10,pady=10,expand=0,side=LEFT)
btn_erstellen.place(x=10, y=410)
#Button Start
btn_erstellen=Button(fenster,text="Start",command=start)
btn_erstellen.pack(anchor=S,padx=10,pady=10,expand=0,side=LEFT)
btn_erstellen.place(x=10, y=10)
#Buttonende
btn_ende=Button(fenster,text="Ende",command=schließen)
btn_ende.pack(anchor=S,padx=10,pady=10,expand=0,side=LEFT)
btn_ende.place(x=90, y=410)
#Textfeld x1
txtx1=Entry(fenster)
txtx1.pack(padx=10,pady=10)
txtx1.place(x=100, y=200)
#Textfeld y1
txty1=Entry(fenster)
txty1.pack(padx=10,pady=10)
txty1.place(x=100, y=250)
#Textfeld x2
txtx2=Entry(fenster)
txtx2.pack(padx=10,pady=10)
txtx2.place(x=340, y=200)
#Textfeld y2
txty2=Entry(fenster)
txty2.pack(padx=10,pady=10)
txty2.place(x=340, y=250)

#Label x1
lbl2=Label(fenster,text='Eingabe für x1')
lbl2.place(x=10, y=200)
#Label x2
lbl3=Label(fenster,text='Eingabe für x2')
lbl3.place(x=250, y=200)
#Label y1
lbl3=Label(fenster,text='Eingabe für y1')
lbl3.place(x=10, y=250)
#Label y2
lbl3=Label(fenster,text='Eingabe für y2')
lbl3.place(x=250, y=250)

#Figuren aus Dokument
#Bishop l+b
bl = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\bl.png.png')
bb = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\bb.png')
#king l+b
kl = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\kl.png')
kb = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\kb.png')
#knigth l+b
nl = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\nl.png')
nb = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\nb.png')
#pawn l+b
pl = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\pl.png')
pb = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\pb.png')
#queen l+b
ql = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\ql.png')
qb = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\qb.png')
#rook l+b
rl = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\rl.png')
rb = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\rb.png')

#pygame screen
pygame.init()
#größe
screen = pygame.display.set_mode([700, 700])
#farben
screen.fill((255, 255, 255))



    


