import pygame, sys
from pygame.locals import *
from constants import *
from Player import Player
from Platform import Platform

class Game:
    def __init__(self):
        #initialize the game screen(set size, title, etc)
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)
        self.fpsClock = pygame.time.Clock()
        self.gameRunning = True

    def run_game_loop(self):
        #The main game loop
        self.playing = True
        while self.playing:
            self.fpsClock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
            self.player.handle_input(self.platforms)



    def new_game(self):
        #reset game/start new game
        self.sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player()
        self.sprites.add(self.player)
        self.platformlist = pygame.sprite.Group()
        self.platforms = []
        x = y = 0
        level = [
            "               PPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "                                           P",
            "                                           P",
            "                                           P",
            "                                           P",
            "                                           P",
            "                                           P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                          PPPPPPP         P",
            "P                 PPPPPP                   P",
            "P                                          P",
            "P         PPPPPPP                          P",
            "P                                          P",
            "P                     PPPPPP               P",
            "P                                          P",
            "P   PPPPPPPPPPP                            P",
            "P                                          P",
            "P                 PPPPPPPPPPP              P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]
        # build the level
        for row in level:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    self.platforms.append(p)
                    self.platformlist.add(p)
                x += 32
            y += 32
            x = 0
        self.run_game_loop()

    def handle_events(self):
        # handle game events
        for event in pygame.event.get():
            #if the X button is pressed then quit/close window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.gameRunning = False




    def update(self):
        self.sprites.update()
        self.platformlist.update()


    def draw(self):
        #Draw the level
        #set background to white
        self.screen.fill(WHITE)
        #draw the sprites
        self.sprites.draw(self.screen)
        #draw the entities list to the screen (platforms)
        self.platformlist.draw(self.screen)
        pygame.display.flip()

    def display_main_menu(self):
        #display main menu
        pass

    def display_game_over_screen(selfs):
        #display the game over screen
        pass
