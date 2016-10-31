import pygame, sys
from pygame.locals import *
from constants import *
from Player import Player
from Platform import Platform
from Camera import *
from MenuCursor import MenuCursor

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
     #   self.display_main_menu()
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
            "P         PPPPPPPPPPP                      P",
            "P                                          P",
            "P                                          P",
            "P                          PPPPPPP         P",
            "P                 PPPPPP                   P",
            "P                                          P",
            "P      PPPPPPPPPP                          P",
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

        self.total_level_width = len(level[0])*32
        self.total_level_height = len(level)*32

        self.run_game_loop()

    def handle_events(self):
        # handle game events
        for event in pygame.event.get():
            # if the X button is pressed then quit/close window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.gameRunning = False
            if pygame.key.get_pressed()[K_ESCAPE]:
                print('pausing')
                self.pause()



    def update(self):
        #update sprite and platform lists
        self.sprites.update()
        self.platformlist.update()


    def draw(self):
        #set background to white
        self.screen.fill(WHITE)
        #create camera that stops scrolling when you reach edges
        camera = Camera(complex_camera, self.total_level_width, self.total_level_height)
        #create camera that is centered around the player
        #camera = Camera(simple_camera, self.total_level_width, self.total_level_height)
        camera.update(self.player)
        for sprite in self.sprites:
            self.screen.blit(sprite.image, camera.apply(sprite))
        for platform in self.platformlist:
            self.screen.blit(platform.image, camera.apply(platform))
        pygame.display.flip()



    def display_main_menu(self):
        #display main menu

        main_menu_open = True
        # create mouse cursor arrow
        mainMenuCursor = MenuCursor()
        selectedOption = 'play'
        while main_menu_open:

            #set background to white
            self.screen.fill(WHITE)
            #draw play and quit text to the screen
            self.print_msg_to_screen('Play', RED, 'large', 0, -100)
            self.print_msg_to_screen('Quit', RED, 'large', 0, 100)
            #draw menu arrow cursor on the screen
            mainMenuCursor.draw(self.screen)
            self.keypressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #259 is the center y coordinate of the Play text
                if mainMenuCursor.rect.y == 259:
                    if self.keypressed[K_RETURN]:
                        main_menu_open = False
                    elif self.keypressed[K_DOWN]:
                        mainMenuCursor.moveToQuit()
                        self.screen.blit(mainMenuCursor.image, (350, 459))
                    #459 is the center y coordinate of the Play text
                if mainMenuCursor.rect.y == 459:
                    if self.keypressed[K_RETURN]:
                        pygame.quit()
                    elif self.keypressed[K_UP]:
                        mainMenuCursor.moveToPlay()
                        self.screen.blit(mainMenuCursor.image, (350, 259))

            pygame.display.update()



    def display_game_over_screen(selfs):
        #display the game over screen
        pass


    def pause(self):

        #pause the game when escape key is pressed
        self.paused = True
        self.print_msg_to_screen('Paused, press Q to quit', BLACK, 'large')
        pygame.display.update()
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if pygame.key.get_pressed()[pygame.K_q]:
                    pygame.quit()
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    #print('unpausing')
                    self.paused = False

       #self.fpsClock.tick(3)


    #function to create text object on screen with specific message, color, size(Sizes specific in constants script)
    def text_objects(self, msg, color, size):
        if size == 'small':
            textSurface = SMALLFONT.render(msg, True, color)
            return textSurface, textSurface.get_rect()
        elif size == 'medium':
            textSurface = MEDIUMFONT.render(msg, True, color)
            return textSurface, textSurface.get_rect()
        elif size == 'large':
            textSurface = LARGEFONT.render(msg, True, color)
            return textSurface, textSurface.get_rect()

    # function to display text messages on screen.
    # (creates a message that can be offset based off of the center of the window using dx and dy)
    def print_msg_to_screen(self, msg, color, size='large', dx=0, dy=0):
        textSurface, textRect = self.text_objects(msg, color, size)
        # => get_rect().center returns a rectangle covering the surface, in this case it's the text ones
        textRect.center = (HALF_WINDOW_WIDTH + dx), (HALF_WINDOW_HEIGHT + dy)
        self.screen.blit(textSurface, textRect)
        return [textRect.left, textRect.centery]
       # print(textRect.left, textRect.centery)
