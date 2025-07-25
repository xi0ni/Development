import pygame
from constants import RED, BLACK,WHITE

class Bowling_ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = 40
        height = 60
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.circle(self.image, WHITE, (width // 2, height // 2), 20)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y