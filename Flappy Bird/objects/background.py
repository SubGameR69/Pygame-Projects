import pygame
import assets
import settings


class Background(pygame.sprite.Sprite):
    def __init__(self, *groups, index):
        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(settings.SCREEN_WIDTH * index, 0))
        super().__init__(*groups)

    def update(self):
        self.rect.x -= 1

        if self.rect.right <= 0:
            self.rect.x = settings.SCREEN_WIDTH
