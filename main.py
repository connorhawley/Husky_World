import pygame
from Game import Game

game = Game()

while game.gameRunning:
    game.new_game()
    pygame.display.update()
