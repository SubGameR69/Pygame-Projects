import pygame

import assets
from layer import Layer
from settings import *


class GameStartMessage(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self._layer = Layer.UI
        self.image = assets.get_sprite("message")
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        super().__init__(*groups)