import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.

        self.image = pygame.Surface((self.radius, self.radius))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        pygame.draw.circle(self.image, (255, 0, 0), (10, 10), 10, 0)

    def move(self):
        pass
