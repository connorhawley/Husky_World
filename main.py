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
    player.handle_keys()
    player.draw(game.screen)
    pygame.display.update()

