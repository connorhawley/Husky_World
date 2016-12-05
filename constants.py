import pygame

#This file contains constants (colors, paths, etc)

#Window size
WINDOW_HEIGHT = 768
WINDOW_WIDTH = 1024
HALF_WINDOW_WIDTH = WINDOW_WIDTH/2
HALF_WINDOW_HEIGHT = WINDOW_HEIGHT/2
SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
#set game title
TITLE = "Super Husky World"
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
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.font.init()
SCREEN = pygame.display.set_mode(SIZE)
SMALLFONT = pygame.font.Font('data/fonts/uconn.ttf', 25)
MEDIUMFONT = pygame.font.Font('data/fonts/uconn.ttf', 50)
LARGEFONT = pygame.font.Font('data/fonts/uconn.ttf', 75)
XLFONT = pygame.font.Font('data/fonts/uconn.ttf', 100)

#Set FPS for game to run at
FPS = 60
#set path for sprites

HUSKY_SPRITES = pygame.image.load('data/sprites/husky_sprites.png').convert_alpha()
MENU_SELECT_SPRITE = pygame.image.load('data/sprites/menu_select_sprite.png').convert_alpha()
BALL_SPRITE = pygame.image.load('data/sprites/ball.png').convert_alpha()
ENEMY_SPRITE = pygame.image.load('data/sprites/enemy4.png').convert_alpha()
ENEMY_SPIKE_SPRITE = pygame.image.load('data/sprites/enemy2.png').convert_alpha()

HUSKY_WORLD_BRICK = pygame.image.load('data/levels/Husky_World_Brick.png').convert_alpha()
HUSKY_WORLD_WOOD = pygame.image.load('data/levels/Husky_World_Wood.png').convert_alpha()
HUSKY_WORLD_STRUCTURE = pygame.image.load('data/levels/Husky_World_Structure.png').convert_alpha()

EXIT_HOOP = pygame.image.load('data/sprites/hoop.png').convert_alpha()

SPIKE = pygame.image.load('data/sprites/spike.png').convert_alpha()
SPIKE2 = pygame.image.load('data/sprites/spike2.png').convert_alpha()
HELP_MENU = pygame.image.load('data/sprites/help_menu.png').convert_alpha()
MAIN_MENU = pygame.image.load('data/sprites/main_menu.png').convert_alpha()


PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32

#player ball shoot cooldown in ms
SHOOT_COOLDOWN = 500


#movement variables
GRAVITY = 0.5
JUMP_HEIGHT = 13
PLAYER_SPEED = 8
ENEMY_SPEED = 3

