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

food_rect = None

while running:
    if begin:
        begin = False
        time = 0
        snake_rect = pygame.rect.Rect(randrange(0, SCREEN_SIZE, SNAKE_PART_SIZE),
                                      randrange(0, SCREEN_SIZE, SNAKE_PART_SIZE),
                                      SNAKE_PART_SIZE,
                                      SNAKE_PART_SIZE)
        snake_length = 1
        snake_parts = []
        snake_direction = pygame.math.Vector2(0, 0)

    if bait:
        bait = False
        food_rect = pygame.rect.Rect(randrange(0, SCREEN_SIZE, FOOD_SIZE),
                                     randrange(0, SCREEN_SIZE, FOOD_SIZE),
                                     FOOD_SIZE,
                                     FOOD_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake_direction[1] > 0:
                snake_direction = pygame.math.Vector2(0, -SNAKE_MOVE_LENGTH)
            if event.key == pygame.K_DOWN and not snake_direction[1] < 0:
                snake_direction = pygame.math.Vector2(0, SNAKE_MOVE_LENGTH)
            if event.key == pygame.K_RIGHT and not snake_direction[0] < 0:
                snake_direction = pygame.math.Vector2(SNAKE_MOVE_LENGTH, 0)
            if event.key == pygame.K_LEFT and not snake_direction[0] > 0:
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

    pygame.draw.rect(screen, FOOD_COLOR, food_rect, 0, 10)
    [pygame.draw.rect(screen, SNAKE_COLOR, snake_part, 8, 4) for snake_part in snake_parts]

    if snake_rect.left < 0 or snake_rect.right > SCREEN_SIZE or snake_rect.top < 0 or snake_rect.bottom > SCREEN_SIZE:
        begin = True

    for part in snake_parts[:-1]:
        if snake_rect.colliderect(part):
            begin = True
            break

    if snake_rect.colliderect(food_rect):
        snake_length += 1
        bait = True

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
