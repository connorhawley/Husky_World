import pygame
from pygame.locals import *
from constants import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        #call parent constructor
        super().__init__()
        #create player sprite image
        self.image = pygame.image.load(player_sprite)
        self.rect = self.image.get_rect()
        #self.x = 0
        #self.y = 0

    def jump(self):

        pass

    def update(self):
       self.gravity()
       #check collisions with platforms

    def gravity(self):
        #calculate gravity on player
        if self.rect.y == 0:
            self.rect.y = 1
        else:
            self.rect.y += gravity

    #draws player sprite to screen
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


    #handles the player input
    def handle_input(self):
        key = pygame.key.get_pressed()
        dist = player_speed
        if key[pygame.K_DOWN]:
            self.rect.y += dist
        if key[pygame.K_UP]:
            self.rect.y -= jump_height
        if key[pygame.K_RIGHT]:
            self.rect.x += dist
        if key[pygame.K_LEFT]:
            self.rect.x -= dist


