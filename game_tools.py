from xmlrpc.client import Boolean
import pygame
from pygame.locals import *
import time


class GameObject:
    # Flip should be true or false
    def __init__(self, image_path=None, color=(50, 220, 50), size=(100, 100), flip=None):
        self.color = color
        self.flip = flip
        self.show_flipped = False

        self.x = 0 
        self.y = 0

        self.w = size[0]
        self.h = size[1]

        # velocity
        self.vel_x = 0
        self.vel_y = 0

        if (image_path):
            image_rect = pygame.image.load(image_path)
            image_rect = pygame.transform.scale(image_rect, size)
            image_flipped = pygame.transform.flip(image_rect, True, False)

            self.image = image_rect
            self.image_flipped = image_flipped


    def render(self, screen):
        if (self.image and not self.show_flipped):
            screen.blit(self.image, (self.x, self.y))
        elif (self.image and self.show_flipped):
            screen.blit(self.image_flipped, (self.x, self.y))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

    def update(self, dt):
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

        if (self.flip is not None):
            if (self.vel_x > 0):
                self.show_flipped = self.flip
            elif (self.vel_x < 0):
                self.show_flipped = not self.flip

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_velocity(self, vel_x = None, vel_y = None):
        if (vel_x is not None):
            self.vel_x = vel_x
        if (vel_y is not None):
            self.vel_y = vel_y

    def accelerate(self, x, y, dt):
        self.vel_x += x * dt
        self.vel_y += y * dt

    def get_box(self):
        return pygame.Rect((self.x, self.y, self.w, self.h))