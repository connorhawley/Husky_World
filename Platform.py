from constants import *
from pygame import *

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load('data/levels/Husky_World_Wood.png')
        self.image.convert()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Structure(pygame.sprite.Sprite):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load('data/levels/Husky_World_Structure.png')
        self.image.convert()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)