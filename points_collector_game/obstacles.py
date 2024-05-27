import random

import pygame

from points_collector_game.configurations import LIGHT_YELLOW, SCREEN_HEIGHT, dinosaur_walking_images


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
