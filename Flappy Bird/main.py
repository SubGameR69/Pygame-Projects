import pygame

from settings import *
import assets
from objects.bird import Bird
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

Background(0, sprites)
Background(1, sprites)


Floor(0, sprites)
Floor(1, sprites)

bird = Bird(sprites)

pygame.time.set_timer(column_create_event, 2400)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
        if event.type == column_create_event:
            Column(sprites)
        bird.movement(event)

    WIN.fill("pink")

    sprites.draw(WIN)
    sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()