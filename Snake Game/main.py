import pygame
from config import *

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Snake Game")

running = True
begin = True
clock = pygame.time.Clock()

snake_rect = None
snake_length = None
snake_parts = None
snake_direction = None

while running:
    if begin:
        begin = False
        snake_rect = pygame.rect.Rect(200, 200, SNAKE_PART_SIZE, SNAKE_PART_SIZE)
        snake_length = 1
        snake_parts = [snake_rect]
        snake_direction = pygame.math.Vector2()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill(BG_COLOR)

    for i in range(0, SCREEN_SIZE, GRID_CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (i, 0), (i, SCREEN_SIZE))
        pygame.draw.line(screen, GRID_COLOR, (0, i), (SCREEN_SIZE, i))

    [pygame.draw.rect(screen, "red", snake_part) for snake_part in snake_parts]

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
