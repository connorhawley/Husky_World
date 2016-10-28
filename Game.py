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
            "P         PPPPPPPPPPP                                 P",
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
            # if the X button is pressed then quit/close window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.gameRunning = False
            if pygame.key.get_pressed()[K_ESCAPE]:
                print('pausing')
                self.pause()



    def update(self):
        self.sprites.update()
        self.platformlist.update()



    def draw(self):
        #Draw the level
        #set background to white
        self.screen.fill(WHITE)
        #draw the sprites list to the screen
        self.sprites.draw(self.screen)
        #draw the platform list to the screen
        self.platformlist.draw(self.screen)
        pygame.display.flip()



    def display_main_menu(self):
        #display main menu

        displayMenu = True
        mainMenuCursor = MenuCursor()
        selectedOption = 'play'
        while displayMenu:
            self.screen.fill(WHITE)
            #menu_arrow = pygame.image.load(menu_select_sprite)
            #menu_arrow_rect = menu_arrow.get_rect()
            #self.screen.blit(menu_arrow, (350, 259))
            #arrowLeft = self.print_msg_to_screen('>', BLUE, 'large', -100, -100)
            #arrowRight = self.print_msg_to_screen('<', BLUE, 'large', 100, -100)
            self.print_msg_to_screen('Play', RED, 'large', 0, -100)
            self.print_msg_to_screen('Quit', RED, 'large', 0, 100)

            mainMenuCursor.draw(self.screen)
            self.keypressed = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if mainMenuCursor.rect.y == 259:
                    if self.keypressed[K_RETURN]:
                        displayMenu = False
                    elif self.keypressed[K_DOWN]:
                        mainMenuCursor.moveToQuit()
                        self.screen.blit(mainMenuCursor.image, (300, 459))
                if mainMenuCursor.rect.y == 459:
                    if self.keypressed[K_RETURN]:
                        pygame.quit()
                    elif self.keypressed[K_UP]:
                        mainMenuCursor.moveToPlay()
                        self.screen.blit(mainMenuCursor.image, (300, 259))

            pygame.display.update()
            #self.fpsClock.tick(30)



    def display_game_over_screen(selfs):
        #display the game over screen
        pass


    def pause(self):
        self.paused = True
        self.print_msg_to_screen('Paused', BLACK, 'large')
        pygame.display.update()
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    print('unpausing')
                    self.paused = False

       #self.fpsClock.tick(3)


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

    # function to display textmessages on screen
    def print_msg_to_screen(self, msg, color, size='large', dx=0, dy=0):
        textSurface, textRect = self.text_objects(msg, color, size)
        # => get_rect().center returns a rectangle covering the surface, in this case it's the text ones
        textRect.center = (HALF_WINDOW_WIDTH + dx), (HALF_WINDOW_HEIGHT + dy)
        self.screen.blit(textSurface, textRect)
       # print(textRect.left, textRect.centery)
