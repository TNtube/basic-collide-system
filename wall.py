import pygame
from pygame.locals import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, coord):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coord
        self.velocity = 5

    def move(self):
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[K_RIGHT] - keys[K_LEFT]) * -self.velocity
        self.rect.y += (keys[K_DOWN] - keys[K_UP]) * -self.velocity
