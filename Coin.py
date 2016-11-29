from constants import *
import time

class Coin(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        super().__init__()
        self.images = ['data/sprites/coins/goldCoin1.png', 'data/sprites/coins/goldCoin2.png', 'data/sprites/coins/goldCoin3.png',
                       'data/sprites/coins/goldCoin4.png', 'data/sprites/coins/goldCoin5.png', 'data/sprites/coins/goldCoin6.png',
                       'data/sprites/coins/goldCoin7.png', 'data/sprites/coins/goldCoin8.png', 'data/sprites/coins/goldCoin9.png',
                       'data/sprites/coins/goldCoin10.png']

        self.image = pygame.image.load(self.images[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image_framerate = 7
        self.image_count = len(self.images)
        self.last_time = pygame.time.get_ticks()
        self.index = 0


    def update(self):
        self.image = pygame.image.load(self.images[int(time.time() * self.image_framerate % len(self.images))]).convert_alpha()
