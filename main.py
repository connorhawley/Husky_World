from constants import *
from Player import Player
from Game import Game

#create player and game objects
player = Player()
game = Game()


game.display_main_menu()
while game.gameRunning:

    game.new_game()
    pygame.display.update()




