# Minwoo Rhee
# 2019 01 16
# breakout.py
# move the paddle with mouse to bounce the ball and break bricks

import pygame, sys, brick, paddle, ball
from pygame.locals import *


def main():
    """
    Variables are defined, main surface is set, place the bricks, paddle, ball and blit
    :return: None
    """
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW - 1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 100
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 12

    # lives
    NUM_TURNS = 2

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

    # bricks and paddle has to be in group to collide the ball
    bricks_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    color_list = [RED, ORANGE, YELLOW, GREEN, CYAN]

    # loop for changing rows
    for a in range(10):

        # color changes after every two rows
        brick_color = color_list[a//2]

        # loop for placing 10 bricks in a row
        for b in range(10):
            my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, brick_color)
            my_brick.rect.x = (BRICK_WIDTH + 4) * b
            my_brick.rect.y = BRICK_Y_OFFSET
            bricks_group.add(my_brick)

        BRICK_Y_OFFSET = BRICK_Y_OFFSET + (BRICK_HEIGHT + 4)

    # placing the paddle
    my_paddle = paddle.Paddle(main_surface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    paddle_group.add(my_paddle)

    # placing the ball
    my_ball = ball.Ball(RED, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = APPLICATION_WIDTH/2
    my_ball.rect.y = APPLICATION_HEIGHT/2

    while True:
            for event in pygame.event.get():
                if event == QUIT:
                    pygame.quit()
                    sys.exit()

                # When all bricks are broke, end the program
                if len(bricks_group) == 0:
                    pygame.quit()
                    sys.exit()

            # When the ball hits the bottom, -1 life
            if my_ball.rect.bottom >= APPLICATION_HEIGHT:
                my_ball.rect.x = APPLICATION_WIDTH / 2
                my_ball.rect.y = APPLICATION_HEIGHT / 2
                if NUM_TURNS == 0:
                    break  # end the program when all loves are lost
                else:
                    NUM_TURNS -= 1

            # fill the surface white so the sprites do not leave traces
            main_surface.fill(WHITE)

            # move and blit paddle
            position = pygame.mouse.get_pos()
            my_paddle.rect.x = position[0] - PADDLE_WIDTH/2
            main_surface.blit(my_paddle.image, my_paddle.rect)

            # move and blit ball
            my_ball.move()
            main_surface.blit(my_ball.image, my_ball.rect)
            my_ball.collide(bricks_group, paddle_group)

            # blit bricks using for loop
            for x in bricks_group:
                main_surface.blit(x.image, x.rect)

            pygame.display.update()


main()
