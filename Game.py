from Camera import *
from MenuCursor import MenuCursor
from Platform import Platform
from Player import Player
from ExitBlock import ExitBlock
from data.levels.Level00 import Level00
from data.levels.Level01 import Level01


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
        #reset game/start new game]

        self.player_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.exitblocks = pygame.sprite.Group()
        self.platforms = []
        self.levels = [Level00, Level01] #list of levels
        self.build_level(self.levels[0])  #starting level
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
                #print('pausing')
                self.pause()

    def update(self):
        #update sprite and platform lists
        self.player_list.update()
        self.platform_list.update()
        self.player.ball_list.update()
        self.enemy_list.update()
        for e in self.enemy_list:
            e.move(self.platform_list, self.player)



    def build_level(self, Level):
        # build the level

        self.player_list.empty()
        self.player = Player()
        self.player.ball_list = pygame.sprite.Group()
        self.player_list.add(self.player)
        self.platforms = []
        self.exitblocks.empty()
        self.enemy_list.empty()
        self.platform_list.empty()
        self.enemy_list.add(Level().enemies)
        x = y = 0
        for row in Level().level:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    self.platforms.append(p)
                    self.platform_list.add(p)
                if col == "E":
                    e = ExitBlock(x, y)
                    self.exitblocks.add(e)
                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0

        self.total_level_width = len(Level().level[0]) * PLATFORM_WIDTH
        self.total_level_height = len(Level().level) * PLATFORM_HEIGHT



    def draw(self):
        #set background to white
        self.screen.fill(WHITE)
        #create camera that stops scrolling when you reach edges
        camera = Camera(complex_camera, self.total_level_width, self.total_level_height)
        #create camera that is centered around the player
        #camera = Camera(simple_camera, self.total_level_width, self.total_level_height)
        camera.update(self.player)

        #draw all the sprites/images to screen and apply camera to them
        for platform in self.platform_list:
            self.screen.blit(platform.image, camera.apply(platform))
        for sprite in self.player_list:
            self.screen.blit(sprite.image, camera.apply(sprite))
        for enemy in self.enemy_list:
            self.screen.blit(enemy.image, camera.apply(enemy))
            #if any enemy hits the player then restart the game
            if pygame.sprite.spritecollideany(enemy, self.player_list):
                self.new_game()
                #could also just make it restart current level.
        for exitblock in self.exitblocks:
            self.screen.blit(exitblock.image, camera.apply(exitblock))
            if exitblock.rect.colliderect(self.player.rect):
                self.build_level(self.levels[1])
                #go to next level if touch block?
        # display death msg, save score, move back to start position

        #draw all basketballs to the screen and apply camera, and check for collison
        #if ball hits platform, delete ball. if hits enenmy, delete enemy & platform
        for ball in self.player.ball_list:
            self.screen.blit(ball.image, camera.apply(ball))
            self.block_hit_list = pygame.sprite.spritecollide(ball, self.platform_list, False)
            self.enemy_ball_hit_list = pygame.sprite.groupcollide(self.player.ball_list, self.enemy_list, True, True)
            for block in self.block_hit_list:
                self.player.ball_list.remove(ball)

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
            self.print_msg_to_screen('Play', NAVY_BLUE, 'large', 0, -100)
            self.print_msg_to_screen('Quit', NAVY_BLUE, 'large', 0, 100)
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
                    #459 is the center y coordinate of the quit text
                if mainMenuCursor.rect.y == 459:
                    if self.keypressed[K_RETURN]:
                        pygame.quit()
                    elif self.keypressed[K_UP]:
                        mainMenuCursor.moveToPlay()

            pygame.display.update()


    def display_game_over_screen(self):
        #display the game over screen
        pass


    def pause(self):
        #pause the game when escape key is pressed
        self.paused = True
        self.print_msg_to_screen('Paused, press Q to quit', BLACK, 'medium')
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

    # def render_tiles_to_screen(self, filename):
    #     tmx_data = load_pygame(filename)
    #     if tmx_data.background_color:
    #         self.screen.fill(pygame.Color(self.tmx_data.background_color))
    #
    #     # iterate over all the visible layers, then draw them
    #     # according to the type of layer they are.
    #     for layer in tmx_data.visible_layers:
    #
    #         # draw map tile layers
    #         if isinstance(layer, pytmx.TiledTileLayer):
    #
    #             # iterate over the tiles in the layer
    #             for x, y, image in layer.tiles():
    #                 self.screen.blit(image, (x * tmx_data.tilewidth, y * tmx_data.tileheight))
    #
    #         # draw object layers
    #         elif isinstance(layer, pytmx.TiledObjectGroup):
    #
    #             # iterate over all the objects in the layer
    #             for obj in layer:
    #
    #                 # objects with points are polygons or lines
    #                 if hasattr(obj, 'points'):
    #                     pygame.draw.lines(self.screen, self.poly_color,
    #                                       obj.closed, obj.points, 3)
    #
    #                 # some object have an image
    #                 elif obj.image:
    #                     self.screen.blit(obj.image, (obj.x, obj.y))
    #
    #                 # draw a rect for everything else
    #                 else:
    #                     pygame.draw.rect(self.screen, self.rect_color,
    #                                      (obj.x, obj.y, obj.width, obj.height), 3)
    #
    #         # draw image layers
    #         elif isinstance(layer, pytmx.TiledImageLayer):
    #             if layer.image:
    #                 self.screen.blit(layer.image, (0, 0))