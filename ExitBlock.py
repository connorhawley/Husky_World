from pygame import *
from constants import *

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class ExitBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(GREEN)
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)
