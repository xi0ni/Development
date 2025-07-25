import pygame
from bowling_ball import Bowling_ball
from constants import BLUE


SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

pygame.init()
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

ball = Bowling_ball()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLUE)
    ball.draw(screen)
    pygame.display.flip()
    ball.move(400, 500)


pygame.quit()
