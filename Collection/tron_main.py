#==========================================
# Title:  Tron
# Author: Megaterion
#==========================================

import pygame
import sys
import time

#Menu
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Tron")
surface = pygame.display.get_surface() 
WIDTH, HEIGHT = surface.get_width(), surface.get_height()
offset = 60
 
font = pygame.font.SysFont(None, 72)
lost_font = pygame.font.SysFont("comicsans", 60)


#Game
BLACK = (0, 0, 0)  
P1_COLOUR = (0, 255, 255) 
P2_COLOUR = (255, 187, 39)
P3_COLOUR = (210, 0, 3)

music = "Tron_Assets/Lightcycle_Race.mp3"
crash_sound = "Tron_Assets/Crash_sound.mp3" 
pygame.mixer.init(44100, -16, 2, 1024*4)

pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

class Player:
    def __init__(self, x, y, b, c):
        self.x = x  #x-Pos
        self.y = y  #y-Pos
        self.speed = 1  #Geschwindigkeit
        self.bearing = b  #Ausrichtung
        self.colour = c
        self.boost = False  #ist Boost aktiv
        self.start_boost = time.time()  #kontrolliert die boost dauer
        self.boosttime = 5
        self.rect = pygame.Rect(self.x - 1, self.y - 1, 2, 2) 

    def draw(self):
        self.rect = pygame.Rect(self.x - 1, self.y - 1, 2, 2)
        pygame.draw.rect(WIN, self.colour, self.rect, 0) 

    def move(self):
        if not self.boost:  #Wenn kein Boost aktiv ist
            self.x += self.bearing[0]
            self.y += self.bearing[1]
        else:               #Wenn Boost aktiv ist
            self.x += self.bearing[0] * 2
            self.y += self.bearing[1] * 2

    def booster(self):
        if self.boost == True:
            if self.boosttime > 0:
                self.start_boost = time.time()

def new_game():
    new_p1 = Player(50, HEIGHT / 2, (2, 0), P1_COLOUR)
    new_p2 = Player(WIDTH - 50, HEIGHT / 2, (-2, 0), P2_COLOUR)
    return new_p1, new_p2

                
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
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
        mainClock.tick(60)
 
def game():
    running = True

    while runnging:
        clock = pygame.time.Clock()
        check_time = time.time()

        objects = list()  #Liste mit allen Playern
        path = list()  #Liste mit allen Pfadteilen
        p1 = Player(50, (HEIGHT- offset) / 2, (2, 0), P1_COLOUR)
        p2 = Player(WIDTH - 50, (HEIGHT- offset) / 2, (-2, 0), P2_COLOUR)
        objects.append(p1)
        path.append((p1.rect, '1'))
        objects.append(p2)
        path.append((p2.rect, '2'))

        player_score = [35, 60]

        wall_rects = [pygame.Rect([0, offset, 15, HEIGHT]) , pygame.Rect([0, offset, WIDTH, 15]),\
                      pygame.Rect([WIDTH - 15, offset, 15, HEIGHT]),\
                      pygame.Rect([0, HEIGHT - 15, WIDTH, 15])]
        
        done = False
        new = False

        while not done:
            for event in pygame.event.get():  #alle events im letzten tick
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYUP:
                    #Player 1
                    if event.key == pygame.K_TAB:
                        objects[0].boost = False
                        objects[0].booster()
                    #Player 2
                    if event.key == pygame.K_TAB:
                        objects[1].boost = False
                        objects[1].booster()
                elif event.type == pygame.KEYDOWN:
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
                        objects[0].booster()
                
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
                        objects[1].booster()

                    if event.key == pygame.K_ESCAPE:
                        running = False

            WIN.fill(BLACK)  #leert das Fensteer

            for r in wall_rects: pygame.draw.rect(WIN, (42, 42, 42), r, 0)  #Mauer erzeugen

            for o in objects:
                if time.time() - o.start_boost >= o.boosttime:
                    o.boosttime =- time.time() - o.start_boost
                    o.boost = False

                if (o.rect, '1') in path or (o.rect, '2') in path \
                    or o.rect.collidelist(wall_rects) > -1:  #kollide mit einem Pfad
                       #verhindert das der Spieler mit dem eigenen gerade erstellten Pfad kollidiert
                    if (time.time() - check_time) >= 0.1:
                        check_time = time.time()

                        if o.colour == P1_COLOUR:
                            player_score[1] += 1
                            lost_label = lost_font.render("Spieler 2 gewinnt!", 1, (255,255,255))
                            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
                
                        else:
                            player_score[0] += 1
                            lost_label = lost_font.render("Spieler 1 gewinnt!", 1, (255,255,255))
                            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
                

                        new = True
                        #pygame.mixer.music.load(crash_sound)
                        #pygame.mixer.music.play()
                
                        #pygame.mixer.music.load(music)
                        #pygame.mixer.music.play()
                        new_p1, new_p2 = new_game()
                        objects = [new_p1, new_p2]
                        path = [(p1.rect, '1'), (p2.rect, '2')]
                        break
                else:
                    path.append((o.rect, '1')) if o.colour == P1_COLOUR else path.append((o.rect, '2'))

                o.draw()
                o.move()

            for r in path:
                if new is True:
                #löscht die Pfade - muss hier sein um grafikglitches zu vermeiden
                    path = []
                    new = False
                    break
                if r[1] == '1': pygame.draw.rect(WIN, P1_COLOUR, r[0], 0)
                else: pygame.draw.rect(WIN, P2_COLOUR, r[0], 0)

            #Zeigt den aktuellen score an
            score_text = font.render('{0} : {1}'.format(player_score[0], player_score[1]), 1, (255, 153, 51))
            score_text_pos = score_text.get_rect()
            score_text_pos.centerx = int(WIDTH / 2)
            score_text_pos.centery = int(offset / 2)
            WIN.blit(score_text, score_text_pos)

            pygame.display.flip()
            clock.tick(60)  # reguliert die FPS

        
        
            pygame.display.update()


def options():
    running = True
    while running:
        WIN.fill((0,0,0))
 
        draw_text('options', font, (255, 255, 255), WIN, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()
