import pygame
import assets
from layer import Layer

from settings import *


class Floor(pygame.sprite.Sprite):
    def __init__(self, index, *groups):
        self._layer = Layer.FLOOR
        self.image = assets.get_sprite("floor")
        self.rect = self.image.get_rect(topleft=(SCREEN_WIDTH * index, SCREEN_HEIGHT - self.image.get_height()))
        self.mask = pygame.mask.from_surface(self.image)
        super().__init__(*groups)

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.rect.x = SCREEN_WIDTH
