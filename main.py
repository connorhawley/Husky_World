from constants import *
from Player import Player
from Game import Game
from Platform import Platform

#create player and game objects
player = Player()
game = Game()

while game.gameRunning:
    game.new_game()
    pygame.display.update()




