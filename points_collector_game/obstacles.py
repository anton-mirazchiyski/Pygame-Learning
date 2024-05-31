import random

import pygame

from points_collector_game.configurations import LIGHT_YELLOW, SCREEN_HEIGHT, dinosaur_walking_images, SCREEN_WIDTH


class Obstacle(pygame.sprite.Sprite):
    SIZE = (100, 90)
    DAMAGE = 35
    MOVEMENT_VAR = 0

    def __init__(self):
        super().__init__()
        self.surf = pygame.image.load('images/dino_sprite/walking/Walk (1).png').convert_alpha()
        self.surf.set_colorkey(LIGHT_YELLOW)
        self.surf = pygame.transform.smoothscale(self.surf, self.SIZE)
        self.rect = self.surf.get_rect(center=(
            30, random.randint(10, SCREEN_HEIGHT - 10)
        ))
        self.rect.width -= 40
        self.is_visible = True

    def update(self):
        self.rect.move_ip(4, 0)

        if self.MOVEMENT_VAR >= len(dinosaur_walking_images):
            self.MOVEMENT_VAR = 0
        image = dinosaur_walking_images[self.MOVEMENT_VAR]
        image = pygame.transform.smoothscale(image, self.SIZE)
        self.surf = image
        self.MOVEMENT_VAR += 1


class ObstaclesHandler:
    MAX_OBSTACLES_ON_SCREEN = 3

    def __init__(self):
        self.obstacles = pygame.sprite.Group()

    def add_obstacle(self):
        self.remove_out_of_screen_obstacle()
        if len(self.obstacles) < self.MAX_OBSTACLES_ON_SCREEN:
            obstacle = Obstacle()
            self.obstacles.add(obstacle)

    def remove_out_of_screen_obstacle(self):
        for obstacle in self.obstacles:
            if obstacle.rect.x > SCREEN_WIDTH:
                obstacle.kill()

    def handle_collided_obstacles(self, collided_obstacles, player):
        collision_time = pygame.time.get_ticks()
        # print(collision_time)
        for obstacle in collided_obstacles:
            if collision_time % 3 == 0:
                obstacle.is_visible = not obstacle.is_visible
                # obstacle.kill()
                # player.take_damage(obstacle)

    def check_collision_with_player(self, current_player):
        collided_obstacles = pygame.sprite.spritecollide(current_player, self.obstacles, False)
        if collided_obstacles:
            self.handle_collided_obstacles(collided_obstacles, current_player)
