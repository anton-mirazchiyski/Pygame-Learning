import pygame

from points_collector_game.configurations import LIGHT_YELLOW, SCREEN_WIDTH, SCREEN_HEIGHT, player_running_images


class Player(pygame.sprite.Sprite):
    SIZE = (140, 140)
    MOVING = False
    MOVEMENT_VAR = 0

    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('images/redhat_boy_sprite/idle/Idle (6).png').convert_alpha()
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
