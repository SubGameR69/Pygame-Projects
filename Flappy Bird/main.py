import pygame

from settings import *
import assets
from objects.bird import Bird
from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.game_start_msg import GameStartMessage
from objects.game_over_msg import GameOverMessage
from objects.score import Score

pygame.init()

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT

run = True
gameover = False
gamestarted = False


assets.load_sprites()
assets.load_sounds()

sprites = pygame.sprite.LayeredUpdates()


def create_sprites():
    Background(0, sprites)
    Background(1, sprites)
    Floor(0, sprites)
    Floor(1, sprites)

    return Bird(sprites), GameStartMessage(sprites), Score(sprites)


bird, game_start_msg, score = create_sprites()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == column_create_event:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                gamestarted = True
                game_start_msg.kill()
                pygame.time.set_timer(column_create_event, 1500)

            if event.key == pygame.K_ESCAPE and gameover:
                gameover = False
                gamestarted = False
                sprites.empty()
                bird, game_start_msg, score = create_sprites()

        bird.movement(event)

    sprites.draw(WIN)

    if not gameover and gamestarted:
        sprites.update()

    if bird.check_collision(sprites) and not gameover:
        gameover = True
        gamestarted = False
        GameOverMessage(sprites)
        pygame.time.set_timer(column_create_event, 0)
        assets.play_sound("hit")

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1
            assets.play_sound("point")

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
