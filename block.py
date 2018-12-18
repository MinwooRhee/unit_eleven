import pygame
import random


class Block(pygame.sprite.Sprite):

    def __init__(self, screen, width, height, color):
        super().__init__()
        self.screen = screen
        self.width = width
        self.height = height
        self.color = color
        self.x_speed = random.randint(1, 20)
        self.y_speed = random.randint(1, 20)

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)

    def move(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.x_speed = - self.x_speed
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.y_speed = - self.y_speed

    def collide(self, blocks_group):
        if pygame.sprite.spritecollide(self, blocks_group, False):
            self.x_speed = - self.x_speed
            self.y_speed = - self.y_speed
