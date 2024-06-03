import pygame
import random
import time

WIDTH, HEIGHT = 720, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load Images
RED_SPACE_SHIP  = pygame.image.load("assets/pixel_ship_red_small.png")
GREEN_SPACE_SHIP  = pygame.image.load("assets/pixel_ship_green_small.png")
BLUE_SPACE_SHIP  = pygame.image.load("assets/pixel_ship_blue_small.png")

# Player Ship
YELLOW_SPACE_SHIP  = pygame.image.load("assets/pixel_ship_yellow.png")

# Lasers
RED_LASER = pygame.image.load("assets/pixel_laser_red.png")
BLUE_LASER = pygame.image.load("assets/pixel_laser_blue.png")
GREEN_LASER = pygame.image.load("assets/pixel_laser_green.png")
YELLOW_LASER = pygame.image.load("assets/pixel_laser_yellow.png")

# BackGround
BG = pygame.transform.scale(pygame.image.load("assets/background-black.png"), (WIDTH, HEIGHT))

def main():
    running = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        pygame.display.update()

    while running:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

    pygame.quit()

if __name__ == "__main__":
    main()
