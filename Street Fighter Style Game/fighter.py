import pygame


class Fighter:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 180)

    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect)