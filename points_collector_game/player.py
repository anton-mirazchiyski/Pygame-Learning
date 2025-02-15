import pygame

from points_collector_game.configurations import LIGHT_YELLOW, SCREEN_WIDTH, SCREEN_HEIGHT, player_running_images, \
    player_idle_images
from points_collector_game.points import SuperPoint


class Player(pygame.sprite.Sprite):
    SIZE = (140, 140)
    MAX_HEALTH = 100
    IDLE_VAR = 0
    MOVEMENT_VAR = 0

    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('images/redhat_boy_sprite/idle/Idle (6).png').convert_alpha()
        self.surf.set_colorkey(LIGHT_YELLOW)
        self.surf = pygame.transform.smoothscale(self.surf, self.SIZE)
        self.rect = self.surf.get_rect(center=(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        ))
        self.rect.width -= 20
        self.health = self.MAX_HEALTH
        self.score = 0

    def idle(self):
        if self.IDLE_VAR >= len(player_idle_images):
            self.IDLE_VAR = 0
        self.surf = player_idle_images[self.IDLE_VAR]
        self.surf = pygame.transform.smoothscale(self.surf, self.SIZE)

        self.IDLE_VAR += 1

    def move(self):
        if self.MOVEMENT_VAR >= len(player_running_images):
            self.MOVEMENT_VAR = 0
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.center = (mouse_x, mouse_y)

        self.surf = player_running_images[self.MOVEMENT_VAR]
        self.surf = pygame.transform.smoothscale(self.surf, self.SIZE)
        self.MOVEMENT_VAR += 1

    def collect_points(self, points):
        for current_point in points:
            if pygame.Rect.colliderect(self.rect, current_point.rect):
                self.score += 1
                points.remove(current_point)

    def collect_bonus_points(self, points):
        for current_point in points:
            if pygame.Rect.colliderect(self.rect, current_point.rect):
                if isinstance(current_point, SuperPoint):
                    self.score += 50
                else:
                    self.score += 15
                points.remove(current_point)

    def take_damage(self, obstacle):
        if self.health - obstacle.DAMAGE < 0:
            self.health = 0
        else:
            self.health -= obstacle.DAMAGE
