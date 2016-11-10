from constants import *
from pygame import *

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load('data/sprites/tile32.png')
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)