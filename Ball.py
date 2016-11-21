from constants import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, ball_direction):
        super().__init__()
        self.image = pygame.image.load(BALL_SPRITE).convert_alpha()
        self.rect = self.image.get_rect()
        self.ball_direction = ball_direction


    def update(self):
        if self.ball_direction == 'right':
            self.rect.x += 15
        if self.ball_direction == 'left':
            self.rect.x -= 15

