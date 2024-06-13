import pygame
from settings import *

pygame.init()

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    WIN.fill("pink")

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()