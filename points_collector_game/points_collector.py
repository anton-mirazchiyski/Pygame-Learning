import sys

import pygame

from points_collector_game.configurations import screen, LIGHT_YELLOW, \
    score_font, GREEN_COLOR, clock, player_health_font
from points_collector_game.obstacles import ObstaclesHandler
from points_collector_game.player import Player
from points_collector_game.points import PointsHandler


player = Player()
points_handler = PointsHandler()
obstacles_handler = ObstaclesHandler()

PLACE_OBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(PLACE_OBSTACLE, 2000)

PLACE_BONUS_POINT = pygame.USEREVENT + 2
pygame.time.set_timer(PLACE_BONUS_POINT, 20000)

while True:
    for event in pygame.event.get():
        if event.type == PLACE_OBSTACLE:
            obstacles_handler.add_obstacle()
        if event.type == PLACE_BONUS_POINT:
            points_handler.add_bonus_point()
        if event.type == pygame.MOUSEMOTION:
            player.move()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill(LIGHT_YELLOW)
    player_score = score_font.render(f'Your score: {player.score}', True, GREEN_COLOR)
    player_health = player_health_font.render(f'Health: {player.health}', True, (170, 74, 68))

    points_handler.draw_points()
    points_handler.draw_bonus_points()
    player.collect_points(points_handler.current_points)
    player.collect_bonus_points(points_handler.bonus_points)
    obstacles_handler.obstacles.update()
    obstacles_handler.check_collision_with_player(player)

    screen.blit(player.surf, player.rect)
    # pygame.draw.rect(screen, (0, 0, 0), player.rect, 1)
    for obstacle in obstacles_handler.obstacles:
        screen.blit(obstacle.surf, obstacle.rect)
        # pygame.draw.rect(screen, (0, 0, 0), obstacle.rect, 1)
    screen.blit(player_score, (40, 40))
    screen.blit(player_health, (40, 600))
    pygame.display.flip()
    clock.tick(20)
