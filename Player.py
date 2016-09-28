import pygame
from pygame.locals import *
from constants import *

class Player(pygame.sprite.Sprite):

    def __init__(self):

      super().__init__()
      self.image = pygame.image.load(player_sprite)
      self.x = 0
      self.y = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = jonathan_speed
        if key[pygame.K_DOWN]:
            self.y += dist
        if key[pygame.K_UP]:
            self.y -= dist
        if key[pygame.K_RIGHT]:
            self.x += dist
        if key[pygame.K_LEFT]:
            self.x -= dist

    def jump(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))