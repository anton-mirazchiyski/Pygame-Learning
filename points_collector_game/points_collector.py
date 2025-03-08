import sys

import pygame

from points_collector_game.configurations import screen, LIGHT_YELLOW, clock
from points_collector_game.events import PLACE_OBSTACLE, PLACE_BONUS_POINT, PLACE_SUPER_BONUS_POINT
from points_collector_game.game_text import TextHandler
from points_collector_game.obstacles import ObstaclesHandler
from points_collector_game.player import Player
from points_collector_game.points import PointsHandler, BonusPointsHandler

text_handler = TextHandler()
player = Player()
points_handler = PointsHandler()
bonus_points_handler = BonusPointsHandler()
obstacles_handler = ObstaclesHandler()

while True:
    for event in pygame.event.get():
        if event.type == PLACE_OBSTACLE:
            obstacles_handler.add_obstacle()
        if event.type == PLACE_BONUS_POINT:
            bonus_points_handler.add_bonus_point()
        if event.type == PLACE_SUPER_BONUS_POINT:
            bonus_points_handler.add_super_point()
        if event.type == pygame.MOUSEMOTION and not player.is_hurt:
            player.move()
        else:
            player.idle()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill(LIGHT_YELLOW)

    points_handler.draw_points()
    points_handler.handle_overlapping_with_text(
        text_handler.handle_player_score(player.score)[1],
        text_handler.handle_player_health(player.health)[1]
    )

    bonus_points_handler.draw_bonus_points()
    bonus_points_handler.handle_overlapping_with_text(
        text_handler.handle_player_score(player.score)[1],
        text_handler.handle_player_health(player.health)[1]
    )

    player.collect_points(points_handler.current_points)
    player.collect_bonus_points(bonus_points_handler.bonus_points)
    obstacles_handler.obstacles.update()

    screen.blit(player.surf, player.rect)

    for obstacle in obstacles_handler.obstacles:
        if obstacle.is_visible:
            screen.blit(obstacle.surf, obstacle.rect)
        if obstacle.has_collided:
            obstacles_handler.handle_collided_obstacle(obstacle)

    collided_obstacle = pygame.sprite.spritecollideany(player, obstacles_handler.obstacles)
    if collided_obstacle:
        collided_obstacle.has_collided = True
        player.is_hurt = True
        player.take_damage(collided_obstacle)

    screen.blit(
        text_handler.handle_player_score(player.score)[0],
        text_handler.handle_player_score(player.score)[1])
    screen.blit(
        text_handler.handle_player_health(player.health)[0],
        text_handler.handle_player_health(player.health)[1])

    pygame.display.flip()
    clock.tick(20)
