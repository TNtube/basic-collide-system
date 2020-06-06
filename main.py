import pygame
from game import Game

pygame.init()

screen = pygame.display.set_mode((550, 350))

run = True
game = Game()

clock = pygame.time.Clock()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    game.update(screen)
    screen.blit(pygame.font.Font(None, 20).render(f"FPS : {round(clock.get_fps(), 2)}", True, (0, 255, 0)), (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
