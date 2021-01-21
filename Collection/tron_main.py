import pygame
import time
pygame.init()

BLACK = (0, 0, 0)  
P1_COLOUR = (0, 255, 255) 
P2_COLOUR = (255, 0, 255) 


class Player:
    def __init__(self, x, y, b, c):
        self.x = x  #x-Pos
        self.y = y  #y-Pos
        self.speed = 1  #Geschwindigkeit
        self.bearing = b  #Ausrichtung
        self.colour = c
        self.boost = False  #ist Boost aktiv
        self.start_boost = time.time()  #kontrolliert die boost dauer
        self.boosts = 3
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

    def boost(self):
        if self.boosts > 0:
            self.boosts -= 1
            self.boost = True
            self.start_boost = time.time()


def new_game():
    new_p1 = Player(50, HEIGHT / 2, (2, 0), P1_COLOUR)
    new_p2 = Player(WIDTH - 50, HEIGHT / 2, (-2, 0), P2_COLOUR)
    return new_p1, new_p2


WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Tron")

surface = pygame.display.get_surface() 
WIDTH, HEIGHT = surface.get_width(), surface.get_height()

offset = 60

font = pygame.font.Font(None, 72)

clock = pygame.time.Clock()  # used to regulate FPS
check_time = time.time()  # used to check collisions with rects

objects = list()  # list of all the player objects
path = list()  # list of all the path rects in the game
p1 = Player(50, (HEIGHT- offset) / 2, (2, 0), P1_COLOUR)  # creates player
p2 = Player(WIDTH - 50, (HEIGHT- offset) / 2, (-2, 0), P2_COLOUR)
objects.append(p1)
path.append((p1.rect, '1'))
objects.append(p2)
path.append((p2.rect, '2'))

player_score = [0, 0]  # current player score

wall_rects = [pygame.Rect([0, offset, 15, HEIGHT]) , pygame.Rect([0, offset, WIDTH, 15]),\
              pygame.Rect([WIDTH - 15, offset, 15, HEIGHT]),\
              pygame.Rect([0, HEIGHT - 15, WIDTH, 15])]  # outer walls of window

done = False
new = False

while not done:
    for event in pygame.event.get():  # gets all event in last tick
        if event.type == pygame.QUIT:  # close button pressed
            done = True
        elif event.type == pygame.KEYDOWN:  # keyboard key pressed
            # === Player 1 === #
            if event.key == pygame.K_w and objects[0].bearing != (0,2):
                objects[0].bearing = (0, -2)
            elif event.key == pygame.K_s and objects[0].bearing != (0,-2):
                objects[0].bearing = (0, 2)
            elif event.key == pygame.K_a and objects[0].bearing != (2,0):
                objects[0].bearing = (-2, 0)
            elif event.key == pygame.K_d and objects[0].bearing != (-2,0):
                objects[0].bearing = (2, 0)
            elif event.key == pygame.K_TAB:
                objects[0].boost()
            # === Player 2 === #
            if event.key == pygame.K_UP and objects[1].bearing != (0,2):
                objects[1].bearing = (0, -2)
            elif event.key == pygame.K_DOWN and objects[1].bearing != (0,-2):
                objects[1].bearing = (0, 2)
            elif event.key == pygame.K_LEFT and objects[1].bearing != (2,0):
                objects[1].bearing = (-2, 0)
            elif event.key == pygame.K_RIGHT and objects[1].bearing != (-2,0):
                objects[1].bearing = (2, 0)
            elif event.key == pygame.K_RSHIFT:
                objects[1].boost()

            if event.key == pygame.K_ESCAPE:
               pygame.quit()

    WIN.fill(BLACK)  # clears the WIN

    for r in wall_rects: pygame.draw.rect(WIN, (42, 42, 42), r, 0)  # draws the walls

    for o in objects:
        if time.time() - o.start_boost >= 0.5:  # limits boost to 0.5s
            o.boost = False

        if (o.rect, '1') in path or (o.rect, '2') in path \
           or o.rect.collidelist(wall_rects) > -1:  # collided with path or wall
            # prevent player from hitting the path they just made
            if (time.time() - check_time) >= 0.1:
                check_time = time.time()

                if o.colour == P1_COLOUR:
                    player_score[1] += 1
                else: player_score[0] += 1

                new = True
                new_p1, new_p2 = new_game()
                objects = [new_p1, new_p2]
                path = [(p1.rect, '1'), (p2.rect, '2')]
                break
        else:  # not yet traversed
            path.append((o.rect, '1')) if o.colour == P1_COLOUR else path.append((o.rect, '2'))

        o.draw()
        o.move()

    for r in path:
        if new is True:
        # empties the path - needs to be here to prevent graphical glitches
            path = []
            new = False
            break
        if r[1] == '1': pygame.draw.rect(WIN, P1_COLOUR, r[0], 0)
        else: pygame.draw.rect(WIN, P2_COLOUR, r[0], 0)

    # display the current score on the WIN
    score_text = font.render('{0} : {1}'.format(player_score[0], player_score[1]), 1, (255, 153, 51))
    score_text_pos = score_text.get_rect()
    score_text_pos.centerx = int(WIDTH / 2)
    score_text_pos.centery = int(offset / 2)
    WIN.blit(score_text, score_text_pos)

    pygame.display.flip()  # flips display
    clock.tick(60)  # regulates FPS

pygame.quit()
