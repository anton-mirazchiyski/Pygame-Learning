import pygame, sys
import random

pygame.init()

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (30, 144, 255)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Points Collector')
screen.fill(WHITE_COLOR)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.rect.Rect((500, 500), (40, 40))
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


while True:
    player = Player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE_COLOR)
    pygame.draw.rect(screen, BLUE_COLOR, player.rect)
    pygame.display.flip()
