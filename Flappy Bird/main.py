import pygame

from settings import *
import assets
from objects.bird import Bird
from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.game_start_msg import GameStartMessage
from objects.game_over_msg import GameOverMessage

pygame.init()

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT

run = True
gameover = False
gamestarted = False
score = 0

assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates()


def create_sprites():
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameStartMessage(sprites)


bird, game_start_msg = create_sprites()



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                gamestarted = True
                game_start_msg.kill()
                pygame.time.set_timer(column_create_event, 1500)

            if event.key == pygame.K_ESCAPE and gameover:
                gameover = False
                gamestarted = False
                sprites.empty()
                bird, game_start_msg = create_sprites()

        if event.type == column_create_event:
            Column(sprites)
        bird.movement(event)

    sprites.draw(WIN)

    if not gameover and gamestarted:
        sprites.update()

    if bird.check_collision(sprites):
        gameover = True
        gamestarted = False
        GameOverMessage(sprites)

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score += 1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
