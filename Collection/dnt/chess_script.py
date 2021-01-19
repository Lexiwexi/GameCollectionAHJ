#==========================================
# Title:  Schach
# Author: Lexiwexi
#
# Variables:
# aboard -> array of board
#   - aboard[y-position][x-position][color,piece]

# Methods:
# linSearch(lys, element)
#   - linear search of elements in lys
# boardGen()
#   - Generates empty array (see aboard)
# boardSet()
#   - Setup chess-board with pieces
# boardDisplay()
#   - Display aboard in console (redundant in pygame)
# boardUpdate(x1, y1, x2, y2)
#   - Move piece from one position to another
# isLegalMove(x1, y1, x2, y2, piece, currentcolor)
#   - Check is move from one position to another is legal
# pieceId(array)
#   - Output Id of piece
#   - array[0] = piece; array[1] = color
# playerId(player)
#   - Output color of player from id
# playerMove(Player)
#   - Get player input
#==========================================

aboard = []
charset = "ABCDEFGH"
playerList = ["Black","White"]


def linSearch(lys, element):
    '''Linear search of element in lys'''
    for i in range (len(lys)):
        if lys[i] == element:
            return i
    return -1

def boardGen():
    '''Generate/Reset board through appending new list elements'''
    for i in range(8):
        aboard.append([])
        for j in range(8):
            aboard[i].append([0,0])


def boardSet():
    '''Setup Board with pieces by asigning each color-square a piece'''
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



def boardDisplay():
    '''Display board in console line by line

    function is redundant in pygame'''
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
        print("",i+1,end="")
        print()
    print("x",charset,"x")

def boardUpdate(x1,y1,x2,y2):
    '''move piece from 'x1','y1' to 'x2','y2''''
    aboard[y2][x2]=aboard[y1][x1]
    aboard[y1][x1]=[0,0]

def isLegalMove(x1,y1,x2,y2,piece,currentcolor):
    '''Checks if move from one square to another is legal

Check if move from 'x1','y1' to 'x2','y2' with current player color as 'currentcolor' is legal'''
    c = 1
    if currentcolor != 0:
        if currentcolor == 1:
            c = 1
        if currentcolor == 2:
            c = -1

    loc1    = aboard[y1][x1]
    loc2    = aboard[y2][x2] 
    if (loc1[0] == currentcolor) and (loc2[0] != currentcolor):
        
        if loc1[1] == 0: #if piece is Pawn
            if ( (y1 != 1) and (c==1) ) or ( (y1 != 6) and (c==-1) ): #if not in Pawn-Line* (x = 2 for black, x = 7 for white)
                if ( ( (x2 == x1) and (y2 == y1+(1*c)) ) and ( aboard[y2][x2] == [0,0] ) ) or ( ( ( (x2==x1+1) or (x2==x1-1) ) and (y2 == y1+1*c) ) and ( aboard[y2][x2] != [0,0] ) ):
                    #ifselected square empty and no movement in x position and movement in y position only 1 (or -1 in case of white) 
                    #or if selected square enemy color and 
                    return True
            else:
                if ( ( (x2 == x1) and (y2 == y1+(2*c) ) and ( aboard[y2][x2] == [0,0] ) ) or ( ( ( (x2==x1+1) or (x2==x1-1) ) and (y2 == y1+2*c) ) and ( aboard[y2][x2] != [0,0] ) ) ) or ( ( ( (x2 == x1) and (y2 == y1+(1*c)) ) and ( aboard[y2][x2] == [0,0] ) ) or ( ( ( (x2==x1+1) or (x2==x1-1) ) and (y2 == y1+1*c) ) and ( aboard[y2][x2] != [0,0] ) ) ):
                    print("hell yea")
                    return True

            if loc1[1] == 1: #if piece is Knight
                if ( (x2 == x1+2)or(x2 == x1-2) ) and ( (y2 == y1+1*c) or (y2 == y1-1*c) ) or ( (x2 == x1+1)or(x2 == x1-1) ) and ( (y2 == y1+2*c) or (y2 == y1-2*c) ):
                    return True

            if loc1[1] == 2: #if piece is King
                if  ( ( (x2==x1+1)or(x2==x1-1) ) or ( (y2==y1+1*c)or(y2==y1-1*c) ) )  or ( ( (x2==x1+1)or(x2==x1-1) ) and ( (y2==y1+1*c)or(y2==y1-1*c) ) ):
                    return True

            if piece == 3: #if piece is Queen
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

            if loc1[1] == 4: #if piece is Bishop
                if (x2-x1)==(y2-y1):
                    for n in range( int( (float(x2-x1)**0.5)**2) ):
                        print(n,'n')
                    return True

            if loc1[1] == 5: #if piece is Rook

                if ( ( (x2-x1) == 0) and ( (y2-y1) != 0) ): #if only movement in y pos
                    for n in range( ( (y2-y1)*c )-1 ): #look between y1 and y2 to see if they are full
                        if aboard[y1+n+1][x1] != [0,0]: #if so, return False
                            return False
                    return True
                
                if ( ( (x2-x1) != 0) and ( (y2-y1) == 0) ): #if only movement in x pos
                    for n in range(x2-x1-1): #look between x1 and x2 to see if they are full
                        if aboard[y1][x1+n+1] != [0,0]: #if so, return False
                            return False
                    return True

def pieceId(array):
    '''Output piece Name

    Redundant in pygame'''
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
    '''Output color of player'''
    if player == 1:
        return "Black"
    if player == 2:
        return "White"
    else:
        return "???"


def playerMove(Player):
    '''Get player input and output into array'''
    z = False

    print("Player",playerList[Player-1],"'s turn:   ")
    """
    x1 = int(input("x1 "))
    y1 = int(input("y1 "))
    x2 = int(input("x2 "))
    y2 = int(input("y1 "))"""

    pos1 = input("Position 1: ")

    if (linSearch(charset,pos1[0]) == -1)or(len(pos1)!=2):
        print('Please input legal value')
        z = True

    while z:
        print()
        pos1 = input("Position 1: ")

        if (linSearch(charset,pos1[0]) == -1)or(len(pos1)!=2):
            print('Please input legal value')
        else:
            z = False

    print(pos1)

    x1 = linSearch(charset,pos1[0])
    y1 = int(pos1[1])-1

    print(pieceId([aboard[y1][x1][1] , Player]))

    pos2 = input("Position 2: ")

    if (linSearch(charset,pos2[0]) == -1)or(len(pos2)!=2):
        print('Please input legal value')
        z = True

    while z:
        print()
        pos2 = input("Position 2: ")
        if (linSearch(charset,pos2[0]) == -1)or(len(pos2)!=2):
            print('Please input legal value')
        else:
            z = False

    x2 = linSearch(charset,pos2[0])
    y2 = int(pos2[1])-1

    return([x1,y1,x2,y2])

#Main
boardGen()
boardSet()

roundCount = 0
G = True
Player = 2
while G:
    boardDisplay()
    roundCount += 1
    move = playerMove(Player) #x1,y1,x2,y2
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
