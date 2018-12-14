import pygame, sys, brick, paddle
from pygame.locals import *

def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW - 1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)

    pygame.init()
    main_surface = pygame.display.set_mode((400, 600), 0, 32)
    pygame.display.set_caption("breakout")
    main_surface.fill(WHITE)

    bricks_group = pygame.sprite.Group()
    color_list = [RED, ORANGE, YELLOW, GREEN, CYAN]

    for a in range(10):

        color = color_list[a//2]

        for b in range(10):
            my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
            my_brick.rect.x = (BRICK_WIDTH + 4) * b
            my_brick.rect.y = BRICK_Y_OFFSET
            bricks_group.add(my_brick)

        BRICK_Y_OFFSET = BRICK_Y_OFFSET + (BRICK_HEIGHT + 4)

    my_paddle = paddle.Paddle(main_surface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET

    while True:
            for event in pygame.event.get():
                if event == QUIT:
                    pygame.quit()
                    sys.exit()

            main_surface.fill(WHITE)
            position = pygame.mouse.get_pos()
            my_paddle.rect.x = position[0]
            main_surface.blit(my_paddle.image, my_paddle.rect)

            for x in bricks_group:
                main_surface.blit(x.image, x.rect)

            pygame.display.update()


main()
