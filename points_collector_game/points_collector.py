import sys

import pygame

from points_collector_game.configurations import SCREEN_WIDTH, SCREEN_HEIGHT, screen, LIGHT_YELLOW, \
    score_font, GREEN_COLOR, game_over_font, clock
from points_collector_game.obstacles import Obstacle
from points_collector_game.player import Player
from points_collector_game.points import PointsHandler


def out_of_screen(group):
    for member in group:
        if member.rect.x > SCREEN_WIDTH:
            member.kill()
            return True


player = Player()
points_handler = PointsHandler()

obstacles = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            player.move()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    screen.fill(LIGHT_YELLOW)
    player_score = score_font.render(f'Your score: {player.score}', True, GREEN_COLOR)

    if len(obstacles) < 3 or (out_of_screen(obstacles) and len(obstacles) < 3):
        obstacle = Obstacle()
        obstacles.add(obstacle)
    obstacles.update()

    points_handler.draw_points()
    points_handler.collect_points(player)

    if pygame.sprite.spritecollideany(player, obstacles):
        screen.fill((0, 0, 0))
        game_over = game_over_font.render('You were hit. Game over!', True, GREEN_COLOR)
        screen.blit(game_over, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    screen.blit(player.surf, player.rect)
    for obstacle in obstacles:
        screen.blit(obstacle.surf, obstacle.rect)
    screen.blit(player_score, (40, 40))
    pygame.display.flip()
    clock.tick(20)
