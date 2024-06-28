import pygame
from random import randint

# General Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

running = True

player_surf = pygame.image.load("assets/images/player.png").convert_alpha()
star_surf = pygame.image.load("assets/images/star.png").convert_alpha()

star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # draw the game
    display_surface.fill("darkgray")
    for pos in star_position:
        display_surface.blit(star_surf, pos)
    display_surface.blit(player_surf, (200, 200))
    pygame.display.update()

pygame.quit()
