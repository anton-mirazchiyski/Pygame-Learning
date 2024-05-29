import random
import time
from abc import ABC, abstractmethod

import pygame

from points_collector_game.configurations import SCREEN_WIDTH, SCREEN_HEIGHT, screen, RED_COLOR, BLUE_COLOR


class Point(ABC):
    def __init__(self):
        self.center = (
            random.randint(10, SCREEN_WIDTH - 10),
            random.randint(10, SCREEN_HEIGHT - 10)
        )
        self.rect = self.draw()

    @abstractmethod
    def draw(self):
        pass


class NormalPoint(Point):
    COLOR = RED_COLOR

    def __init__(self):
        self.radius = 10
        super().__init__()

    def draw(self):
        circle_rect = pygame.draw.circle(screen, self.COLOR, self.center, self.radius)
        return circle_rect


class BonusPoint(Point):
    COLOR = BLUE_COLOR

    def __init__(self):
        self.radius = 15
        super().__init__()

    def draw(self):
        circle_rect = pygame.draw.circle(screen, self.COLOR, self.center, self.radius)
        return circle_rect


class PointsHandler:
    MAX_NORMAL_POINTS_ON_SCREEN = 10
    MAX_BONUS_POINTS_ON_SCREEN = 3

    def __init__(self):
        self.current_points = self.create_points()
        self.bonus_points = []

    def create_points(self):
        return [NormalPoint() for _ in range(self.MAX_NORMAL_POINTS_ON_SCREEN)]

    def renew_points(self):
        if not self.current_points:
            time.sleep(0.1)
            self.current_points = self.create_points()

    def draw_points(self):
        self.renew_points()
        for current_point in self.current_points:
            current_point.draw()

    def add_bonus_point(self):
        if len(self.bonus_points) < self.MAX_BONUS_POINTS_ON_SCREEN:
            bonus_point = BonusPoint()
            self.bonus_points.append(bonus_point)
        self.current_points.extend(self.bonus_points)

