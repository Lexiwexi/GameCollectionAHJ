#==========================================
# Title:  Schach
# Author: Lexiwexi
#==========================================

aboard = []
charset = "ABCDEFGH"

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
    
    
# Display board in console
def boardDisplay():
    display = ""
    for i in range(len(aboard)):
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
                display = " "
                
            print(display,end="")
        print()

#is move x1 y1 to x2 y2 legal?
def isLegalMove(x1,y1,x2,y2,piece,currentcolor):
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if currentcolor != 0:
        #print(aboard[y1][x1][0])
        if ((aboard[y1][x1][0] == currentcolor) and (aboard[y1][x1][1] == piece) ) and (aboard[y2][x2][0] != currentcolor):
            if piece == 0:
                if ( ( (x2 == x1) and (y2 == y1+1) ) and ( aboard[y2][x2] == [0,0] ) ) or ( ( ( (x2==x1+1) or (x2==x1-1) ) and (y2 == y1+1 ) ) and ( aboard[y2][x2] != [0,0] ) ):
                    return True
            if piece == 1:
                if ( (x2 == x1+2)or(x2 == x1-2) ) and ( (y2 == y1+1) or (y2 == y1-1) ) or ( (x2 == x1+1)or(x2 == x1-1) ) and ( (y2 == y1+2) or (y2 == y1-2) ):
                    return True
            if piece == 2:
                if  ( ( (x2==x1+1)or(x2==x1-1) ) or ( (y2==y1+1)or(y2==y1-1) ) )  or ( ( (x2==x1+1)or(x2==x1-1) ) and ( (y2==y1+1)or(y2==y1-1) ) ):
                    return True
            if piece == 3:
                if ( ( ( (x2-x1) != 0) and ( (y2-y1) == 0) ) or ( ( (x2-x1) == 0) and ( (y2-y1) != 0) ) ) or ( (x2-x1)==(y2-y1) ):
                    return True
            if piece == 4:
                if (x2-x1)==(y2-y1):
                    return True
            if piece == 5:
                if ( ( (x2-x1) != 0) and ( (y2-y1) == 0) ) or ( ( (x2-x1) == 0) and ( (y2-y1) != 0) ):
                    return True

#move piece from x1,y1 to x2,y2
def boardUpdate(x1,y1,x2,y2):
    aboard[y2-1][x2-1]=aboard[y1-1][x1-1]
    aboard[y1-1][x1-1]=[0,0]

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

#PlayerTurn
def playerMove(Player):
    print("Player",Player,"'s turn:   ")
    x1 = int(input("x1 "))
    y1 = int(input("y1 "))
    x2 = int(input("x2 "))
    y2 = int(input("y1 "))
    return([x1,y1,x2,y2])
'''
Pieces in Chess:

pawn  : 0 ♟︎
-> movement: posy+1
-> attack  : posy+1,posx +/- 1

knight: 1 ♞
-> movement: posy +/- 2, posx +/- 1 OR posy +/- 1, posx +/- 2
-> attack: movement

king  : 2 ♚
-> movement: posy +/- 1 OR posx +/- 1 OR posy +/- 1,posx +/-
-> attack: movement
queen : 3 ♛
-> movement: posy +/- n, posx +/- n OR posy +/- n OR posx +/- n
-> attack: movement

bishop: 4 ♝
-> movement: posy +/- n, posx +/- n
-> attack: movement

rook  : 5 ♜
-> movement: posy +/- n OR posx +/- n
-> attack: movement

boardattributes
board[x][y][color(0-2),piece(0-5)]
'''

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
        print(pieceId([aboard[move[1]][move[0]][1] , Player]), "moves to", (charset[move[2]-1]+str(move[3]) ) )
        if Player == 1:
            Player = 2
        else:
            Player = 1
    else:
        print("!!!Move is not legal!!!")
        print()
        print("Select another move")
    


