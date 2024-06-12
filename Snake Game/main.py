import pygame
from config import *
from random import randrange

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Snake Game")

running = True
begin = True
bait = True

clock = pygame.time.Clock()

time = None

snake_rect = None
snake_length = None
snake_parts = None
snake_direction = None
ran_snake_pos = randrange(0, SCREEN_SIZE, SNAKE_PART_SIZE)
ran_food_pos = randrange(0, SCREEN_SIZE, SNAKE_PART_SIZE)

food_rect = None

while running:
    if begin:
        begin = False
        time = 0
        snake_rect = pygame.rect.Rect(ran_snake_pos, ran_snake_pos, SNAKE_PART_SIZE, SNAKE_PART_SIZE)
        snake_length = 1
        snake_parts = []
        snake_direction = pygame.math.Vector2(0, 0)

    if bait:
        bait = False
        food_rect = pygame.rect.Rect(ran_food_pos, ran_food_pos, FOOD_SIZE, FOOD_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_direction = pygame.math.Vector2(0, -SNAKE_MOVE_LENGTH)
            if event.key == pygame.K_DOWN:
                snake_direction = pygame.math.Vector2(0, SNAKE_MOVE_LENGTH)
            if event.key == pygame.K_RIGHT:
                snake_direction = pygame.math.Vector2(SNAKE_MOVE_LENGTH, 0)
            if event.key == pygame.K_LEFT:
                snake_direction = pygame.math.Vector2(-SNAKE_MOVE_LENGTH, 0)

    screen.fill(BG_COLOR)

    time_now = pygame.time.get_ticks()

    for i in range(0, SCREEN_SIZE, GRID_CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (i, 0), (i, SCREEN_SIZE))
        pygame.draw.line(screen, GRID_COLOR, (0, i), (SCREEN_SIZE, i))

    if time_now - time > DELAY:
        time = time_now
        snake_rect.move_ip(snake_direction)
        snake_parts.append(snake_rect.copy())
        snake_parts = snake_parts[-snake_length:]

    pygame.draw.rect(screen, FOOD_COLOR, food_rect)
    [pygame.draw.rect(screen, SNAKE_COLOR, snake_part) for snake_part in snake_parts]

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
