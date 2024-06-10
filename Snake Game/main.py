import pygame
from config import *

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Snake Game")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill(BG_COLOR)

    for i in range(0, SCREEN_SIZE, GRID_CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (i, 0), (i, SCREEN_SIZE))
        pygame.draw.line(screen, GRID_COLOR, (0, i), (SCREEN_SIZE, i))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
