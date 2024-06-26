import os
import pygame

sprites = {}
sounds = {}


def load_sprites():
    path = os.path.join("assets", "sprites")
    for file in os.listdir(path):
        sprites[file.split(".")[0]] = pygame.image.load(os.path.join(path, file))


def get_sprite(name):
    return sprites[name]


def load_sounds():
    path = os.path.join("assets", "audios")
    for file in os.listdir(path):
        sounds[file.split(".")[0]] = pygame.mixer.Sound(os.path.join(path, file))


def play_sound(name):
    sounds[name].play()
