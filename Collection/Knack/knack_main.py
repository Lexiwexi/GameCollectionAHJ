import pygame
import random
import time

#globale variablen
global Deck
Deck=['Karo 7','Karo 8','Karo 9','Karo 10','Karo B','Karo D','Karo K','Karo A','Herz 7','Herz 8','Herz 9','Herz 10','Herz B','Herz D,','Herz K','Herz A','Pik 7','Pik 8','Pik 9','Pik 10','Pik B','Pik D','Pik K','Pik A','Kreuz 7','Kreuz 8','Kreuz 9','Kreuz 10','Kreuz B','Kreuz D','Kreuz K','Kreuz A']
global Stappel
Stappel=[]
global Spieler1
Spieler1 = []
global Spieler2
Spieler2 = []
global Spieler3
Spieler3 = []
global Spieler4
Spieler4 = []

#pygame display
pygame.init()
screen = pygame.display.set_mode( (700, 400 ) )
pygame.display.set_caption('Knack')

kreuz7 = pygame.image.load("Knack_Assets\7C.png").convert()
kreuz7 = pygame.transform.scale(kreuz7, (100, 100))
karo7 = pygame.image.load("Knack_Assets\7D.png").convert()
karo7 = pygame.transform.scale(karo7, (100, 100))
pik7 = pygame.image.load("Knack_Assets\7S.png").convert()
pik7 = pygame.transform.scale(pik7, (100, 100))
herz7 = pygame.image.load("Knack_Assets\7H.png").convert()
herz7 = pygame.transform.scale(herz7, (100, 100))

kreuz8 = pygame.image.load("Knack_Assets\8C.png").convert()
kreuz8 = pygame.transform.scale(kreuz8, (100, 100))
karo8 = pygame.image.load("Knack_Assets\8D.png").convert()
karo8 = pygame.transform.scale(karo8, (100, 100))
pik8 = pygame.image.load("Knack_Assets\8S.png").convert()
pik8 = pygame.transform.scale(pik8, (100, 100))
herz8 = pygame.image.load"Knack_Assets\8H.png").convert()
herz8 = pygame.transform.scale(herz8, (100, 100))

kreuz9 = pygame.image.load("Knack_Assets\9C.png").convert()
kreuz9 = pygame.transform.scale(kreuz9, (100, 100))
karo9 = pygame.image.load("Knack_Assets\9D.png").convert()
karo9 = pygame.transform.scale(karo9, (100, 100))
pik9 = pygame.image.load("Knack_Assets\9S.png").convert()
pik9 = pygame.transform.scale(pik9, (100, 100))
herz9 = pygame.image.load("Knack_Assets\9H.png").convert()
herz9 = pygame.transform.scale(herz9, (100, 100))

kreuz10 = pygame.image.load("Knack_Assets\10C.png").convert()
kreuz10 = pygame.transform.scale(kreuz10, (100, 100))
karo10 = pygame.image.load("Knack_Assets\10D.png").convert()
karo10 = pygame.transform.scale(karo10, (100, 100))
pik10 = pygame.image.load("Knack_Assets\10S.png").convert()
pik10 = pygame.transform.scale(pik10, (100, 100))
herz10 = pygame.image.load("Knack_Assets\10H.png").convert()
herz10 = pygame.transform.scale(herz10, (100, 100))

kreuzb = pygame.image.load("Knack_Assets\JC.png").convert()
kreuzb = pygame.transform.scale(kreuzb, (100, 100))
karob = pygame.image.load("Knack_Assets\JD.png").convert()
karob = pygame.transform.scale(karob, (100, 100))
pikb = pygame.image.load("Knack_Assets\JS.png").convert()
pikb = pygame.transform.scale(pikb, (100, 100))
herzb = pygame.image.load("Knack_Assets\JH.png").convert()
herzb = pygame.transform.scale(herzb, (100, 100))

kreuzd = pygame.image.load("Knack_Assets\QC.png").convert()
kreuzd = pygame.transform.scale(kreuzd, (100, 100))
karod = pygame.image.load("Knack_Assets\QD.png").convert()
karod = pygame.transform.scale(karod, (100, 100))
pikd = pygame.image.load("Knack_Assets\QS.png").convert()
pikd = pygame.transform.scale(pikd, (100, 100))
herzd = pygame.image.load"Knack_Assets\QH.png").convert()
herzd = pygame.transform.scale(herzd, (100, 100))

kreuzk = pygame.image.load("Knack_Assets\KC.png").convert()
kreuzk = pygame.transform.scale(kreuzk, (100, 100))
karok = pygame.image.load("Knack_Assets\KD.png").convert()
karok = pygame.transform.scale(karok, (100, 100))
pikk = pygame.image.load("Knack_Assets\KS.png").convert()
pikk = pygame.transform.scale(pikk, (100, 100))
herzk = pygame.image.load("Knack_Assets\KH.png").convert()
herzk = pygame.transform.scale(herzk, (100, 100))

kreuza = pygame.image.load("Knack_Assets\AC.png").convert()
kreuza = pygame.transform.scale(kreuza, (100, 100))
karoa = pygame.image.load("Knack_Assets\AD.png").convert()
karoa = pygame.transform.scale(karoa, (100, 100))
pika = pygame.image.load("Knack_Assets\AS.png").convert()
pika = pygame.transform.scale(pika, (100, 100))
herza = pygame.image.load("Knack_Assets\AH.png").convert()
herza = pygame.transform.scale(herza, (100, 100))

#funktion zum mischen der karten
def mischen():
    for i in range(len(Deck)+100):
        j=random.randrange(len(Deck))#zufällige karte aus deck raussuchen
        jtwo = random.randrange(len(Deck))#zweite zufällige karte aus deck raussuchen

        tempf = Deck[j]#karten tauschen
        tempz = Deck[jtwo]

        Deck[j] = tempz
        Deck[jtwo] = tempf

#funktion zu tauschen aller karten
def alle1():
    Kartetausch=0
    for b in range(3):
        Kartetausch=Stappel[b] # alle Karten tauschen spieler 1
        Stappel[b]=Spieler1[b]
        Spieler1[b]=Kartetausch

def alle2():
    Kartetausch=0
    for b in range(3):
        Kartetausch=Stappel[b] #alle Karten tauschen spieler 2
        Stappel[b]=Spieler2[b]
        Spieler2[b]=Kartetausch

def alle3():
    Kartetausch=0
    for b in range(3):
        Kartetausch=Stappel[b] #alle Karten tauschen spieler 3
        Stappel[b]=Spieler3[b]
        Spieler3[b]=Kartetausch

def alle4():
    Kartetausch=0
    for b in range(3):
        Kartetausch=Stappel[b] #alle Karten tauschen spieler 4
        Stappel[b]=Spieler4[b]
        Spieler4[b]=Kartetausch

#===========================================
#ZÄHLALGORITHMEN VORAUS
#===========================================
def zählen():
    Punkte1=0
    Karo=0
    Herz=0
    Pik=0
    Kreuz=0
    Deckart=[]
    for x in range(3):
        a=Spieler1[x]
        b=a.split()
        c=b[0]
        if c=='Karo':
            Karo=Karo+1
            Deckart.append(c)
        if c=='Herz':
            Herz=Herz+1
            Deckart.append(c)
        if c=='Pik':
            Pik=Pik+1
            Deckart.append(c)
        if c=='Kreuz':
            Kreuz=Kreuz+1
            Deckart.append(c)        
    if Karo>Herz and Karo>Pik and Karo>Kreuz:
        for a in range(3):
            if Deckart[a]=='Karo':
                if Spieler1[a]=='Karo A':
                    Punkte1=Punkte1+11
                if Spieler1[a]=='Karo 10' or Spieler1[a]=='Karo B' or Spieler1[a]=='Karo D' or Spieler1[a]=='Karo K': 
                    Punkte1=Punkte1+10
                if Spieler1[a]=='Karo 7':
                    Punkte1=Punkte1+7
                if Spieler1[a]=='Karo 8':
                    Punkte1=Punkte1+8
                if Spieler1[a]=='Karo 9':
                    Punkte1=Punkte1+9
    if Herz>Karo and Herz>Pik and Herz>Kreuz:
        for a in range(3):
            if Deckart[a]=='Herz':
                if Spieler1[a]=='Herz A':
                    Punkte1=Punkte1+11
                if Spieler1[a]=='Herz 10' or Spieler1[a]=='Herz B' or Spieler1[a]=='Herz D' or Spieler1[a]=='Herz K':
                    Punkte1=Punkte1+10
                if Spieler1[a]=='Herz 7':
                    Punkte1=Punkte1+7
                if Spieler1[a]=='Herz 8':
                    Punkte1=Punkte1+8
                if Spieler1[a]=='Herz 9':
                    Punkte1=Punkte1+9
    if Pik>Herz and Pik>Karo and Pik>Kreuz:
        for a in range(3):
            if Deckart[a]=='Pik':
                if Spieler1[a]=='Pik A':
                    Punkte1=Punkte1+11
                if Spieler1[a]=='Pik 10'or Spieler1[a]=='Pik B'or Spieler1[a]=='Pik D'or Spieler1[a]=='Pik K':
                    Punkte1=Punkte1+10
                if Spieler1[a]=='Pik 7':
                    Punkte1=Punkte1+7
                if Spieler1[a]=='Pik 8':
                    Punkte1=Punkte1+8
                if Spieler1[a]=='Pik 9':
                    Punkte1=Punkte1+9
    if Kreuz>Herz and Kreuz>Pik and Kreuz>Karo:
        for a in range(3):
            if Deckart[a]=='Kreuz':
                if Spieler1[a]=='Kreuz A':
                    Punkte1=Punkte1+11
                if Spieler1[a]=='Kreuz 10'or Spieler1[a]=='Kreuz B'or Spieler1[a]=='Kreuz D'or Spieler1[a]=='Kreuz K':
                    Punkte1=Punkte1+10
                if Spieler1[a]=='Kreuz 7':
                    Punkte1=Punkte1+7
                if Spieler1[a]=='Kreuz 8':
                    Punkte1=Punkte1+8
                if Spieler1[a]=='Kreuz 9':
                    Punkte1=Punkte1+9

    if Punkte1==0:
        a=Spieler1[0]   #Wert der Karte wird festgestellt
        b1=a.split()
        a=Spieler1[1]   #Wert der Karte wird festgestellt
        b2=a.split()
        a=Spieler1[2]   #Wert der Karte wird festgestellt
        b3=a.split()
        if b1[1]==b2[1] and b1[1]==b3[1]:#Abfrage ob alle karten denn selben wert besitzen
            if b1[1]=='A':
                print('Du Gewinnst!!!')#fals Superknack
                neu()
            Punkte1=30.5

    höchstezahl=0
    if Punkte1==0:  #tritt bei drei unterschiedlichen karten auf
        for b in range(3):
            a=Spieler1[b]
            b=a.split()
            c=b[1]
            if c=='A':
                höchstezahl=11
            if c=='10' or c=='B' or c=='D' or c=='K':
                if höchstezahl<10:
                    höchstezahl=10
            if c=='9':
                if höchstezahl<9:
                    höchstezahl=9
            if c=='8':
                if höchstezahl<8:
                    höchstezahl=8
            if c=='7':
                if höchstezahl<7:
                    höchstezahl=7
        Punkte1=höchstezahl

    if Punkte1==31:         #gewinn funktion
        print('Du Gewinnst!!!')
        neu()
        
    Deckart=[]
    print('Du hast->',Punkte1,' Punkte')

    return Punkte1

def zählenspieler2():#Zählen für spieler 2
    Punkte=0
    Karo=0
    Herz=0
    Pik=0
    Kreuz=0
    Deckart=[]
    for x in range(3):
        a=Spieler2[x]
        b=a.split()
        c=b[0]
        if c=='Karo':
            Karo=Karo+1
            Deckart.append(c)
        if c=='Herz':
            Herz=Herz+1
            Deckart.append(c)
        if c=='Pik':
            Pik=Pik+1
            Deckart.append(c)
        if c=='Kreuz':
            Kreuz=Kreuz+1
            Deckart.append(c)
            
    if Karo>Herz and Karo>Pik and Karo>Kreuz:
        for a in range(3):
            if Deckart[a]=='Karo':
                if Spieler2[a]=='Karo A':
                    Punkte=Punkte+11
                if Spieler2[a]=='Karo 10' or Spieler2[a]=='Karo B' or Spieler2[a]=='Karo D' or Spieler2[a]=='Karo K': 
                    Punkte=Punkte+10
                if Spieler2[a]=='Karo 7':
                    Punkte=Punkte+7
                if Spieler2[a]=='Karo 8':
                    Punkte=Punkte+8
                if Spieler2[a]=='Karo 9':
                    Punkte=Punkte+9
    if Herz>Karo and Herz>Pik and Herz>Kreuz:
        for a in range(3):
            if Deckart[a]=='Herz':
                if Spieler2[a]=='Herz A':
                    Punkte=Punkte+11
                if Spieler2[a]=='Herz 10' or Spieler2[a]=='Herz B' or Spieler2[a]=='Herz D' or Spieler2[a]=='Herz K':
                    Punkte=Punkte+10
                if Spieler2[a]=='Herz 7':
                    Punkte=Punkte+7
                if Spieler2[a]=='Herz 8':
                    Punkte=Punkte+8
                if Spieler2[a]=='Herz 9':
                    Punkte=Punkte+9
    if Pik>Herz and Pik>Karo and Pik>Kreuz:
        for a in range(3):
            if Deckart[a]=='Pik':
                if Spieler2[a]=='Pik A':
                    Punkte=Punkte+11
                if Spieler2[a]=='Pik 10'or Spieler2[a]=='Pik B'or Spieler2[a]=='Pik D'or Spieler2[a]=='Pik K':
                    Punkte=Punkte+10
                if Spieler2[a]=='Pik 7':
                    Punkte=Punkte+7
                if Spieler2[a]=='Pik 8':
                    Punkte=Punkte+8
                if Spieler2[a]=='Pik 9':
                    Punkte=Punkte+9
    if Kreuz>Herz and Kreuz>Pik and Kreuz>Karo:
        for a in range(3):
            if Deckart[a]=='Kreuz':
                if Spieler2[a]=='Kreuz A':
                    Punkte=Punkte+11
                if Spieler2[a]=='Kreuz 10'or Spieler2[a]=='Kreuz B'or Spieler2[a]=='Kreuz D'or Spieler2[a]=='Kreuz K':
                    Punkte=Punkte+10
                if Spieler2[a]=='Kreuz 7':
                    Punkte=Punkte+7
                if Spieler2[a]=='Kreuz 8':
                    Punkte=Punkte+8
                if Spieler2[a]=='Kreuz 9':
                    Punkte=Punkte+9

    if Punkte==0:
        a=Spieler2[0]   #Wert der Karte wird festgestellt
        b1=a.split()
        a=Spieler2[1]   #Wert der Karte wird festgestellt
        b2=a.split()
        a=Spieler2[2]   #Wert der Karte wird festgestellt
        b3=a.split()
        if b1[1]==b2[1] and b1[1]==b3[1]:       #Abfrage ob alle karten denn selben wert besitzen
            if b1[1]=='A':
                print('Spieler2 hat ein Superknack!!! -> ',Spieler2)
                print('Spieler2 Gewinnt!!!')#fals Superknack
                neu()
            Punkte=30.5
            
    höchstezahl=0
    if Punkte==0:  #tritt bei drei unterschiedlichen karten auf
        for b in range(3):
            a=Spieler2[b]
            b=a.split()
            c=b[1]
            if c=='A':
                höchstezahl=11
            if c=='10' or c=='B' or c=='D' or c=='K':
                if höchstezahl<10:
                    höchstezahl=10
            if c=='9':
                if höchstezahl<9:
                    höchstezahl=9
            if c=='8':
                if höchstezahl<8:
                    höchstezahl=8
            if c=='7':
                if höchstezahl<7:
                    höchstezahl=7
        Punkte=höchstezahl

    if Punkte==31:         #gewinn funktion
        print('Spieler2 hat 31 Punkte')
        print('Spieler2 Gewinnt!!!')
        neu()
    
    Deckart=[]

    return Punkte

def zählenspieler3():#Zählen für spieler 3
    Punkte1=0
    Karo=0
    Herz=0
    Pik=0
    Kreuz=0
    Deckart=[]
    for x in range(3):
        a=Spieler3[x]
        b=a.split()
        c=b[0]
        if c=='Karo':
            Karo=Karo+1
            Deckart.append(c)
        if c=='Herz':
            Herz=Herz+1
            Deckart.append(c)
        if c=='Pik':
            Pik=Pik+1
            Deckart.append(c)
        if c=='Kreuz':
            Kreuz=Kreuz+1
            Deckart.append(c)
            
    if Karo>Herz and Karo>Pik and Karo>Kreuz:
        for a in range(3):
            if Deckart[a]=='Karo':
                if Spieler3[a]=='Karo A':
                    Punkte1=Punkte1+11
                if Spieler3[a]=='Karo 10' or Spieler3[a]=='Karo B' or Spieler3[a]=='Karo D' or Spieler3[a]=='Karo K': 
                    Punkte1=Punkte1+10
                if Spieler3[a]=='Karo 7':
                    Punkte1=Punkte1+7
                if Spieler3[a]=='Karo 8':
                    Punkte1=Punkte1+8
                if Spieler3[a]=='Karo 9':
                    Punkte1=Punkte1+9
    if Herz>Karo and Herz>Pik and Herz>Kreuz:
        for a in range(3):
            if Deckart[a]=='Herz':
                if Spieler3[a]=='Herz A':
                    Punkte1=Punkte1+11
                if Spieler3[a]=='Herz 10' or Spieler3[a]=='Herz B' or Spieler3[a]=='Herz D' or Spieler3[a]=='Herz K':
                    Punkte1=Punkte1+10
                if Spieler3[a]=='Herz 7':
                    Punkte1=Punkte1+7
                if Spieler3[a]=='Herz 8':
                    Punkte1=Punkte1+8
                if Spieler3[a]=='Herz 9':
                    Punkte1=Punkte1+9
    if Pik>Herz and Pik>Karo and Pik>Kreuz:
        for a in range(3):
            if Deckart[a]=='Pik':
                if Spieler3[a]=='Pik A':
                    Punkte1=Punkte1+11
                if Spieler3[a]=='Pik 10'or Spieler3[a]=='Pik B'or Spieler3[a]=='Pik D'or Spieler3[a]=='Pik K':
                    Punkte1=Punkte1+10
                if Spieler3[a]=='Pik 7':
                    Punkte1=Punkte1+7
                if Spieler3[a]=='Pik 8':
                    Punkte1=Punkte1+8
                if Spieler3[a]=='Pik 9':
                    Punkte1=Punkte1+9
    if Kreuz>Herz and Kreuz>Pik and Kreuz>Karo:
        for a in range(3):
            if Deckart[a]=='Kreuz':
                if Spieler3[a]=='Kreuz A':
                    Punkte1=Punkte1+11
                if Spieler3[a]=='Kreuz 10'or Spieler3[a]=='Kreuz B'or Spieler3[a]=='Kreuz D'or Spieler3[a]=='Kreuz K':
                    Punkte1=Punkte1+10
                if Spieler3[a]=='Kreuz 7':
                    Punkte1=Punkte1+7
                if Spieler3[a]=='Kreuz 8':
                    Punkte1=Punkte1+8
                if Spieler3[a]=='Kreuz 9':
                    Punkte1=Punkte1+9

    if Punkte1==0:
        a=Spieler3[0]   #Wert der Karte wird festgestellt
        b1=a.split()
        a=Spieler3[1]   #Wert der Karte wird festgestellt
        b2=a.split()
        a=Spieler3[2]   #Wert der Karte wird festgestellt
        b3=a.split()
        if b1[1]==b2[1] and b1[1]==b3[1]:       #Abfrage ob alle karten denn selben wert besitzen
            if b1[1]=='A':
                print('Spieler3 hat ein Superknack!!! -> ',Spieler3)
                print('Spieler3 Gewinnt!!!')#fals Superknack
                neu()
            Punkte1=30.5

    höchstezahl=0
    if Punkte1==0:  #tritt bei drei unterschiedlichen karten auf
        for b in range(3):
            a=Spieler3[b]
            b=a.split()
            c=b[1]
            if c=='A':
                höchstezahl=11
            if c=='10' or c=='B' or c=='D' or c=='K':
                if höchstezahl<10:
                    höchstezahl=10
            if c=='9':
                if höchstezahl<9:
                    höchstezahl=9
            if c=='8':
                if höchstezahl<8:
                    höchstezahl=8
            if c=='7':
                if höchstezahl<7:
                    höchstezahl=7
        Punkte1=höchstezahl

    if Punkte1==31:         #gewinn funktion
        print('Spieler3 hat 31 Punkte')
        print('Spieler3 Gewinnt!!!')
        neu()
                    
    Deckart=[]

    return Punkte1
    
def zählenspieler4():#Zählen für spieler 4
    Punkte1=0
    Karo=0
    Herz=0
    Pik=0
    Kreuz=0
    Deckart=[]
    for x in range(3):#welche kartenart ist am meisten auf der hand
        a=Spieler4[x]
        b=a.split()
        c=b[0]
        if c=='Karo':
            Karo=Karo+1
            Deckart.append(c)
        if c=='Herz':
            Herz=Herz+1
            Deckart.append(c)
        if c=='Pik':
            Pik=Pik+1
            Deckart.append(c)
        if c=='Kreuz':
            Kreuz=Kreuz+1
            Deckart.append(c)
            
    if Karo>Herz and Karo>Pik and Karo>Kreuz:
        for a in range(3):
            if Deckart[a]=='Karo':
                if Spieler4[a]=='Karo A':
                    Punkte1=Punkte1+11
                if Spieler4[a]=='Karo 10' or Spieler4[a]=='Karo B' or Spieler4[a]=='Karo D' or Spieler4[a]=='Karo K': 
                    Punkte1=Punkte1+10
                if Spieler4[a]=='Karo 7':
                    Punkte1=Punkte1+7
                if Spieler4[a]=='Karo 8':
                    Punkte1=Punkte1+8
                if Spieler4[a]=='Karo 9':
                    Punkte1=Punkte1+9
    if Herz>Karo and Herz>Pik and Herz>Kreuz:
        for a in range(3):
            if Deckart[a]=='Herz':
                if Spieler4[a]=='Herz A':
                    Punkte1=Punkte1+11
                if Spieler4[a]=='Herz 10' or Spieler4[a]=='Herz B' or Spieler4[a]=='Herz D' or Spieler4[a]=='Herz K':
                    Punkte1=Punkte1+10
                if Spieler4[a]=='Herz 7':
                    Punkte1=Punkte1+7
                if Spieler4[a]=='Herz 8':
                    Punkte1=Punkte1+8
                if Spieler4[a]=='Herz 9':
                    Punkte1=Punkte1+9
    if Pik>Herz and Pik>Karo and Pik>Kreuz:
        for a in range(3):
            if Deckart[a]=='Pik':
                if Spieler4[a]=='Pik A':
                    Punkte1=Punkte1+11
                if Spieler4[a]=='Pik 10'or Spieler4[a]=='Pik B'or Spieler4[a]=='Pik D'or Spieler4[a]=='Pik K':
                    Punkte1=Punkte1+10
                if Spieler4[a]=='Pik 7':
                    Punkte1=Punkte1+7
                if Spieler4[a]=='Pik 8':
                    Punkte1=Punkte1+8
                if Spieler4[a]=='Pik 9':
                    Punkte1=Punkte1+9
    if Kreuz>Herz and Kreuz>Pik and Kreuz>Karo:
        for a in range(3):
            if Deckart[a]=='Kreuz':
                if Spieler4[a]=='Kreuz A':
                    Punkte1=Punkte1+11
                if Spieler4[a]=='Kreuz 10'or Spieler4[a]=='Kreuz B'or Spieler4[a]=='Kreuz D'or Spieler4[a]=='Kreuz K':
                    Punkte1=Punkte1+10
                if Spieler4[a]=='Kreuz 7':
                    Punkte1=Punkte1+7
                if Spieler4[a]=='Kreuz 8':
                    Punkte1=Punkte1+8
                if Spieler4[a]=='Kreuz 9':
                    Punkte1=Punkte1+9

    if Punkte1==0:
        a=Spieler4[0]   #Wert der Karte wird festgestellt
        b1=a.split()
        a=Spieler4[1]   #Wert der Karte wird festgestellt
        b2=a.split()
        a=Spieler4[2]   #Wert der Karte wird festgestellt
        b3=a.split()
        if b1[1]==b2[1] and b1[1]==b3[1]:       #Abfrage ob alle karten denn selben wert besitzen
            if b1[1]=='A':
                print('Spieler4 hat ein Superknack!!! -> ',Spieler4)
                print('Spieler4 Gewinnt!!!')#fals Superknack
                neu()
            Punkte1=30.5#wenn alle gleich aber kein superknack

    höchstezahl=0
    if Punkte1==0:  #tritt bei drei unterschiedlichen karten auf
        for b in range(3):
            a=Spieler4[b]
            b=a.split()
            c=b[1]
            if c=='A':
                höchstezahl=11
            if c=='10' or c=='B' or c=='D' or c=='K':
                if höchstezahl<10:
                    höchstezahl=10
            if c=='9':
                if höchstezahl<9:
                    höchstezahl=9
            if c=='8':
                if höchstezahl<8:
                    höchstezahl=8
            if c=='7':
                if höchstezahl<7:
                    höchstezahl=7
        Punkte1=höchstezahl
        

    if Punkte1==31:         #gewinn funktion
        print('Spieler4 hat 31 Punkte')
        print('Spieler4 Gewinnt!!!')
        neu()
                    
    Deckart=[]

    return Punkte1

def zählenstappel():#Zählen für Stappel
    Punkte1=0
    Karo=0
    Herz=0
    Pik=0
    Kreuz=0
    Deckart=[]
    for x in range(3):#welche kartenart ist am meisten auf dem Stappel
        a=Stappel[x]
        b=a.split()
        c=b[0]
        if c=='Karo':
            Karo=Karo+1
            Deckart.append(c)
        if c=='Herz':
            Herz=Herz+1
            Deckart.append(c)
        if c=='Pik':
            Pik=Pik+1
            Deckart.append(c)
        if c=='Kreuz':
            Kreuz=Kreuz+1
            Deckart.append(c)
            
    if Karo>Herz and Karo>Pik and Karo>Kreuz:
        for a in range(3):
            if Deckart[a]=='Karo':
                if Stappel[a]=='Karo A':
                    Punkte1=Punkte1+11
                if Stappel[a]=='Karo 10' or Stappel[a]=='Karo B' or Stappel[a]=='Karo D' or Stappel[a]=='Karo K': 
                    Punkte1=Punkte1+10
                if Stappel[a]=='Karo 7':
                    Punkte1=Punkte1+7
                if Stappel[a]=='Karo 8':
                    Punkte1=Punkte1+8
                if Stappel[a]=='Karo 9':
                    Punkte1=Punkte1+9
    if Herz>Karo and Herz>Pik and Herz>Kreuz:
        for a in range(3):
            if Deckart[a]=='Herz':
                if Stappel[a]=='Herz A':
                    Punkte1=Punkte1+11
                if Stappel[a]=='Herz 10' or Stappel[a]=='Herz B' or Stappel[a]=='Herz D' or Stappel[a]=='Herz K':
                    Punkte1=Punkte1+10
                if Stappel[a]=='Herz 7':
                    Punkte1=Punkte1+7
                if Stappel[a]=='Herz 8':
                    Punkte1=Punkte1+8
                if Stappel[a]=='Herz 9':
                    Punkte1=Punkte1+9
    if Pik>Herz and Pik>Karo and Pik>Kreuz:
        for a in range(3):
            if Deckart[a]=='Pik':
                if Stappel[a]=='Pik A':
                    Punkte1=Punkte1+11
                if Stappel[a]=='Pik 10'or Stappel[a]=='Pik B'or Stappel[a]=='Pik D'or Stappel[a]=='Pik K':
                    Punkte1=Punkte1+10
                if Stappel[a]=='Pik 7':
                    Punkte1=Punkte1+7
                if Stappel[a]=='Pik 8':
                    Punkte1=Punkte1+8
                if Stappel[a]=='Pik 9':
                    Punkte1=Punkte1+9
    if Kreuz>Herz and Kreuz>Pik and Kreuz>Karo:
        for a in range(3):
            if Deckart[a]=='Kreuz':
                if Stappel[a]=='Kreuz A':
                    Punkte1=Punkte1+11
                if Stappel[a]=='Kreuz 10'or Stappel[a]=='Kreuz B'or Stappel[a]=='Kreuz D'or Stappel[a]=='Kreuz K':
                    Punkte1=Punkte1+10
                if Stappel[a]=='Kreuz 7':
                    Punkte1=Punkte1+7
                if Stappel[a]=='Kreuz 8':
                    Punkte1=Punkte1+8
                if Stappel[a]=='Kreuz 9':
                    Punkte1=Punkte1+9

    if Punkte1==0:#wenn keine art überwiegt
        a=Stappel[0]   #Wert der Karte wird festgestellt
        b1=a.split()
        a=Stappel[1]   #Wert der Karte wird festgestellt
        b2=a.split()
        a=Stappel[2]   #Wert der Karte wird festgestellt
        b3=a.split()
        if b1[1]==b2[1] and b1[1]==b3[1]:       #Abfrage ob alle karten denn selben wert besitzen
            if b1[1]=='A':
                Punkte1=33
            else:
                Punkte1=30,5#wenn alle gleich aber kein superknack

    höchstezahl=0#wenn keine art überwiegt und die drei nicht den selben wert haben->Höchste karte bestimmt punktzahl
    if Punkte1==0:  #tritt bei drei unterschiedlichen karten auf
        for b in range(3):
            a=Stappel[b]
            b=a.split()
            c=b[1]
            if c=='A':
                höchstezahl=11
            if c=='10' or c=='B' or c=='D' or c=='K':
                if höchstezahl<10:
                    höchstezahl=10
            if c=='9':
                if höchstezahl<9:
                    höchstezahl=9
            if c=='8':
                if höchstezahl<8:
                    höchstezahl=8
            if c=='7':
                if höchstezahl<7:
                    höchstezahl=7
        Punkte1=höchstezahl
                       
    Deckart=[]

    return Punkte1

#===========================================
#ZÄHLALGORITHMEN Beendet
#===========================================

def legen():
    for b in range(3):
        a = Deck[0]#drei karten auf den stappel
        Stappel.append(a)
        del Deck[0]

    for b in range(3):#drei karten werden an spieler 1 bis 4 vergeben
        a = Deck[0]
        Spieler1.append(a)
        del Deck[0]
    for b in range(3):
        a = Deck[0]
        Spieler2.append(a)
        del Deck[0]
    for b in range(3):
        a = Deck[0]
        Spieler3.append(a)
        del Deck[0]
    for b in range(3):
        a = Deck[0]
        Spieler4.append(a)
        del Deck[0]
    positionkarte()
    stapelpygame()
    pygame.display.flip()

#neues spiel
def neu():
    for b in range(3):
        a = Stappel[0]
        Deck.append(a)
        del Stappel[0]
        
    for b in range(3):
        a = Spieler1[0]
        Deck.append(a)
        del Spieler1[0]
        
    for b in range(3):
        a = Spieler2[0]
        Deck.append(a)
        del Spieler2[0]
        
    for b in range(3):
        a = Spieler3[0]
        Deck.append(a)
        del Spieler3[0]
        
    for b in range(3):
        a = Spieler4[0]
        Deck.append(a)
        del Spieler4[0]
        
    spiel()

#===========================================
#Bots
#===========================================
def bot():
    Kartetausch=0
    Var1=10
    Var2=10
    Punkte1=zählenspieler2()
    Stappelpunkte=zählenstappel()
    for a in range(3):      #Kartentausch algorithmus
        for b in range(3):
            Kartetausch=Spieler2[a]
            Spieler2[a]=Stappel[b]
            Stappel[b]=Kartetausch
            Punkteneu=zählenspieler2()#Zählen des neuen kartenwertes von spieler zwei
            if int(Punkteneu)>Punkte1:
                Var1=a#Spiechern der Werte zum tauschen
                Var2=b
                Punkte1=Punkteneu
            Kartetausch=Spieler2[a]#zurücktausche damit keine falschen karten getauscht werden
            Spieler2[a]=Stappel[b]
            Stappel[b]=Kartetausch
    if Stappelpunkte>Punkte1:#Fals die punkte des stappels hör sind als die eigennen mit tauschen
        for a in range(3):
            Kartetausch=Spieler2[a]
            Spieler2[a]=Stappel[a]
            Stappel[a]=Kartetausch
        print('Spieler2 tauscht mit dem Stappel')
    elif Var1!=10 and Var2!=10:#fals eine karte getauscht werden muss
        Kartetausch=Spieler2[Var1]
        Spieler2[Var1]=Stappel[Var2]
        Stappel[Var2]=Kartetausch
        print('Spieler2 tauscht ',Spieler2[Var1],' gegen ',Stappel[Var2])
    else:#fals keine karte getauscht werden muss
        print('Spieler2 tausch keine Karte')
    positionkarte()
    stapelpygame()
    pygame.display.flip()

def bot2():
    Kartetausch=0
    Var1=10
    Var2=10
    Punkte1=zählenspieler3()
    Stappelpunkte=zählenstappel()
    for a in range(3):      #Kartentausch algorithmus
        for b in range(3):
            Kartetausch=Spieler3[a]
            Spieler3[a]=Stappel[b]
            Stappel[b]=Kartetausch
            Punkteneu=zählenspieler3()#Zählen des neuen kartenwertes von spieler zwei
            if int(Punkteneu)>Punkte1:
                Var1=a#Spiechern der Werte zum tauschen
                Var2=b
                Punkte1=Punkteneu
            Kartetausch=Spieler3[a]
            Spieler3[a]=Stappel[b]
            Stappel[b]=Kartetausch
    if Stappelpunkte>Punkte1:#Fals die punkte des stappels hör sind als die eigennen mit tauschen
        for a in range(3):
            Kartetausch=Spieler3[a]
            Spieler3[a]=Stappel[a]
            Stappel[a]=Kartetausch
        print('Spieler3 tauscht mit dem Stappel')
    elif Var1!=10 and Var2!=10:#fals keine karte getauscht werden muss
        Kartetausch=Spieler3[Var1]
        Spieler3[Var1]=Stappel[Var2]
        Stappel[Var2]=Kartetausch
        print('Spieler3 tauscht ',Spieler3[Var1],' gegen ',Stappel[Var2])
    else:
        print('Spieler3 tausch keine Karte')
    positionkarte()
    stapelpygame()
    pygame.display.flip()

def bot3():
    Kartetausch=0
    Var1=10
    Var2=10
    Punkte1=zählenspieler4()
    Stappelpunkte=zählenstappel()
    for a in range(3):      #Kartentausch algorithmus
        for b in range(3):
            Kartetausch=Spieler4[a]
            Spieler4[a]=Stappel[b]
            Stappel[b]=Kartetausch
            Punkteneu=zählenspieler4()#Zählen des neuen kartenwertes von spieler zwei
            if int(Punkteneu)>Punkte1:
                Var1=a#Spiechern der Werte zum tauschen
                Var2=b
                Punkte1=Punkteneu
            Kartetausch=Spieler4[a]
            Spieler4[a]=Stappel[b]
            Stappel[b]=Kartetausch
    if Stappelpunkte>Punkte1:#Fals die punkte des stappels hör sind als die eigennen mit tauschen
        for a in range(3):
            Kartetausch=Spieler4[a]
            Spieler4[a]=Stappel[a]
            Stappel[a]=Kartetausch
        print('Spieler4 tauscht mit dem Stappel')
    elif Var1!=10 and Var2!=10:#fals keine karte getauscht werden muss
        Kartetausch=Spieler4[Var1]
        Spieler4[Var1]=Stappel[Var2]
        Stappel[Var2]=Kartetausch
        print('Spieler4 tauscht ',Spieler4[Var1],' gegen ',Stappel[Var2])
    else:
        print('Spieler4 tausch keine Karte')
    positionkarte()
    stapelpygame()
    pygame.display.flip()

def Ende1():#Fals Spieler1 die runde beenden möchte
    time.sleep(random.randint(3,6))
    bot()#haben jeweils noch eine aktion
    stapelpygame()
    pygame.display.flip()
    
    time.sleep(random.randint(3,6))
    bot2()
    stapelpygame()
    pygame.display.flip()
    
    time.sleep(random.randint(3,6))
    bot3()
    stapelpygame()
    pygame.display.flip()
    
    Player=zählen()
    b1=zählenspieler2()
    b2=zählenspieler3()
    b3=zählenspieler4()
    print('Die Runde wurden durch das zumachen beendet')

    if Player>b1 and Player>b2 and Player>b3:#wer hat gewonnen
        print('Du Gewinnst')
    elif b1>Player and b1>b2 and b1>b3:    
        print('Spieler2 Gewinnt')
        print(Spieler2)
    elif b2>b1 and b2>Player and b2>b3:
        print('Spieler3 Gewinnt')
        print(Spieler3)
    elif b3>b1 and b3>Player and b3>b2:
        print('Spieler4 Gewinnt')
        print(Spieler4)
    else:
        print('Unentschieden')
    neu()

#=========================================
#Rundenmechanismus
#=========================================
def beginn():#bestimmt wer beginnt
    a=random.randint(0,4)
    if a==0:
        print('Du beginnst')
    elif a==1:
        print ('Spieler 2 beginnt')
        time.sleep(random.randint(3,6))
        bot()
        stapelpygame()
        pygame.display.flip()
        time.sleep(random.randint(3,6))
        bot2()
        stapelpygame()
        pygame.display.flip()
        time.sleep(random.randint(3,6))
        bot3()
        stapelpygame()
        pygame.display.flip()
    elif a==2:
        print('Spieler 3 beginnt')
        time.sleep(random.randint(3,6))
        bot2()
        stapelpygame()
        pygame.display.flip()
        time.sleep(random.randint(3,6))
        bot3()
        stapelpygame()
        pygame.display.flip()
    else:
        print('Spieler 4 beginnt')
        time.sleep(random.randint(3,6))
        bot3()
        stapelpygame()
        pygame.display.flip()

def runde():
    positionkarte()
    stapelpygame()
    pygame.display.flip()
    weiter = False
    while weiter ==False:
        print('Spieler1 Karten->',Spieler1) #Wiedergabe Spieler1
        print('Stappel->',Stappel)          #Wiedergabe Stappel
        print('Andere Optionen->\n neu/ Neues Spiel \n keine/ Keine Karte tauschen \n alle/ Alle Karten tauschen \n zu/ zu machen')#Mögliche Aktionen
        b=str(input('Welche Karte möchtest du aus dem Stappel tauschen?'))
        if str(b)=='neu':                   #Neues Spiel
            neu()
        if str(b)=='keine':#fals keine karte getauscht werden soll, soll nicht in die schleife gegangen werden
            weiter=True
        if str(b)=='alle':
            alle1()
            weiter=True
#--------------------------------------------------------------------
        if str(b)=='zu':#funktion zum beenden wird aufgerufen
            weiter=True
            Ende1()
#--------------------------------------------------------------------------------
        for c in range(3):                  #guckt ob sich die Eingabe in Spieler1 befindet
             if str(b)==Stappel[c]:
                Karte1tausch=Stappel[c]
                Variable1=c
                while weiter==False:
                    b=str(input('Welche Karte möchtest du von deinen Karten tauschen?'))
                    for c in range(3):
                        if str(b)==Spieler1[c]:
                            Karte2tausch=Spieler1[c]
                            Variable2=c
                            
                            Stappel[Variable1]=Karte2tausch
                            Spieler1[Variable2]= Karte1tausch
                            
                            weiter=True
    zählen()
    zählenstappel()
    positionkarte()
    pygame.display.flip()
#====================================================
    time.sleep(random.randint(3,6))
    bot()
    stapelpygame()
    pygame.display.flip()
#====================================================
    time.sleep(random.randint(3,6))
    bot2()
    stapelpygame()
    pygame.display.flip()
#====================================================
    time.sleep(random.randint(3,6))
    bot3()
    stapelpygame()
    pygame.display.flip()
#====================================================   

def stapelpygame():
    for a in range(3):
        if Stappel[a]=='Karo 7':
            screen.blit(karo7 ,  ( 100*a+20,50))
        if Stappel[a]=='Karo 8':
            screen.blit(karo8 ,  ( 100*a+20,50))
        if Stappel[a]=='Karo 9':
            screen.blit(karo9 ,  ( 100*a+20,50))
        if Stappel[a]=='Karo 10':
            screen.blit(karo10 ,  ( 100*a+20,50))
        if Stappel[a]=='Karo B':
            screen.blit(karob ,  ( 100*a+20,50))
        if Stappel[a]=='Karo D':
            screen.blit(karod ,  ( 100*a+20,50))
        if Stappel[a]=='Karo K':
            screen.blit(karok ,  ( 100*a+20,50))
        if Stappel[a]=='Karo A':
            screen.blit(karoa ,  ( 100*a+20,50))

        if Stappel[a]=='Herz 7':
            screen.blit(herz7 ,  ( 100*a+20,50))
        if Stappel[a]=='Herz 8':
            screen.blit(herz8 ,  ( 100*a+20,50))
        if Stappel[a]=='Herz 9':
            screen.blit(herz9 ,  ( 100*a+20,50))
        if Stappel[a]=='Herz 10':
            screen.blit(herz10 ,  ( 100*a+20,50))
        if Stappel[a]=='Herz B':
            screen.blit(herzb ,  ( 100*a+20,50))
        if Stappel[a]=='Herz D':
            screen.blit(herzd ,  ( 100*a+20,50))
        if Stappel[a]=='Herz K':
            screen.blit(herzk ,  ( 100*a+20,50))
        if Stappel[a]=='Herz A':
            screen.blit(herza ,  ( 100*a+20,50))

        if Stappel[a]=='Pik 7':
            screen.blit(pik7 ,  ( 100*a+20,50))
        if Stappel[a]=='Pik 8':
            screen.blit(pik8 ,  ( 100*a+20,50))
        if Stappel[a]=='Pik 9':
            screen.blit(pik9 ,  ( 100*a+20,50))
        if Stappel[a]=='Pik 10':
            screen.blit(pik10 ,  ( 100*a+20,50))
        if Stappel[a]=='Pik B':
            screen.blit(pikb ,  ( 100*a+20,50))
        if Stappel[a]=='Pik D':
            screen.blit(pikd ,  ( 100*a+20,50))
        if Stappel[a]=='Pik K':
            screen.blit(pikk ,  ( 100*a+20,50))
        if Stappel[a]=='Pik A':
            screen.blit(pika ,  ( 100*a+20,50))

        if Stappel[a]=='Kreuz 7':
            screen.blit(kreuz7 ,  ( 100*a+20,50))
        if Stappel[a]=='Kreuz 8':
            screen.blit(kreuz8 ,  ( 100*a+20,50))
        if Stappel[a]=='Kreuz 9':
            screen.blit(kreuz9 ,  ( 100*a+20,50))
        if Stappel[a]=='Kreuz 10':
            screen.blit(kreuz10 ,  ( 100*a+20,50))
        if Stappel[a]=='Kreuz B':
            screen.blit(kreuzb ,  ( 100*a+20,50))
        if Stappel[a]=='Kreuz D':
            screen.blit(kreuzd ,  ( 100*a+20,50))
        if Stappel[a]=='Kreuz K':
            screen.blit(kreuzk ,  ( 100*a+20,50))
        if Stappel[a]=='Kreuz A':
            screen.blit(kreuza ,  ( 100*a+20,50))

def positionkarte():
    for a in range(3):
        if Spieler1[a]=='Karo 7':
            screen.blit(karo7 ,  ( 100*a+20,200))
        if Spieler1[a]=='Karo 8':
            screen.blit(karo8 ,  ( 100*a+20,200))
        if Spieler1[a]=='Karo 9':
            screen.blit(karo9 ,  ( 100*a+20,200))
        if Spieler1[a]=='Karo 10':
            screen.blit(karo10 ,  ( 100*a+20,200))
        if Spieler1[a]=='Karo B':
            screen.blit(karob ,  ( 100*a+20,200))
        if Spieler1[a]=='Karo D':
            screen.blit(karod ,  ( 100*a+20,200))
        if Spieler1[a]=='Karo K':
            screen.blit(karok ,  ( 100*a+20,200))
        if Spieler1[a]=='Karo A':
            screen.blit(karoa ,  ( 100*a+20,200))

        if Spieler1[a]=='Herz 7':
            screen.blit(herz7 ,  ( 100*a+20,200))
        if Spieler1[a]=='Herz 8':
            screen.blit(herz8 ,  ( 100*a+20,200))
        if Spieler1[a]=='Herz 9':
            screen.blit(herz9 ,  ( 100*a+20,200))
        if Spieler1[a]=='Herz 10':
            screen.blit(herz10 ,  ( 100*a+20,200))
        if Spieler1[a]=='Herz B':
            screen.blit(herzb ,  ( 100*a+20,200))
        if Spieler1[a]=='Herz D':
            screen.blit(herzd ,  ( 100*a+20,200))
        if Spieler1[a]=='Herz K':
            screen.blit(herzk ,  ( 100*a+20,200))
        if Spieler1[a]=='Herz A':
            screen.blit(herza ,  ( 100*a+20,200))

        if Spieler1[a]=='Pik 7':
            screen.blit(pik7 ,  ( 100*a+20,200))
        if Spieler1[a]=='Pik 8':
            screen.blit(pik8 ,  ( 100*a+20,200))
        if Spieler1[a]=='Pik 9':
            screen.blit(pik9 ,  ( 100*a+20,200))
        if Spieler1[a]=='Pik 10':
            screen.blit(pik10 ,  ( 100*a+20,200))
        if Spieler1[a]=='Pik B':
            screen.blit(pikb ,  ( 100*a+20,200))
        if Spieler1[a]=='Pik D':
            screen.blit(pikd ,  ( 100*a+20,200))
        if Spieler1[a]=='Pik K':
            screen.blit(pikk ,  ( 100*a+20,200))
        if Spieler1[a]=='Pik A':
            screen.blit(pika ,  ( 100*a+20,200))

        if Spieler1[a]=='Kreuz 7':
            screen.blit(kreuz7 ,  ( 100*a+20,200))
        if Spieler1[a]=='Kreuz 8':
            screen.blit(kreuz8 ,  ( 100*a+20,200))
        if Spieler1[a]=='Kreuz 9':
            screen.blit(kreuz9 ,  ( 100*a+20,200))
        if Spieler1[a]=='Kreuz 10':
            screen.blit(kreuz10 ,  ( 100*a+20,200))
        if Spieler1[a]=='Kreuz B':
            screen.blit(kreuzb ,  ( 100*a+20,200))
        if Spieler1[a]=='Kreuz D':
            screen.blit(kreuzd ,  ( 100*a+20,200))
        if Spieler1[a]=='Kreuz K':
            screen.blit(kreuzk ,  ( 100*a+20,200))
        if Spieler1[a]=='Kreuz A':
            screen.blit(kreuza ,  ( 100*a+20,200))

def spiel():
    print('')
    print('----------------------------------------------')
    print('NEUES SPIEL')
    print('----------------------------------------------')
    print('EINGABE: Das Eingeben der Karte ist so ->Kreuz Bube = Kreuz B / Herz 8 = Herz 8')
    mischen()
    legen()
    beginn()
    positionkarte()
    stapelpygame()
    pygame.display.flip()
    running=True
    while running==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        runde()
    #beendet pygame
    pygame.quit()
spiel()
