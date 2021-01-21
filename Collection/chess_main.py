#==========================================
# Title:  Schach/ Tkinter + Pygame mix
# Author: Lexiwexi
#==========================================
from tkinter import *
import pygame

aboard = []
charset = "ABCDEFGH"     
    
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

def playerId(player):
    if player == 1:
        return "Black"
    if player == 2:
        return "White"
    else:
        return "???"

#Main while loop macht sich nicht gut mit tkinter

'''G = True
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
        print("Select another move")'''
def main():
    boardDisplay()
    move = playerMove(Player) #x1,y1,x2,y2
    if isLegalMove(move[0],move[1],move[2],move[3],aboard[move[1]][move[0]][1],Player):
            if Player==1:
                Player = 2
                boardUpdate(move[0],move[1],move[2],move[3])
                main()
            else:
                Player = 1
                main()
    else:
            lblp=Label(fenster,text='Falscher Zug')
            lblp.place(x=80, y=80)
            main()
#==========================================
#funktionen angepasst

#Start button funktion
def start():
	boardGen()
	boardSet()
	erstellen()
	main()
	
#beenden
def schließen():
    pygame.quit()
    fenster.destroy()

#Schachbrett
def erstellen():
    pygame.draw.rect(screen, (30,30,30), (65,65,5,570))
    pygame.draw.rect(screen, (30,30,30), (65,630,570,5))
    pygame.draw.rect(screen, (30,30,30), (630,65,5,570))
    pygame.draw.rect(screen, (30,30,30), (65,65,570,5))
    for a in range(4):
        for b in range(4):
            x=70+a*140
            y=140+b*140
            pygame.draw.rect(screen, (30,30,30), (x,y,70,70))
    for a in range(4):
        for b in range(4):
            x=140+a*140
            y=70+b*140
            pygame.draw.rect(screen, (30,30,30), (x,y,70,70))
	
# Generate/Reset board
def boardGen():
    for i in range(8):
        aboard.append([])
        for j in range(8):
            aboard[i].append([0,0]) 

#list for placmend
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

#move piece from x1,y1 to x2,y2
def boardUpdate(x1,y1,x2,y2):
    aboard[y2][x2]=aboard[y1][x1]
    aboard[y1][x1]=[0,0]
    screen.fill((255, 255, 255))
    boardDisplay()

#Koordinaten von x1 y1 x2 y2
def playerMove():
	fenster2=Tk()
	fenster2.geometry("100x100")
	#Textfeld x1
	txtx1=Entry(fenster2)
	txtx1.pack(padx=10,pady=10)
	txtx1.place(x=100, y=200)
	#Textfeld y1
	txty1=Entry(fenster2)
	txty1.pack(padx=10,pady=10)
	txty1.place(x=100, y=250)
	#Textfeld x2
	txtx2=Entry(fenster2)
	txtx2.pack(padx=10,pady=10)
	txtx2.place(x=340, y=200)
	#Textfeld y2
	txty2=Entry(fenster2)
	txty2.pack(padx=10,pady=10)
	txty2.place(x=340, y=250)

	#Label x1
	lbl2=Label(fenster2,text='Eingabe für x1')
	lbl2.place(x=10, y=200)
	#Label x2
	lbl3=Label(fenster2,text='Eingabe für x2')
	lbl3.place(x=250, y=200)
	#Label y1
	lbl3=Label(fenster2,text='Eingabe für y1')
	lbl3.place(x=10, y=250)
	#Label y2
	lbl3=Label(fenster2,text='Eingabe für y2')
	lbl3.place(x=250, y=250)
	
	#Button move
	btn_erstellen=Button(fenster2,text="Move",command=playerMoveEingabe)
	btn_erstellen.pack(anchor=S,padx=10,pady=10,expand=0,side=LEFT)
	btn_erstellen.place(x=80, y=10)
	
def playerMoveEingabe():
    a=txtx1.get()
    if a!='':
        txtx1.delete(0, END)
        x1=int(a)
    else:
        txtx1.delete(0, END)

    b=txty1.get()
    if b!='':
        txty1.delete(0, END)
        y1=int(b)
    else:
        txty1.delete(0, END)

    c=txtx2.get()
    if c!='':
        txtx2.delete(0, END)
        x2=int(c)
    else:
        txtx2.delete(0, END)

    d=txty2.get()
    if d!='':
        txty2.delete(0, END)
        y2=int(d)
    else:
        txty2.delete(0, END)
        fenster.destroy()
    return([x1,y1,x2,y2])

#board update
def boardDisplay():
    display = ""
    for i in range(8):
        for j in range(8):
            if aboard[i][j][0] != 0: #if not empty
                a=70+i*70
                b=70+j*70
                if aboard[i][j][0] == 1: #if Black
                    if aboard[i][j][1] == 0:
                        screen.blit(pb, (b,a))
                    if aboard[i][j][1] == 1:
                        screen.blit(nb, (b,a))
                    if aboard[i][j][1] == 2:
                        screen.blit(kb, (b,a))
                    if aboard[i][j][1] == 3:
                        screen.blit(qb, (b,a))
                    if aboard[i][j][1] == 4:
                        screen.blit(bb, (b,a))
                    if aboard[i][j][1] == 5:
                        screen.blit(rb, (b,a))
                if aboard[i][j][0] == 2: #if White
                    if aboard[i][j][1] == 0:
                        screen.blit(pl, (b,a))
                    if aboard[i][j][1] == 1:
                        screen.blit(nl, (b,a))
                    if aboard[i][j][1] == 2:
                        screen.blit(kl, (b,a))
                    if aboard[i][j][1] == 3:
                        screen.blit(ql, (b,a))
                    if aboard[i][j][1] == 4:
                        screen.blit(bl, (b,a))
                    if aboard[i][j][1] == 5:
                        screen.blit(rl, (b,a))
    pygame.display.flip()
	
#==========================================
#klappt nicht mit formatierung
#Tkinter pygame stuff

#Tkinter fenster
fenster=Tk()
fenster.geometry("500x450")
#label Schach
lbl1=Label(fenster,text='Schach')
#label Player
lblp=Label(fenster,text='Am Zug:')
lblp.place(x=10, y=80)
#Button Start
btn_erstellen=Button(fenster,text="Start",command=start)
btn_erstellen.pack(anchor=S,padx=10,pady=10,expand=0,side=LEFT)
btn_erstellen.place(x=10, y=10)
#Buttonende
btn_ende=Button(fenster,text="Ende",command=schließen)
btn_ende.pack(anchor=S,padx=10,pady=10,expand=0,side=LEFT)
btn_ende.place(x=90, y=410)

#Figuren aus Dokument
#Bishop l+b
'''bl = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\bl.png.png')
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
rb = pygame.image.load(r'C:\Users\Jan-Eric Gedicke\Documents\Schachfiguren\rb.png')'''

#pygame screen
pygame.init()
#größe
screen = pygame.display.set_mode([700, 700])
#farben
screen.fill((255, 255, 255))
