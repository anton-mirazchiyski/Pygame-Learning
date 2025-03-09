import random
import time
from abc import ABC, abstractmethod

import pygame

from points_collector_game.configurations import SCREEN_WIDTH, SCREEN_HEIGHT, screen, RED_COLOR, BLUE_COLOR, \
    DARK_GRAY, GREEN_COLOR


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
    COLOR = GREEN_COLOR

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


class SuperPoint(BonusPoint):
    COLOR = DARK_GRAY


class PointsHandler:
    MAX_NORMAL_POINTS_ON_SCREEN = 10

    def __init__(self):
        self.current_points = self.create_points()

    def create_points(self):
        return [NormalPoint() for _ in range(self.MAX_NORMAL_POINTS_ON_SCREEN)]

    def renew_points(self):
        if not self.current_points:
            time.sleep(0.1)
            self.current_points = self.create_points()

    def replace_point(self, point):
        self.current_points.remove(point)
        new_point = NormalPoint()
        self.current_points.append(new_point)
        new_point.draw()

    def handle_overlapping_points(self):
        i = 1
        for first_point in self.current_points:
            other_points = self.current_points[:i - 1] + self.current_points[i:]
            for second_point in other_points:
                if pygame.Rect.colliderect(first_point.rect, second_point.rect):
                    self.replace_point(second_point)
            i += 1

    def handle_overlapping_with_text(self, *args):
        for point in self.current_points:
            for text_rect in args:
                if pygame.Rect.colliderect(point.rect, text_rect):
                    self.replace_point(point)

    def draw_points(self):
        self.renew_points()
        for current_point in self.current_points:
            current_point.draw()
        self.handle_overlapping_points()


class BonusPointsHandler(PointsHandler):
    MAX_BONUS_POINTS_ON_SCREEN = 3

    def __init__(self):
        super().__init__()
        self.bonus_points = []

    def add_bonus_point(self):
        if self.can_add_bonus_point:
            bonus_point = BonusPoint()
            self.bonus_points.append(bonus_point)

    def add_super_point(self):
        if self.can_add_bonus_point:
            super_point = SuperPoint()
            self.bonus_points.append(super_point)

    def handle_overlapping_points(self):
        for point in self.current_points:
            for bonus_point in self.bonus_points:
                if pygame.Rect.colliderect(point.rect, bonus_point.rect):
                    super().replace_point(point)

    def handle_overlapping_with_text(self, *args):
        for point in self.bonus_points:
            for text_rect in args:
                if pygame.Rect.colliderect(point.rect, text_rect):
                    self.bonus_points.remove(point)
                    new_point = BonusPoint() if isinstance(point, BonusPoint) else SuperPoint()
                    self.bonus_points.append(new_point)
                    new_point.draw()

    def draw_bonus_points(self):
        self.handle_overlapping_points()
        for bonus_point in self.bonus_points:
            bonus_point.draw()

    @property
    def can_add_bonus_point(self):
        return len(self.bonus_points) < self.MAX_BONUS_POINTS_ON_SCREEN
