import pygame, sys
from pygame.locals import *
import block


pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
X_SPEED = 50
Y_SPEED = 50
main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 32, 0)
pygame.display.set_caption("Animation")

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
WIDTH = 25
HEIGHT = 25

my_block = block.Block(main_window, WIDTH, HEIGHT, BLUE)
new_block = block.Block(main_window, WIDTH, HEIGHT, GREEN)
red_block = block.Block(main_window, WIDTH, HEIGHT, RED)

my_block.rect.x = 10
my_block.rect.y = 10
new_block.rect.x = WINDOW_WIDTH - 35
new_block.rect.y = WINDOW_HEIGHT - 35
red_block.rect.x = 20
red_block.rect.y = 20

while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()

    main_window.fill(WHITE)
    my_block.move()
    new_block.move()
    red_block.move()
    main_window.blit(my_block.image, my_block.rect)
    main_window.blit(new_block.image, new_block.rect)
    main_window.blit(red_block.image, red_block.rect)
    pygame.display.update()
