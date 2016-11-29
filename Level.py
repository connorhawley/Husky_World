import pygame
from Enemy import *
from Player import Player

class Level():
    def __init__(self):
        self.level = []
        self.enemies = pygame.sprite.Group()
        self.invincible_enemies = pygame.sprite.Group()




