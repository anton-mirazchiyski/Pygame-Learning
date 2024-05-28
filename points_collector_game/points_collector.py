import sys

import pygame

from points_collector_game.configurations import SCREEN_WIDTH, SCREEN_HEIGHT, screen, LIGHT_YELLOW, \
    score_font, GREEN_COLOR, game_over_font, clock, player_health_font, BLUE_COLOR
from points_collector_game.obstacles import ObstaclesHandler
from points_collector_game.player import Player
from points_collector_game.points import PointsHandler


player = Player()
points_handler = PointsHandler()
obstacles_handler = ObstaclesHandler()

PLACE_OBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(PLACE_OBSTACLE, 2000)

while True:
    for event in pygame.event.get():
        if event.type == PLACE_OBSTACLE:
            obstacles_handler.add_obstacle()
        if event.type == pygame.MOUSEMOTION:
            player.move()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill(LIGHT_YELLOW)
    player_score = score_font.render(f'Your score: {player.score}', True, GREEN_COLOR)
    player_health = player_health_font.render(f'Health: {player.health}', True, (170, 74, 68))

    points_handler.draw_points()
    player.collect_points(points_handler.current_points)
    obstacles_handler.obstacles.update()
    obstacles_handler.check_collision_with_player(player)

    screen.blit(player.surf, player.rect)
    for obstacle in obstacles_handler.obstacles:
        screen.blit(obstacle.surf, obstacle.rect)
    screen.blit(player_score, (40, 40))
    screen.blit(player_health, (200, 40))
    pygame.display.flip()
    clock.tick(20)
