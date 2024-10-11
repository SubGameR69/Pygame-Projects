import pygame, sys
from fighter import Fighter

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Fighter")
clock = pygame.time.Clock()

bg_img = pygame.image.load("./assets/images/background/background.jpg").convert_alpha()

fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)


def draw_bg():
    new_bg = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(new_bg, (0, 0))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    draw_bg()
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    fighter_1.move(SCREEN_WIDTH)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
