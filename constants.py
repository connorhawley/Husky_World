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
ORANGE = (255,165,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
NAVY_BLUE = (0,14,47)

#Fonts
pygame.font.init()
SMALLFONT = pygame.font.Font('data/fonts/uconn.ttf', 25)
MEDIUMFONT = pygame.font.Font('data/fonts/uconn.ttf', 50)
LARGEFONT = pygame.font.Font('data/fonts/uconn.ttf', 75)
XLFONT = pygame.font.Font('data/fonts/uconn.ttf', 100)

#Set FPS for game to run at
FPS = 60
#set path for sprites

HUSKY_SPRITES = 'data/sprites/husky_sprites.png'
MENU_SELECT_SPRITE = 'data/sprites/menu_select_sprite.png'
BALL_SPRITE = 'data/sprites/ball.png'
ENEMY_SPRITE = 'data/sprites/enemy.png'
ENEMY_SPIKE_SPRITE = 'data/sprites/enemy2.png'

HUSKY_WORLD_BRICK = 'data/levels/Husky_World_Brick.png'
HUSKY_WORLD_WOOD = 'data/levels/Husky_World_Wood.png'
HUSKY_WORLD_STRUCTURE = 'data/levels/Husky_World_Structure.png'

SPIKE = 'data/sprites/spike.png'
SPIKE2 = 'data/sprites/spike2.png'

HELP_MENU = 'data/sprites/help_menu.png'


PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32

#player ball shoot cooldown in ms
SHOOT_COOLDOWN = 500


#movement variables
GRAVITY = 0.5
JUMP_HEIGHT = 13
PLAYER_SPEED = 8
ENEMY_SPEED = 3

