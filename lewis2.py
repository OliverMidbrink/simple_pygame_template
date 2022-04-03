import sys
import pygame
from pygame.locals import *
import time
from game_tools import GameObject

pygame.init()
fps=60
fpsclock=pygame.time.Clock()

width, height = 800, 500
screen = pygame.display.set_mode((width, height))

w, h = 217, 217

bild1 = pygame.image.load("spindash.png")
bild1 = pygame.transform.scale(bild1, (w, h))


x, y = 1, 1
speed = 3
pygame.font.init()

font = pygame.font.SysFont("Tinos", 35)

victory = font.render("Victory", True, (0, 255, 0))
defeat = font.render("Defeat", True, (255, 0, 0))


stuck = False
timer = 5
starttime = time.time()
gamefinished = False
won = False

## ================= NEW STUFF =========================
character = GameObject("sonic_side.png", size=(100, 100), flip=False)
character.set_position(x=width/2, y=height/2)

world_x, world_y = 0, 0

dt = 0

def win(screen):
    gamefinished = True
    won = True
    screen.blit(victory, (200, 25))

def loose(screen):
    gamefinished = True
    screen.blit(defeat, (200, 25))


ground = GameObject()
ground.set_position(x=width/2, y=height/2 - 100)

box = GameObject()
box.set_position(x=width/2 + 100, y=height/2)


objects = [ground, box]
bounding_boxes = [ground.get_box, box.get_box]



while True:
    ##¤ ============================ GRAPHICS ======================================
    screen.fill((255, 255, 255))
    

    if not gamefinished:
        time_remaining_string = str(round(timer - (time.time() - starttime)))
        timer_bild = font.render(time_remaining_string, True, (255, 0, 0))
        screen.blit(timer_bild, (300, 35))


    if time.time() - starttime > timer:
        stuck = True
        gamefinished = True

        if not won:
            loose(screen)

    character.render(screen)


    pygame.display.flip()
    fpsclock.tick()

    dt = fpsclock.tick(fps) / 1000

    time.sleep(0.01)

    ### ======================== GAME LOGIC ==============================

    keys = pygame.key.get_pressed()

    character.set_velocity(vel_x=0) 

    if ((character.x + character.w / 2 - width / 2) < width / 4 and keys[pygame.K_RIGHT]):
        # character is on the left side
        character.set_velocity(vel_x=500)
    
    if ((character.x + character.w / 2 - width / 2) > - width / 4 and keys[pygame.K_LEFT]):
        # character is on the right side
        character.set_velocity(vel_x=-500)   

    
    ### Collision deteciton

    #for index in 


    character.update(dt)

    # QUIT text
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

