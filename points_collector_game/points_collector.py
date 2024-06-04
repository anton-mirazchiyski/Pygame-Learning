import sys

import pygame

from points_collector_game.configurations import screen, LIGHT_YELLOW, \
    score_font, GREEN_COLOR, clock, player_health_font
from points_collector_game.obstacles import ObstaclesHandler
from points_collector_game.player import Player
from points_collector_game.points import PointsHandler, BonusPointsHandler

player = Player()
points_handler = PointsHandler()
bonus_points_handler = BonusPointsHandler()
obstacles_handler = ObstaclesHandler()

PLACE_OBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(PLACE_OBSTACLE, 2000)

PLACE_BONUS_POINT = pygame.USEREVENT + 2
pygame.time.set_timer(PLACE_BONUS_POINT, 20000)

PLACE_SUPER_BONUS_POINT = pygame.USEREVENT + 3
pygame.time.set_timer(PLACE_SUPER_BONUS_POINT, 50000)

while True:
    for event in pygame.event.get():
        if event.type == PLACE_OBSTACLE:
            obstacles_handler.add_obstacle()
        if event.type == PLACE_BONUS_POINT:
            bonus_points_handler.add_bonus_point()
        if event.type == PLACE_SUPER_BONUS_POINT:
            bonus_points_handler.add_super_point()
        if event.type == pygame.MOUSEMOTION:
            player.move()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill(LIGHT_YELLOW)
    player_score = score_font.render(f'Your score: {player.score}', True, GREEN_COLOR)
    player_health = player_health_font.render(f'Health: {player.health}', True, (170, 74, 68))

    points_handler.draw_points()
    bonus_points_handler.draw_bonus_points()
    player.collect_points(points_handler.current_points)
    player.collect_bonus_points(bonus_points_handler.bonus_points)
    obstacles_handler.obstacles.update()
    obstacles_handler.check_collision_with_player(player)

    screen.blit(player.surf, player.rect)
    for obstacle in obstacles_handler.obstacles:
        if obstacle.is_visible:
            screen.blit(obstacle.surf, obstacle.rect)
    screen.blit(player_score, (40, 40))
    screen.blit(player_health, (40, 600))
    pygame.display.flip()
    clock.tick(20)
