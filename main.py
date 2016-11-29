from constants import *
from Game import Game

#create game object and runs it

game = Game()

while game.gameRunning:
    game.new_game()
    pygame.display.update()
