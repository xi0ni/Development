import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
done = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
