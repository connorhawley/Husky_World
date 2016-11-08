from Game import *
from pygame.math import Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([32,32])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.onGround = False
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.dy = 0

    def move(self, platforms, player):

        #self.dx = 5
        if not self.onGround:
            self.dy += GRAVITY
        self.rect.left += self.dx
        self.collide(self.rect.x, 0, platforms)
        self.rect.top += self.dy
        self.onGround = False
        self.collide(0, self.rect.y, platforms)


    def collide(self, dx, dy, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                if dx > 0:
                    #colliding on the right
                    self.rect.right = platform.rect.left
                if dx < 0:
                    self.rect.left = platform.rect.right
                    #colliding on the left
                if dy > 0:
                    #you are on the ground
                    self.rect.bottom = platform.rect.top
                    self.onGround = True
                    self.dy = 0
                if dy < 0:
                    self.rect.top = platform.rect.bottom
                    self.dy += 2

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))