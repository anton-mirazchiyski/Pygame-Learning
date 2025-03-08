import pygame

PLACE_OBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(PLACE_OBSTACLE, 2000)

PLACE_BONUS_POINT = pygame.USEREVENT + 2
pygame.time.set_timer(PLACE_BONUS_POINT, 20000)

PLACE_SUPER_BONUS_POINT = pygame.USEREVENT + 3
pygame.time.set_timer(PLACE_SUPER_BONUS_POINT, 50000)
