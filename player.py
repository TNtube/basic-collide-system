import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 150
        self.velocity = 5

    def blit(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[K_RIGHT] - keys[K_LEFT]) * self.velocity
        self.rect.y += (keys[K_DOWN] - keys[K_UP]) * self.velocity
