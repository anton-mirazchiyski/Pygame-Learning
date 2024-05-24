import sys
import pygame

import random

pygame.init()

clock = pygame.time.Clock()

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (30, 144, 255)
RED_COLOR = (205, 92, 92)
GREEN_COLOR = (8, 143, 143)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Points Collector')
screen.fill(WHITE_COLOR)

score_font = pygame.font.SysFont('arial', 24)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.rect.Rect((500, 500), (40, 40))
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.score = 0

    def move(self):
        pygame.mouse.set_visible(False)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.center = (mouse_x, mouse_y)


class Point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.center = (
            random.randint(10, SCREEN_WIDTH - 10),
            random.randint(10, SCREEN_HEIGHT - 10)
        )
        self.radius = 10
        self.rect = self.draw()

    def draw(self):
        circle_rect = pygame.draw.circle(screen, RED_COLOR, self.center, self.radius)
        return circle_rect


player = Player()
points = [Point() for i in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            player.move()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill(WHITE_COLOR)

    player_score = score_font.render(f'Your score: {player.score}', True, GREEN_COLOR)
    pygame.draw.rect(screen, BLUE_COLOR, player.rect)

    for point in points:
        point.draw()
        if pygame.Rect.colliderect(player.rect, point.rect):
            player.score += 1
            points.remove(point)

    screen.blit(player_score, (40, 40))
    pygame.display.flip()
    clock.tick(20)
