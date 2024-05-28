import random
import time

import pygame

from points_collector_game.configurations import SCREEN_WIDTH, SCREEN_HEIGHT, screen, RED_COLOR


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


class PointsHandler:
    MAX_POINTS_ON_SCREEN = 10

    def __init__(self):
        self.current_points = self.create_points()

    def create_points(self):
        return [Point() for _ in range(self.MAX_POINTS_ON_SCREEN)]

    def renew_points(self):
        if not self.current_points:
            time.sleep(0.1)
            self.current_points = self.create_points()

    def draw_points(self):
        self.renew_points()
        for current_point in self.current_points:
            current_point.draw()
