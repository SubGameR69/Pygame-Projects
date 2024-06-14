import pygame

from objects.background import Background
from settings import *
import assets


pygame.init()

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

run = True

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

Background(sprites)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    WIN.fill("pink")

    sprites.draw(WIN)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()