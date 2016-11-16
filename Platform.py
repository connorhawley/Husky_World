from constants import *
from pygame import *

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load('data/levels/Husky_World_Wood.png')
        self.image.convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Structure(pygame.sprite.Sprite):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load('data/levels/Husky_World_Structure.png')
        self.image.convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class JumpBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(BLUE)
        self.image.set_alpha(75)
        self.image.convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class ExitBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(GREEN)
        self.image.convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class KillBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load('data/sprites/spike.png')
        self.image.convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class InvisibleBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(PURPLE)
        self.image.convert_alpha()
        self.image.set_alpha(100)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Brick(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load('data/levels/Husky_World_Brick.png')
        self.image.convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)