import pygame, sys
import random

pygame.init()

clock = pygame.time.Clock()

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (30, 144, 255)
RED_COLOR = (205, 92, 92)

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

    pygame.draw.rect(screen, BLUE_COLOR, player.rect)
    for point in points:
        pygame.draw.circle(screen, RED_COLOR, point.center, point.radius)
        # if pygame.sprite.collide_circle(player, point):
        #     points.remove(point)

    pygame.display.flip()
    clock.tick(20)
