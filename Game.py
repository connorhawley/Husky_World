from Camera import *
from MenuCursor import MenuCursor
from Platform import *
from Player import Player
from Coin import Coin
from Enemy import Enemy
from data.levels.Level00 import Level00
from data.levels.Level01 import Level01
from data.levels.Level02 import Level02

import threading
from math import *


class Game:
    def __init__(self):
        #initialize the game screen(set size, title, etc)
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption(TITLE)
        self.fpsClock = pygame.time.Clock()
        self.gameRunning = True

    def display_stats(self):
        threading.Timer(1.0, self.display_stats).start()
        #print("(",self.player.rect.x,",",self.player.rect.y,")")
        print("Enemy platforms: ", len(self.enemy_platform_list))
        print("Score:", self.score)

    def printfps(self):
        return str(floor(self.fpsClock.get_fps()))

    def new_game(self):
        #reset game/start new game]
        self.player_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.invincible_enemy_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.enemy_platform_list = pygame.sprite.Group()
        self.exit_blocks_list = pygame.sprite.Group()
        self.jump_blocks_list = pygame.sprite.Group()
        self.kill_blocks_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.score = 0
        self.current_level = 0
        self.levels = [Level00, Level01, Level02] #list of levels
        self.build_level(self.levels[self.current_level])  #starting level
        self.display_stats()
        self.run_game_loop()


    def run_game_loop(self):
        # The main game loop
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
            self.fpsClock.tick(FPS)

    def handle_events(self):
        # handle game events
        for event in pygame.event.get():
            # if the X button is pressed then quit/close window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                    self.gameRunning = False
            if pygame.key.get_pressed()[K_ESCAPE]:
                self.pause()
            #for testing purposes, pressing K/L goes to previous or next level
            if pygame.key.get_pressed()[K_k]:
                if self.current_level-1 < 0:
                    print("There is no previous level to go to")
                else:
                    self.build_level(self.levels[self.current_level-1])
                    self.current_level -= 1
            if pygame.key.get_pressed()[K_l]:
                if self.current_level+1 >= len(self.levels):
                    print("There is no next level to go to")
                else:
                    self.build_level(self.levels[self.current_level+1])
                    self.current_level += 1

    def update(self):
        #call update functions on lists
        self.player_list.update(self.platform_list)
        self.player.ball_list.update()
        self.enemy_list.update(self.enemy_platform_list)
        self.invincible_enemy_list.update(self.enemy_platform_list)
        self.coin_list.update()


    def build_level(self, Level):
        # build the level
        self.player_list.empty()
        self.player = Level().player
        self.player_list.add(self.player)
        self.player.ball_list = pygame.sprite.Group()
        self.invincible_enemy_list.empty()
        self.jump_blocks_list.empty()
        self.exit_blocks_list.empty()
        self.kill_blocks_list.empty()
        self.coin_list.empty()
        self.enemy_list.empty()
        self.platform_list.empty()
        self.enemy_platform_list.empty()
        self.enemy_list.add(Level().enemies)
        self.invincible_enemy_list.add(Level().invincible_enemies)
        x = y = 0
        for row in Level().level:
            for col in row:
                if col == "P":
                    p = Platform(x, y)
                    self.platform_list.add(p)
                    #self.enemy_platform_list.add(p)
                if col == "R":
                    r = EnemyPlatform(x, y)
                    self.platform_list.add(r)
                    self.enemy_platform_list.add(r)
                if col == "X":
                    e = ExitBlock(x, y)
                    self.exit_blocks_list.add(e)
                if col == "J":
                    j = JumpBlock(x, y)
                    self.jump_blocks_list.add(j)
                if col == "S":
                    s = Structure(x, y)
                    self.platform_list.add(s)
                if col == "Q":
                    q = EnemyStructure(x, y)
                    self.platform_list.add(q)
                    self.enemy_platform_list.add(q)
                if col == "K":
                    k = KillBlock(x, y)
                    self.kill_blocks_list.add(k)
                    #self.enemy_platform_list.add(k)
                if col == "I":
                    i = InvisibleBlock(x, y)
                    self.enemy_platform_list.add(i)
                if col == "B":
                    b = Brick(x, y)
                    self.platform_list.add(b)
                    #self.enemy_platform_list.add(b)
                if col == "U":
                    u = KillBlock2(x, y)
                    self.kill_blocks_list.add(u)
                    self.enemy_platform_list.add(u)
                if col == "E":
                    e = Enemy(x, y, 'normal')
                    self.enemy_list.add(e)
                if col == "Z":
                    z = Enemy(x, y, 'invincible')
                    self.invincible_enemy_list.add(z)
                if col == "C":
                    c = Coin(x, y)
                    self.coin_list.add(c)
                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0


        self.total_level_width = len(Level().level[0]) * PLATFORM_WIDTH
        self.total_level_height = len(Level().level) * PLATFORM_HEIGHT


    def draw(self):
        #set background to blue
        self.screen.fill((173,216,230))
        #create camera that stops scrolling when you reach edges:
        camera = Camera(complex_camera, self.total_level_width, self.total_level_height)
        #create camera that is centered around the player:
        #camera = Camera(simple_camera, self.total_level_width, self.total_level_height)


        camera.update(self.player)

        #draw all the sprites/images to screen and apply camera to them
        for platform in self.platform_list:
            self.screen.blit(platform.image, camera.apply(platform))

        for player in self.player_list:
            self.screen.blit(player.image, camera.apply(player))

        for enemy in self.enemy_list:
            self.screen.blit(enemy.image, camera.apply(enemy))
            #if enemy hits a jump block, then jump.
            if pygame.sprite.spritecollideany(enemy, self.jump_blocks_list):
                enemy.jump()

        for enemy in self.invincible_enemy_list:
            self.screen.blit(enemy.image, camera.apply(enemy))
            if pygame.sprite.spritecollideany(enemy, self.jump_blocks_list):
                enemy.jump()

        #restart the level if the player touches an enemy
        if pygame.sprite.groupcollide(self.enemy_list, self.player_list, False, False):
            self.build_level(self.levels[self.current_level])
            self.score -= 100
        if pygame.sprite.groupcollide(self.invincible_enemy_list, self.player_list, False, False):
            self.score -= 100
            self.build_level(self.levels[self.current_level])

        #draw exit blocks to the screen. If player hits the block then go to next level.
        for exitblock in self.exit_blocks_list:
            self.screen.blit(exitblock.image, camera.apply(exitblock))
            if exitblock.rect.colliderect(self.player.rect):
                self.current_level += 1
                self.score += 100
                self.build_level(self.levels[self.current_level])

        for killblock in self.kill_blocks_list:
            self.screen.blit(killblock.image, camera.apply(killblock))

        for coin in self.coin_list:
            self.screen.blit(coin.image, camera.apply(coin))



        if pygame.sprite.groupcollide(self.kill_blocks_list, self.player_list, False, False):
            self.build_level(self.levels[self.current_level])
            self.score -= 100

        #+200 score if you get a coin
        if pygame.sprite.groupcollide(self.player_list, self.coin_list, False, True):
            self.score += 200

        #draw all basketballs to the screen and apply camera, and check for collison
        #if ball hits platform, delete ball. if hits enenmy, delete enemy & ball
        for ball in self.player.ball_list:
            self.screen.blit(ball.image, camera.apply(ball))


        pygame.sprite.groupcollide(self.player.ball_list, self.platform_list, True, False)
        pygame.sprite.groupcollide(self.player.ball_list, self.invincible_enemy_list, True, False)

        #+10 score if you kill enemy
        if pygame.sprite.groupcollide(self.player.ball_list, self.enemy_list, True, True):
            self.score += 10

        self.print_msg_to_screen(self.printfps(), WHITE, 'small', -HALF_WINDOW_WIDTH+50, -HALF_WINDOW_HEIGHT+100)
        self.print_msg_to_screen('Score:', WHITE, 'small', -HALF_WINDOW_WIDTH +55 , -HALF_WINDOW_HEIGHT + 20)
        self.print_msg_to_screen(str(self.score), WHITE, 'small', -HALF_WINDOW_WIDTH + 150, -HALF_WINDOW_HEIGHT + 20)

        pygame.display.update()


    def display_main_menu(self):
        #display main menu
        main_menu_open = True
        at_menu_bottom = False
        at_menu_top = True
        # create mouse cursor arrow
        mainMenuCursor = MenuCursor()
        selectedOption = 'play'
        while main_menu_open:
            #set background to white
            self.screen.fill((173,216,230))
            #draw play and quit text to the screen
            score_txt = 'Score: +10 for killing enemy, +100 for finishing level, -100 for dying'
            self.print_msg_to_screen('Play', NAVY_BLUE, 'large', 0, -100)
            self.print_msg_to_screen('Quit', NAVY_BLUE, 'large', 0, 100)
            self.print_msg_to_screen(score_txt, NAVY_BLUE, 'small', 0, 300)
            #self.print_msg_to_screen('Test', NAVY_BLUE, 'large', 0, 300)
            #draw menu arrow cursor on the screen
            mainMenuCursor.draw(self.screen)
            keypressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if keypressed[K_s]:
                    if at_menu_bottom:
                        pass
                    else:
                        mainMenuCursor.moveDown()
                elif keypressed[K_w]:
                    if at_menu_top:
                        pass
                    else:
                        mainMenuCursor.moveUp()
                    #259 is the center y coordinate of the Play text
                if mainMenuCursor.rect.y == 259:
                    at_menu_bottom = False
                    at_menu_top = True
                    if keypressed[K_RETURN]:
                        main_menu_open = False
                    #459 is the center y coordinate of the quit text
                if mainMenuCursor.rect.y == 459:
                    at_menu_top = False
                    at_menu_bottom = True
                    if keypressed[K_RETURN]:
                        pygame.quit()
                # if mainMenuCursor.rect.y == 659:
                #     at_menu_top = False
                #     at_menu_bottom = True


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
