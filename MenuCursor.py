from constants import *


class MenuCursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(MENU_SELECT_SPRITE)
        self.rect = self.image.get_rect()
        self.rect.x = 340
        self.rect.y = 259


    def moveUp(self):
        self.rect.y -= 200
    def moveDown(self):
        self.rect.y += 200

    def handleKeys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.moveDown()
        if key[pygame.K_UP]:
            self.moveUp()


    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))