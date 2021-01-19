import random
import time
import subprocess as sp

S = 0
G = 0

def mischen(mischzahl):
    for i in range(mischzahl):
        j=random.randrange(51)+1
        jtwo = random.randrange(51)+1

        tempf = KartenF[j]
        tempz = KartenZ[j]

        KartenF[j] = KartenF[jtwo]
        KartenZ[j] = KartenZ[jtwo]

        KartenF[jtwo] = tempf
        KartenZ[jtwo] = tempz

def translate(Z, F):
    tran = ''
    if F == 1:
        tran += '♣'
    if F == 2:
        tran += '♠'
    if F == 3:
        tran += '♡'
    if F == 4:
        tran += '♢'

    
    if Z == 1 :
        tran += 'A'
    if Z == 2 :
        tran += '2'
    if Z == 3 :
        tran += '3'
    if Z == 4 :
        tran += '4'
    if Z == 5 :
        tran += '5'
    if Z == 6 :
        tran += '6'
    if Z == 7 :
        tran += '7'
    if Z == 8 :
        tran += '8'
    if Z == 9 :
        tran += '9'
    if Z == 10:
        tran += '10'
    if Z == 11:
        tran += 'B'
    if Z == 12:
        tran += 'D'
    if Z == 13:
        tran += 'K'

    return(tran)

def Sziehen():
    global S
    for i in range(51):
        if (ShZ[i] == None) and (ShF[i] == None):
            for j in range(51):
                if (KartenF[j] != [None]) and (KartenZ[j] != [None]):
                    ShZ[i] = KartenZ[j]
                    ShF[i] = KartenF[j]
                    KartenZ[j] = [None]
                    KartenF[j] = [None]
                    S += 1
                    return

def Slegen():
    g= 1
    global Gt
    global TopZ
    global TopF
    global S
    global G
    while g == 1:
        print('Ihre Hand:')
        print('0 : Ziehen')
        for i in range(S):
            print(i+1,' : ', translate(ShZ[i],ShF[i]))
        time.sleep(1)      
        print()
        print('Welche Karte möchten sie legen?')
        whl = int(input())-1
        if whl == -1:
            Sziehen()
            g = 0

        elif ShZ[int(whl)] == 11:
            print('Sie dürfen sich eine Farbe wünschen')
            print('1 : Kreuz')
            print('2 : Piek')
            print('3 : Herz')
            print('4 : Karo')
            nF = input()
            TopZ = ShZ[int(whl)]
            TopF = int(nF)      
            del ShZ[int(whl)]
            del ShF[int(whl)]
            S -= 1
            g = 0
            
        elif (ShZ[int(whl)] == TopZ) or (ShF[int(whl)] == TopF):
            if ShZ[int(whl)] == 8 or ShZ[int(whl)] == 7:
                Gt=0
                if ShZ[int(whl)] == 7:
                    for i in range(1):
                        
                        for i in range(51):
                            if (GhZ[i-1] == [None]) and (GhF[i-1] == [None]):
                                for j in range(51):
                                    if (KartenF[j] != [None]) and (KartenZ[j] != [None]):
                                        GhZ[i] = KartenZ[j]
                                        GhF[i] = KartenF[j]
                                        KartenZ[j] = [None]
                                        KartenF[j] = [None]
                                        G += 1
                                        #return
                    print('Ihr Gegner zieht 2 Karten')
                else:
                    print('Ihr Gegner setzt eine Runde aus')
                        
                    
            TopZ = ShZ[int(whl)]
            TopF = ShF[int(whl)]      
            del ShZ[int(whl)]
            del ShF[int(whl)]
            S -= 1
            g  = 0

        
            
        else:
            print()
            print('!!!Diese Karte können sie nicht legen!!!')
            print()

def Glegen():
    global St
    global G
    global TopZ
    global TopF
    chZ = [None] * 52
    chF = [None] * 52
    ch  = [None] * 52
    l = 0
    for i in range(len(GhZ)):
        if (GhZ[i] == TopZ) or (GhF[i] == TopF):
            ch[l] = i
            l += 1

    if l != 0:
        gwhl  = random.randrange(l)
        if (GhZ[ch[gwhl]] == 8) or (GhZ[ch[gwhl]] == 7):
           St=0
           if (GhZ[ch[gwhl]] == 7):
               Sziehen()
               Sziehen()
               print('Ihr Gegner legt eine 7')
               print('Sie ziehen 2 Karten')
               print()
           else:
               print('Ihr Gegner legt eine 8')
               print('Sie setzen eine Runde aus')
        TopZ  = GhZ[ch[gwhl]]
        TopF  = GhF[ch[gwhl]]      
        del GhZ[ch[gwhl]]
        del GhF[ch[gwhl]]
        G -= 1
        time.sleep(1)
        print('Ihr Gegner legt eine Karte')
        print('Die oberste Karte ist', translate(TopZ, TopF))
    
        
    else:
        time.sleep(1)
        print('Ihr Gegner zieht eine Karte')
        
        
        for i in range(52):
            if (GhZ[i] == None) and (GhF[i] == None):
                for j in range(52):
                    if (KartenF[j] != [None]) and (KartenZ[j] != [None]):
                        GhZ[i] = KartenZ[j]
                        GhF[i] = KartenF[j]
                        KartenZ[j] = [None]
                        KartenF[j] = [None]
                        G += 1
                        return    


    

KartenF = [None] * 52 #Karten       Form
KartenZ = [None] * 52 #Karten       Zahl
ShF     = [None] * 52 #Spieler hand Form
ShZ     = [None] * 52 #Spieler hand Zahl
GhF     = [None] * 52 #Gegner  hand Form
GhZ     = [None] * 52 #Gegner  hand Zahl

#kartendeck generieren
for i in range(4):
    for j in range(13):
        KartenZ[j+(13*(i+1))-13] = j+1
        KartenF[j+(13*(i+1))-13] = i+1

#karten mischen
mischen(random.randrange(75)+25)
print('♢ Maumau ♠')
t = 1
while t == 1:
  print('Wie viele Karten soll ich jedem Spieler geben?')
  AmountK = int(input())
  if AmountK > 13:
    sp.call('clear',shell=True)
    print('Die Zahl ist zu groß!')
    print()
  else:
    break
sp.call('clear',shell=True)
#karten verteilen
Num = 0
for i in range(int(AmountK)):
    ShF[i] = KartenF[Num]
    ShZ[i] = KartenZ[Num]
    S += 1
    KartenF[Num] = [None]
    KartenZ[Num] = [None]
    Num += 1
    GhF[i] = KartenF[Num]
    GhZ[i] = KartenZ[Num]
    G += 1
    KartenF[Num] = [None]
    KartenZ[Num] = [None]
    Num += 1
#Top = translate(KartenZ[int(AmountK)*2],KartenF[int(AmountK)*2])

for i in range(52):
        if (KartenF[i] != [None]) and (KartenZ[i] != [None]):
            TopF = KartenF[i]
            TopZ = KartenZ[i]
St= 1
Gt= 1
game = 1
while game == 1: #Gameloop
    if St == 1:
        
        print('Die oberste Karte ist', translate(TopZ, TopF)) #Eigener turn
        print()
        time.sleep(1)
        print('Sie sind drann')
        time.sleep(1)
        Slegen()
        if S == 0:
            print('Sie rufen "Maumau"')
            time.sleep(2)
            sp.call('clear',shell=True)  
            print('Sie haben gewonnen')
            print()
            print('Glückwunsch')
            game = 0
            break
        elif S == 1:
            print('Sie rufen "Mau"')
        print()
    St=1
    sp.call('clear',shell=True)        

        
    if Gt == 1:        
        print('Die oberste Karte ist', translate(TopZ, TopF)) #Gegner turn
        print()
        
        time.sleep(1)
        print('Der Gegner ist drann')
        time.sleep(random.randrange(3))
        Glegen()
        if G == 0:
            print('Ihr Gegner ruft "Maumau"')
            time.sleep(2)
            sp.call('clear',shell=True)  
            print('Ihr Gegner gewann')
            game = 0
            break
        elif G == 1:
            print('Ihr Gegner ruft "Mau"')
        print('Ihr Gegner besitzt noch ', G,' Karten')
        print()
        time.sleep(5)
    Gt=1
    sp.call('clear',shell=True)

#credit goes to Lexi(, that's me)    