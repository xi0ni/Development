import pygame
from main import *


class bowling_ball():
    def __init__(self):
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

