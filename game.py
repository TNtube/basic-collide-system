from player import Player
from wall import Wall
from collision import Collide
import pygame

level = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
         [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
         [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
         [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
         [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
         [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class Game:
    def __init__(self):
        self.player = Player()
        self.blocks = pygame.sprite.Group()
        self.collide = Collide()
        for i, line in enumerate(level):
            for j, case in enumerate(line):
                if case:
                    self.blocks.add(Wall((j * 50, i * 50)))

    def update(self, screen):
        screen.fill((255, 255, 255))
        self.collide.collision(self.player, self.blocks)
        self.player.blit(screen)
        self.blocks.draw(screen)
        for i in self.blocks:
            i.move()
