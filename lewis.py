import sys
import pygame
from pygame.locals import *
import time

pygame.init()
fps=60
fpsclock=pygame.time.Clock()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

w, h = 217, 217

bild1 = pygame.image.load("spindash.png")
bild1 = pygame.transform.scale(bild1, (w, h))

"""up = 234234
down = 234234
right = 2134234
left = 234234234"""

x, y = 1, 1
speed = 3
pygame.font.init()

font = pygame.font.SysFont("Tinos", 35)

victory = font.render("Victory", True, (0, 255, 0))
defeat = font.render("Defeat", True, (255, 0, 0))


stuck = False
timer = 5
starttime = time.time()
gameover = False
won = False

while True:
    screen.fill((255, 255, 255))    # !!
    
    #screen.fill((0, 0, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    pygame.draw.circle(screen, (0,0,0), (250, 250), 100)
    screen.blit(bild1, (x,y))

    tolerance = 10
    if abs(x - 250 + w / 2) < tolerance and abs(y - 250 + h / 2) < tolerance:
        screen.blit(victory, (200, 25))
        stuck = True
        won = True
        gameover = True

    #w = 30

    if not gameover:
        time_remaining_string = str(round(timer - (time.time() - starttime)))
        timer_bild = font.render(time_remaining_string, True, (255, 0, 0))
        screen.blit(timer_bild, (300, 35))


    if time.time() - starttime > timer:
        stuck = True
        gameover=True

        if not won:
            screen.blit(defeat, (200, 25))


    pygame.display.flip()
    fpsclock.tick()

    time.sleep(0.01)

    #x+=0
    #y+=0

    if not stuck:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            y -= speed
        if keys[pygame.K_DOWN]:
            y += speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_LEFT]:
            x -= speed

