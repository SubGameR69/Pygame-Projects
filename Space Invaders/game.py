import pygame
import random
import time

pygame.font.init()
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

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP.convert_alpha()
        self.laser_img = YELLOW_LASER.convert_alpha()
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

def main():
    running = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("BigBlueTerm437 Nerd Font", 35)

    PLAYER_VEL = 5

    clock = pygame.time.Clock()
    player = Player(WIDTH/2, HEIGHT - 150)

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, "#fdfdfd")
        level_label = main_font.render(f"Level: {level}", 1, "#fdfdfd")

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        player.draw(WIN)

        pygame.display.update()

    while running:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= 1 * PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x <= WIDTH - player.get_width():
            player.x += 1 * PLAYER_VEL
        if keys[pygame.K_UP] and player.y > 0:
            player.y -= 1 * PLAYER_VEL
        if keys[pygame.K_DOWN] and player.y <= HEIGHT  - player.get_height():
            player.y += 1 * PLAYER_VEL

    pygame.quit()

if __name__ == "__main__":
    main()
