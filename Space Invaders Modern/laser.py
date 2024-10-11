import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, constraint):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill("white")
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.max_h = constraint

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.max_h + 50:
            self.kill()

    def update(self):
        self.rect.y += self.speed
        self.destroy()

# END OF THE GAME
