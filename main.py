import pygame, os, sys
from pygame.locals import *
from constants import *
from Player import *
from Game import *

#create player and game objects
player = Player()
game = Game()

while game.gameRunning:
    game.new_game()
    pygame.display.update()


