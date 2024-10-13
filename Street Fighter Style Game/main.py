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

WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

warrior_sheet = pygame.image.load("./assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("./assets/images/wizard/Sprites/wizard.png").convert_alpha()

WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

fighter_1 = Fighter(200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS)
fighter_2 = Fighter(700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS)


def draw_bg():
    new_bg = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(new_bg, (0, 0))


def draw_healthbar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, "white", (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, "red", (x, y, 400, 30))
    pygame.draw.rect(screen, "yellow", (x, y, 400 * ratio, 30))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    draw_bg()
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    fighter_1.update()
    fighter_2.update()

    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    
    draw_healthbar(fighter_1.health, 20, 20)
    draw_healthbar(fighter_2.health, 580, 20)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
