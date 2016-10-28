import pygame, os

#This file contains constants (colors, paths, etc)

#Window size
WINDOW_HEIGHT = 768
WINDOW_WIDTH = 1024
HALF_WINDOW_WIDTH = WINDOW_WIDTH/2
HALF_WINDOW_HEIGHT = WINDOW_HEIGHT/2
SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
#set game title
TITLE = "Husky World"
#Colors
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
PURPLE = (255,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

#Fonts
pygame.font.init()
SMALLFONT = pygame.font.SysFont('data / fonts / freesansbold.ttf', 25)
MEDIUMFONT = pygame.font.SysFont('data/fonts/freesansbold.ttf', 50)
LARGEFONT = pygame.font.SysFont('data/fonts/freesansbold.ttf', 100)

#Set FPS for game to run at
FPS = 60
#set path for the player sprite
player_sprite = 'data/sprites/dog.png'

menu_select_sprite = 'data/sprites/menu_select_sprite.png'
