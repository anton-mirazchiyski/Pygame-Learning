import pygame

pygame.init()

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (30, 144, 255)

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE_COLOR)

box_x, box_y = 40, 350
box_width, box_height = 50, 50

box = pygame.rect.Rect((box_x, box_y), (box_width, box_height))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(screen, BLUE_COLOR, box)
    pygame.display.flip()
