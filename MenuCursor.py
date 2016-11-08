from constants import *


class MenuCursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('data/sprites/menu_select_sprite.png')
        self.rect = self.image.get_rect()
        self.rect.x = 340
        self.rect.y = 259
        self.onPlay = True
        self.onQuit = False

    def moveToPlay(self):
        self.rect.y -= 200
        self.onQuit = False
        self.onPlay = True

    def moveToQuit(self):
        self.rect.y += 200
        self.onPlay = False
        self.onQuit = True

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


    def handleKeys(self):
        key = pygame.key.get_pressed()
        if self.onPlay:
            if key[pygame.K_DOWN]:
                self.moveToQuit()
        if self.onQuit:
            if key[pygame.K_UP]:
                self.moveToPlay()


