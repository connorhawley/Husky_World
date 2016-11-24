from constants import *
from Player import Player
from Game import Game

#create player and game objects

game = Game()
#player = Player()

while game.gameRunning:
    game.new_game()
    pygame.display.update()
