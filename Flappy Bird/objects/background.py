import pygame
import assets


class Background(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(0, 0))
        super().__init__(*groups)
