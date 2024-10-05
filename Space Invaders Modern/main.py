import pygame, sys


class Game:
    def __init__(self):
        pass

    def run(self):
        pass
        # update all sprite groups
        # draw all sprite groups


if __name__ == "__main__":
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    running = True
    FPS = 60

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill((30, 30, 30))

            pygame.display.flip()
            clock.tick(FPS)

    pygame.quit()
    sys.exit()
