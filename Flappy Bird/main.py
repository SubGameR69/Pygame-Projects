import pygame

from settings import *
import assets
from objects.background import Background
from objects.floor import Floor
from objects.column import Column


pygame.init()

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT

run = True

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()

Background(sprites, index=0)
Background(sprites, index=1)

Floor(0, sprites)
Floor(1, sprites)

pygame.time.set_timer(column_create_event, 2400)

Column(sprites)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        if event.type == column_create_event:
            Column(sprites)

    WIN.fill("pink")

    sprites.draw(WIN)
    sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()