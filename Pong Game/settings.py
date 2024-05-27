import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 700
SIZE = {"paddle": (40, 100), "ball": (30, 30)}
SPEED = {"player": 500, "opponent": 250, "ball": 450}
COLORS = {
    "paddle": "#ee322c",
    "paddle shadow": "#b12521",
    "ball": "#ee622c",
    "ball shadow": "#c14f24",
    "bg": "#002633"
}