from constants import *

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(BALL_SPRITE)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 15

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))