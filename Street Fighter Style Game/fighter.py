import pygame


class Fighter:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 180)

    def move(self, screen_width):
        speed = 10

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x += -speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += speed

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= screen_width:
            self.rect.right = screen_width

    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect)