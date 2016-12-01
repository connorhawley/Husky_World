from constants import *
from pygame import *

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = HUSKY_WORLD_WOOD
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class EnemyPlatform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = HUSKY_WORLD_WOOD
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class FakePlatform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = HUSKY_WORLD_WOOD
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Structure(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = HUSKY_WORLD_STRUCTURE
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class EnemyStructure(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = HUSKY_WORLD_STRUCTURE
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class JumpBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.Surface([32,32])
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class ExitBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = EXIT_HOOP
        self.rect = Rect(x-128, y-234, 160, 266)

class KillBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = SPIKE
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class KillBlock2(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = SPIKE2
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class InvisibleBlock(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.Surface([32,32])
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class Brick(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = HUSKY_WORLD_BRICK
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)