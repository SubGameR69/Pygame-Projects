import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def update(self, dt):
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt


class Star(pygame.sprite.Sprite):
    def __init__(self, *groups, surf):
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_rect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))


# General Setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
FPS = 60

all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load("assets/images/star.png").convert_alpha()
for _ in range(20):
    Star(all_sprites, surf=star_surf)
player = Player(all_sprites)

running = True

meteor_surf = pygame.image.load("assets/images/meteor.png").convert_alpha()
meteor_rect = meteor_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load("assets/images/laser.png")
laser_rect = laser_surf.get_rect(bottomleft=(20, WINDOW_HEIGHT - 20))

while running:
    dt = clock.tick(FPS) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("fire laser")

    keys = pygame.key.get_pressed()
    player.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    all_sprites.update(dt)

    # draw the game
    display_surface.fill("darkgray")
    all_sprites.draw(display_surface)

    # Player Movement
    pygame.display.update()

pygame.quit()
