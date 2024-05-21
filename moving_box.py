import pygame

pygame.init()

clock = pygame.time.Clock()

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (30, 144, 255)

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE_COLOR)

pygame.display.set_caption('Moving Box')

box_x, box_y = 40, 350
box_width, box_height = 50, 50

box = pygame.rect.Rect((box_x, box_y), (box_width, box_height))


def move_box(current_box):
    current_box.move_ip(5, 0)
    if current_box.x > SCREEN_WIDTH:
        current_box.center = (box_x, box_y)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(WHITE_COLOR)
    pygame.draw.rect(screen, BLUE_COLOR, box)
    move_box(box)
    pygame.display.flip()
    clock.tick(45)
