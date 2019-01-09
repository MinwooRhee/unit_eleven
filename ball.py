import pygame, math


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius
        self.x_speed = 0
        self.y_speed = 5

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.

        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, (255, 0, 0), (radius, radius), radius, 0)

    def move(self):

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left <= 0 or self.rect.right >= self.windowWidth:
            self.x_speed = - self.x_speed
        if self.rect.top <= 0:
            self.y_speed = - self.y_speed

    def collide(self, bricks_group, paddle_group):
        if pygame.sprite.spritecollide(self, bricks_group, True):
            self.x_speed = - self.x_speed
            self.y_speed = - self.y_speed
        if pygame.sprite.spritecollide(self, paddle_group, False):
            mouse = pygame.mouse.get_pos()
            position = self.rect.x + self.radius - mouse[0]
            self.x_speed = position/5
            self.y_speed = - 30
