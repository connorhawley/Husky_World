import pygame

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
NAVY_BLUE = (0,14,47)

#Fonts
pygame.font.init()
SMALLFONT = pygame.font.Font('data/fonts/uconn.ttf', 25)
MEDIUMFONT = pygame.font.Font('data/fonts/uconn.ttf', 50)
LARGEFONT = pygame.font.Font('data/fonts/uconn.ttf', 75)

#Set FPS for game to run at
FPS = 60
#set path for sprites
HUSKY_SPRITES = 'data/sprites/husky_sprites.png'
MENU_SELECT_SPRITE = 'data/sprites/menu_select_sprite.png'
BALL_SPRITE = 'data/sprites/ball.png'

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32

#player movement variables
GRAVITY = 0.5
JUMP_HEIGHT = 16
PLAYER_SPEED = 8
