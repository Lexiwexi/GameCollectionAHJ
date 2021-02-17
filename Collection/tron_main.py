#==========================================
# Title:  Tron
# Author: Megaterion
#==========================================

import pygame
import sys
import time
from pygame.locals import *



class Player:
    def __init__(self, pID, x, y, b, c):
        self.pID = pID
        self.x = x  #x-Pos
        self.y = y  #y-Pos
        self.speed = 1  #Geschwindigkeit
        self.bearing = b  #Ausrichtung
        self.colour = c
        self.boost = False
        self.laser = True
        self.boostlimit = 300
        self.rect = pygame.Rect(self.x - 1, self.y - 1, 2, 2)

        self.i = False
        self.j = 0
        
    def move(self):
        self.x += self.bearing[0]
        self.y += self.bearing[1]
        
    def draw(self):
        self.rect = pygame.Rect(self.x - 1, self.y - 1, 2, 2)
        pygame.draw.rect(WIN, self.colour, self.rect, 0)

    def coll(self): 
        if self.rect.collidelist(wall_rects) > -1 or self.rect.collidelist(path) > -1:
            if self.colour == P1_COLOUR:
                player_score[1] += 1
                lost_label = lost_font.render("Spieler 2 gewinnt!", 1, (255,255,255))
                WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
                
            elif self.colour == P2_COLOUR:
                player_score[0] += 1
                lost_label = lost_font.render("Spieler 1 gewinnt!", 1, (255,255,255))
                WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

            pygame.mixer.Sound.play(crash_sound)
            objects.clear()
            path.clear()
            path_colour.clear()
            pygame.display.update()
            pygame.time.wait(1500)
            summonPlayer()
        
        else:
            path.append(self.rect)
            path_colour.append(self.colour)

    def shoot(self):
        self.Laser = False
        print("shoot")

        pygame.draw.rect(WIN, LASER_COLOUR, [100, 100, 200, 200], 0)
        
        """
        if self.bearing == (0,2):                   #oben
            for p in range(len(path)):
                if: path[p] == pygame.Rect(self.x - 1, self.y - 1, 2, 2)
        elif self.bearing == (0,-2):                #unten
            
        elif self.bearing == (2,0):                 #links
            
        elif self.bearing == (-2,0):                #rechts

        """
            
        
        

def summonPlayer():
    p1 = Player('1', WIDTH/3, (HEIGHT-offset) / 2, (2, 0), P1_COLOUR)
    p2 = Player('2', (WIDTH/3)*2, (HEIGHT-offset) / 2,(-2, 0), P2_COLOUR)
    objects.append(p1)
    objects.append(p2)
                
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
def main_menu():
    pygame.mixer.music.load(menu_music)
    pygame.mixer.music.play(-1)
    
    while True:
        WIN.fill(BLACK)
        draw_text('main menu', font, (255, 255, 255), WIN, 20, 20)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(WIN, (255, 0, 0), button_1)
        pygame.draw.rect(WIN, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(FPS)
 
def game():
    running = True
    

    while running:        
        pygame.mixer.music.load(game_music)
        pygame.mixer.music.play(-1)

        game = True
        summonPlayer()

        while game:
            for event in pygame.event.get():  #alle events im letzten tick
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.KEYUP:
                    #Player 1
                    if event.key == pygame.K_TAB:
                        objects[0].boost = False
                    #Player 2
                    if event.key == pygame.K_RSHIFT:
                        objects[1].boost = False
                        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game = False
                        running = False
                        
                        pygame.mixer.music.load(menu_music)
                        pygame.mixer.music.play(-1)
                        
                    #Player 1
                    if event.key == pygame.K_w and objects[0].bearing != (0,2):
                        objects[0].bearing = (0, -2)
                    elif event.key == pygame.K_s and objects[0].bearing != (0,-2):
                        objects[0].bearing = (0, 2)
                    elif event.key == pygame.K_a and objects[0].bearing != (2,0):
                        objects[0].bearing = (-2, 0)
                    elif event.key == pygame.K_d and objects[0].bearing != (-2,0):
                        objects[0].bearing = (2, 0)
                    elif event.key == pygame.K_TAB:
                            objects[0].boost = True
                    elif event.key == pygame.K_q:
                            if objects[0].laser == True:
                                objects[0].shoot()
                                          
                    #Player 2
                    if event.key == pygame.K_UP and objects[1].bearing != (0,2):
                        objects[1].bearing = (0, -2)
                    elif event.key == pygame.K_DOWN and objects[1].bearing != (0,-2):
                        objects[1].bearing = (0, 2)
                    elif event.key == pygame.K_LEFT and objects[1].bearing != (2,0):
                        objects[1].bearing = (-2, 0)
                    elif event.key == pygame.K_RIGHT and objects[1].bearing != (-2,0):
                        objects[1].bearing = (2, 0)
                    elif event.key == pygame.K_RSHIFT:
                        objects[1].boost = True
                    elif event.key == pygame.K_q:
                            if objects[1].laser == True:
                                objects[1].shoot()
                    
            WIN.fill(BLACK)  #leert das Fensteer

            for w in wall_rects:
                pygame.draw.rect(WIN, (42, 42, 42), w, 0)  #Mauer erzeugen

            for p in range(len(path)):
                if path_colour[p] == P1_COLOUR:
                    pygame.draw.rect(WIN, P1_COLOUR, path[p], 0)
                else:
                    pygame.draw.rect(WIN, P2_COLOUR, path[p], 0)

            for o in objects:
                if o.boost == True:
                    if o.boostlimit - 1 >= 0:
                        o.boostlimit = o.boostlimit - 1
                        o.speed = 2
                    else:
                        o.boost = False
                else:
                    o.speed = 1
                    if o.j != 20:
                        o.j = o.j + 1
                    else:  
                        if o.boostlimit + 1 <= 300:
                            o.boostlimit = o.boostlimit + 1
                        o.j = 0
                        
                if o.speed == 1:
                    if o.i == True:
                        o.move()
                        o.draw()
                        o.coll()
                        o.i = False
                    else:
                        o.i = True
                elif o.speed == 2:
                    o.move()
                    o.draw()
                    o.coll()

            pygame.draw.rect(WIN, LASER_COLOUR, [100, 100, 200, 200], 0)

            #zeigt die verbleibende Boostdauer an
            boost_text = boost_font.render('{0}                           {1}'.format(objects[0].boostlimit, objects[1].boostlimit), 1, (255, 153, 51))
            boost_text_pos = boost_text.get_rect()
            boost_text_pos.centerx = int(WIDTH / 2)
            boost_text_pos.centery = int(offset / 2)
            WIN.blit(boost_text, boost_text_pos)
            
            #Zeigt den aktuellen score an
            score_text = font.render('{0} : {1}'.format(player_score[0], player_score[1]), 1, (255, 153, 51))
            score_text_pos = score_text.get_rect()
            score_text_pos.centerx = int(WIDTH / 2)
            score_text_pos.centery = int(offset / 2)
            WIN.blit(score_text, score_text_pos)

            pygame.display.flip()
            mainClock.tick(FPS)
            
        pygame.display.update()

def options():
    running = True
    while running:
        WIN.fill(BLACK)
 
        draw_text('options', font, (255, 255, 255), WIN, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(FPS)

###############
        
#Menu
click = False
mainClock = pygame.time.Clock()
FPS = 120
pygame.init()

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Tron")
surface = pygame.display.get_surface() 
WIDTH, HEIGHT = surface.get_width(), surface.get_height()
offset = 60

boost_font = pygame.font.SysFont(None, 36)
font = pygame.font.SysFont(None, 72)
lost_font = pygame.font.SysFont(None, 60)


#Game
BLACK = (0, 0, 0)
LASER_COLOUR = pygame.Color(255, 255, 255)
P1_COLOUR = (0, 255, 255) 
P2_COLOUR = (255, 187, 39)
P3_COLOUR = (210, 0, 3)

player_score = [0, 0]

path = []  #Liste mit allen Pfadteilen
path_colour = [] #Liste mit Farben der Pfadteile
objects = []  #Liste mit allen Playern
        
wall_rects = [pygame.Rect([0, offset, 15, HEIGHT]) , #links
                      pygame.Rect([0, offset, WIDTH, 15]), #oben
                      pygame.Rect([WIDTH - 15, offset, 15, HEIGHT]),#rechts
                      pygame.Rect([0, HEIGHT - 15, WIDTH, 15]) #unten
                      ]

menu_music = "Tron_Assets/Tron_menu.mp3"
game_music = "Tron_Assets/Lightcycle_Race.mp3"
crash_sound = pygame.mixer.Sound("Tron_Assets/Crash_sound.mp3")

###############
main_menu()
