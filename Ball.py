from constants import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, ball_direction):
        super().__init__()
        self.image = BALL_SPRITE
        self.rect = self.image.get_rect()
        self.ball_direction = ball_direction
        self.dx = 15


    def update(self):
        if self.ball_direction == 'right':
            self.rect.x += self.dx
        if self.ball_direction == 'left':
            self.rect.x -= self.dx
