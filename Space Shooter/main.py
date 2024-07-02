import pygame
from random import randint

# General Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
FPS = 60

running = True

player_surf = pygame.image.load("assets/images/player.png").convert_alpha()
player_rect = player_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = -1
player_speed = 5

star_surf = pygame.image.load("assets/images/star.png").convert_alpha()
star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]

meteor_surf = pygame.image.load("assets/images/meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load("assets/images/laser.png")
laser_rect = laser_surf.get_rect(bottomleft=(20, WINDOW_HEIGHT - 20))

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    # draw the game
    display_surface.fill("darkgray")
    for pos in star_position:
        display_surface.blit(star_surf, pos)
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    display_surface.blit(player_surf, player_rect)

    # Player Movement
    player_rect.x += player_direction * player_speed
    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction *= -1
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
