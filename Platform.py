from constants import *
from pygame import *

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load(HUSKY_WORLD_WOOD).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class EnemyPlatform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load(HUSKY_WORLD_WOOD).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Structure(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load(HUSKY_WORLD_STRUCTURE).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class JumpBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.Surface([32,32])
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class ExitBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(GREEN)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class KillBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load(SPIKE).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class KillBlock2(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load(SPIKE2).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class InvisibleBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.Surface([32,32])
        self.image.fill(PURPLE)
        self.image.set_alpha(100)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Brick(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load(HUSKY_WORLD_BRICK).convert_alpha()
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)