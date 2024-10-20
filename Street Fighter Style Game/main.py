import pygame, sys
from fighter import Fighter
from pygame import mixer

pygame.init()
mixer.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Fighter")
clock = pygame.time.Clock()

bg_img = pygame.image.load("./assets/images/background/background.jpg").convert_alpha()

victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

mixer.music.load("assets/audio/music.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1, 0.0, 3000)

sword_fx = mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(0.5)

intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False
ROUND_OVER_COOLDOWN = 2000

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

count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


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

    if intro_count <= 0:
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2, round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1, round_over)
    else:
        draw_text(str(intro_count), count_font, "red", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()

    if not round_over:
        if not fighter_1.alive:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif not fighter_2.alive:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
            fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
    
    draw_healthbar(fighter_1.health, 20, 20)
    draw_healthbar(fighter_2.health, 580, 20)

    draw_text("P1: " + str(score[0]), score_font, "red", 20, 60)
    draw_text("P2: " + str(score[1]), score_font, "red", 580, 60)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
