import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        """
        initialize the class as sprite, fill the sprite with background color and draw the ball
        :param color: color of the ball
        :param windowWidth: width of the application
        :param windowHeight: height of the application
        :param radius: radius of the ball
        """
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius
        self.x_speed = 0
        self.y_speed = 5
        # absolute speed of the ball after hitting the paddle
        self.abs_speed = 15

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.

        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, self.color, (radius, radius), radius, 0)

    def move(self):
        """
        move the ball, speed changing when the ball hits the sides and the top
        :return: None
        """

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left <= 0 or self.rect.right >= self.windowWidth:
            self.x_speed = - self.x_speed
        if self.rect.top <= 0:
            self.y_speed = - self.y_speed

    def collide(self, bricks_group, paddle_group):
        """
        ball collides with the bricks and the paddle
        :param bricks_group: sprite group of bricks
        :param paddle_group: sprite group of paddle
        :return: None
        """

        if pygame.sprite.spritecollide(self, bricks_group, True):
            self.y_speed = - self.y_speed
        if pygame.sprite.spritecollide(self, paddle_group, False):
            # the x speed of the ball changes relative to the distance between the mouse and the ball
            mouse = pygame.mouse.get_pos()
            position = self.rect.x + self.radius - mouse[0]  # position is a tupple
            self.x_speed = position/5
            self.y_speed = - abs(self.abs_speed - abs(position/5))
