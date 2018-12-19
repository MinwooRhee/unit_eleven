import pygame, sys, random
from pygame.locals import *
import block


pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 32, 0)
pygame.display.set_caption("Animation")

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
WIDTH = 25
HEIGHT = 25

blocks_group = pygame.sprite.Group()
color_list = [RED, BLUE, GREEN]

for x in range(10):
    new_block = block.Block(main_window, WIDTH, HEIGHT, color_list[x % 3])
    new_block.rect.x = random.randint(WIDTH, WINDOW_WIDTH - WIDTH)
    new_block.rect.y = random.randint(HEIGHT, WINDOW_HEIGHT - HEIGHT)
    blocks_group.add(new_block)

main_window.fill(WHITE)

while True:

    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()

    main_window.fill(WHITE)
    for a_block in blocks_group:
        a_block.move()
        blocks_group.remove(a_block)
        a_block.collide(blocks_group)
        blocks_group.add(a_block)
        main_window.blit(a_block.image, a_block.rect)

    pygame.display.update()
