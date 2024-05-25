import sys
import pygame

import random

pygame.init()

clock = pygame.time.Clock()

WHITE_COLOR = (255, 255, 255)
LIGHT_YELLOW = (255, 255, 224)
BLUE_COLOR = (30, 144, 255)
RED_COLOR = (205, 92, 92)
GREEN_COLOR = (8, 143, 143)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Points Collector')
screen.fill(LIGHT_YELLOW)

score_font = pygame.font.SysFont('arial', 24)
game_over_font = pygame.font.SysFont('arial', 40)

player_running_images = [
    pygame.image.load('Run (1).png').convert_alpha(),
    pygame.image.load('Run (2).png').convert_alpha(),
    pygame.image.load('Run (3).png').convert_alpha(),
    pygame.image.load('Run (4).png').convert_alpha(),
]

dinosaur_walking_images = [
    pygame.image.load('images/dino_sprite/walking/Walk (1).png').convert_alpha(),
    pygame.image.load('images/dino_sprite/walking/Walk (2).png').convert_alpha(),
    pygame.image.load('images/dino_sprite/walking/Walk (3).png').convert_alpha(),
    pygame.image.load('images/dino_sprite/walking/Walk (4).png').convert_alpha(),
    pygame.image.load('images/dino_sprite/walking/Walk (5).png').convert_alpha(),
    pygame.image.load('images/dino_sprite/walking/Walk (6).png').convert_alpha(),
    pygame.image.load('images/dino_sprite/walking/Walk (7).png').convert_alpha(),
    pygame.image.load('images/dino_sprite/walking/Walk (8).png').convert_alpha(),
    pygame.image.load('images/dino_sprite/walking/Walk (9).png').convert_alpha(),
    pygame.image.load('images/dino_sprite/walking/Walk (10).png').convert_alpha(),
]


class Player(pygame.sprite.Sprite):
    SIZE = (140, 140)
    MOVING = False
    MOVEMENT_VAR = 0

    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('Idle (6).png').convert_alpha()
        self.surf.set_colorkey(LIGHT_YELLOW)
        self.surf = pygame.transform.smoothscale(self.surf, self.SIZE)
        self.rect = self.surf.get_rect(center=(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        ))
        self.score = 0

    def move(self):
        pygame.mouse.set_visible(False)

        if self.MOVEMENT_VAR >= len(player_running_images):
            self.MOVEMENT_VAR = 0
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.center = (mouse_x, mouse_y)
        self.surf = player_running_images[self.MOVEMENT_VAR]
        self.surf = pygame.transform.smoothscale(self.surf, self. SIZE)
        self.MOVEMENT_VAR += 1


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


class Obstacle(pygame.sprite.Sprite):
    SIZE = (100, 90)
    MOVEMENT_VAR = 0

    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('images/dino_sprite/walking/Walk (1).png').convert_alpha()
        self.surf.set_colorkey(LIGHT_YELLOW)
        self.surf = pygame.transform.smoothscale(self.surf, self.SIZE)
        self.rect = self.surf.get_rect(center=(
            30, random.randint(10, SCREEN_HEIGHT - 10)
        ))

    def update(self):
        self.rect.move_ip(4, 0)

        if self.MOVEMENT_VAR >= len(dinosaur_walking_images):
            self.MOVEMENT_VAR = 0
        image = dinosaur_walking_images[self.MOVEMENT_VAR]
        image = pygame.transform.smoothscale(image, self.SIZE)
        self.surf = image
        self.MOVEMENT_VAR += 1


def out_of_screen(group):
    for member in group:
        if member.rect.x > SCREEN_WIDTH:
            member.kill()
            return True


player = Player()
points = [Point() for i in range(10)]

obstacles = pygame.sprite.Group()


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            player.move()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill(LIGHT_YELLOW)
    player_score = score_font.render(f'Your score: {player.score}', True, GREEN_COLOR)

    if len(obstacles) < 3 or (out_of_screen(obstacles) and len(obstacles) < 3):
        obstacle = Obstacle()
        obstacles.add(obstacle)
    obstacles.update()

    for point in points:
        point.draw()
        if pygame.Rect.colliderect(player.rect, point.rect):
            player.score += 1
            points.remove(point)

    if pygame.sprite.spritecollideany(player, obstacles):
        screen.fill((0, 0, 0))
        game_over = game_over_font.render('You were hit. Game over!', True, GREEN_COLOR)
        screen.blit(game_over, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    screen.blit(player.surf, player.rect)
    for obstacle in obstacles:
        screen.blit(obstacle.surf, obstacle.rect)
    screen.blit(player_score, (40, 40))
    pygame.display.flip()
    clock.tick(20)
