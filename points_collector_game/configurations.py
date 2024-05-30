import pygame

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

pygame.mouse.set_visible(False)

score_font = pygame.font.SysFont('arial', 24)
player_health_font = pygame.font.SysFont('cambria', 24)
game_over_font = pygame.font.SysFont('arial', 40)

player_running_images = [
    pygame.image.load('images/redhat_boy_sprite/running/Run (1).png').convert_alpha(),
    pygame.image.load('images/redhat_boy_sprite/running/Run (2).png').convert_alpha(),
    pygame.image.load('images/redhat_boy_sprite/running/Run (3).png').convert_alpha(),
    pygame.image.load('images/redhat_boy_sprite/running/Run (4).png').convert_alpha(),
]

dinosaur_walking_images = [
    pygame.image.load(f'images/dino_sprite/walking/Walk ({number}).png').convert_alpha() for number in range(1, 10 + 1)
]
