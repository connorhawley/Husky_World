from constants import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, type='normal'):
        super().__init__()
        if type == 'normal':
            self.image = pygame.image.load(ENEMY_SPRITE).convert_alpha()
        elif type == 'invincible':
            self.image = pygame.image.load(ENEMY_SPIKE_SPRITE).convert_alpha()

        self.rect = self.image.get_rect()
        self.onGround = False
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.dy = 0
        self.direction = 'left'

    def update(self, platforms):
        if self.direction == 'left':
            self.dx = -3
        if self.direction == 'right':
            self.dx = 3

        if not self.onGround:
            self.dy += GRAVITY
        self.rect.left += self.dx
        # collision for x axis
        self.collide(self.dx, 0, platforms)
        self.rect.top += self.dy
        self.onGround = False
        # collision for y axis
        self.collide(0, self.dy, platforms)


    def collide(self, dx, dy, platforms):
        for platform in platforms:
            if pygame.sprite.collide_rect(self, platform):
                if dx > 0:
                    #colliding on the right
                    self.direction = 'left'
                    self.rect.right = platform.rect.left
                if dx < 0:
                    self.direction = 'right'
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

    def jump(self):
        if self.onGround:
            self.dy -= 10

