from Camera import *
from MenuCursor import MenuCursor
from Platform import *
from Coin import Coin
from Enemy import Enemy
from data.levels.Level00 import Level00
from data.levels.Level01 import Level01
from data.levels.Level02 import Level02

import threading, pickle, shelve
from math import floor


class Game:
    def __init__(self):
        #initialize the game screen(set size, title, etc)
        pygame.init()
        pygame.mixer.init()
        self.screen = SCREEN
        pygame.display.set_caption(TITLE)
        self.fpsClock = pygame.time.Clock()
        self.gameRunning = True
        self.playing = True
        self.noclipping = False


    def display_stats(self):
        threading.Timer(1.0, self.display_stats).start()
        #print("Enemy platforms: ", len(self.enemy_platform_list))
        #print("Platforms:", len(self.platform_list))
        #print("FPS:", self.printfps())
        #print("(",self.player.rect.x,",",self.player.rect.y,")",'\n')
        #print("Score:", self.score)
        #print(self.score, self.level_score)

    def printfps(self):
        return str(floor(self.fpsClock.get_fps()))

    def get_high_score(self):
        high_score = 0
        try:
            high_score_file = open("high_score.txt", "r")
            high_score = int(high_score_file.read())
            high_score_file.close()
        except IOError:
            # Error reading file, no high score
            print("There is no high score yet.")
        except ValueError:
            # There's a file there, but we don't understand the number.
            print("Invalid number, starting at zero.")

        return high_score

    def save_high_score(self, new_high_score):
        try:
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()
        except IOError:
            print("Unable to save the high score.")


    def new_game(self):
        #reset game/start new game]
        self.get_high_score()
        self.player_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.invincible_enemy_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.enemy_platform_list = pygame.sprite.Group()
        self.fake_blocks_list = pygame.sprite.Group()
        self.exit_blocks_list = pygame.sprite.Group()
        self.jump_blocks_list = pygame.sprite.Group()
        self.kill_blocks_list = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.score = 0
        self.level_score = 0
        self.current_level = 0
        self.levels = [Level00, Level01, Level02] #list of levels
        self.display_main_menu()
        self.build_level(self.levels[self.current_level])  #starting level
       # self.display_stats()
        self.run_game_loop()


    def run_game_loop(self):
        # The main game loop
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
                    pygame.quit()
            if pygame.key.get_pressed()[K_ESCAPE]:
                self.display_pause_menu()
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
            # if pygame.key.get_pressed()[K_KP5]:
            #     self.save(self.player, self.enemy_list, self.invincible_enemy_list, self.coin_list, self.current_level)
            #
            # if pygame.key.get_pressed()[K_KP2]:
            #     self.player2, self.enemy_list, self.invincible_enemy_list, self.coin_list, self.current_level = self.load()
            #     self.resume_level(self.levels[self.current_level])
            #     self.player.image = Player(0,0).image
            #     self.player.rect = self.player2.rect
            #     for e in self.enemy_list: e.image = Enemy(e.rect.x, e.rect.y).image
            #     for e in self.invincible_enemy_list: e.image = Enemy(e.rect.x, e.rect.y, 'invincible').image
            #     for c in self.coin_list: c.image = Coin(c.rect.x, c.rect.y).image


            # press n to noclip
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_n:
                    self.noclipping = not self.noclipping

    def update(self):
        #call update functions on lists
        if self.noclipping == False:
            self.player_list.update(self.platform_list)
        else:
            self.player.noclip()

        self.player.ball_list.update()
        self.enemy_list.update(self.enemy_platform_list)
        self.invincible_enemy_list.update(self.enemy_platform_list)
        self.coin_list.update()

    #
    # def save(self, player ,enemies, invenemies, coins, level):
    #     f = shelve.open("save.bin")
    #     for p in self.player_list: p.image = None
    #     for e in self.enemy_list: e.image = None
    #     for e in self.invincible_enemy_list: e.image = None
    #     for e in self.coin_list: e.image = None
    #     f['player'] = player
    #     f['enemies'] = enemies
    #     f['invenemies'] = invenemies
    #     f['coins'] = coins
    #     f['level'] = level
    #     f.close()
    #     self.new_game()
    #
    # def load(self):
    #     try:
    #         f = shelve.open("save.bin")
    #         return f['player'], f['enemies'], f['invenemies'], f['coins'], f['level']
    #     except KeyError:
    #         return None
    #     finally:
    #         f.close()
    #
    # def resume_level(self, Level):
    #         # build the level
    #         self.player_list.empty()
    #         self.player = Level().player
    #         self.platform_list.empty()
    #         self.jump_blocks_list.empty()
    #         self.exit_blocks_list.empty()
    #         self.kill_blocks_list.empty()
    #         self.fake_blocks_list.empty()
    #         self.platform_list.empty()
    #         self.player_list.add(self.player)
    #         self.player.ball_list = pygame.sprite.Group()
    #         self.invincible_enemy_list.empty()
    #
    #         x = y = 0
    #         for row in Level().level:
    #             for col in row:
    #                 if col == "P":
    #                     p = Platform(x, y)
    #                     self.platform_list.add(p)
    #                     #self.enemy_platform_list.add(p)
    #                 if col == "R":
    #                     r = EnemyPlatform(x, y)
    #                     self.platform_list.add(r)
    #                     self.enemy_platform_list.add(r)
    #                 if col == "X":
    #                     e = ExitBlock(x, y)
    #                     self.exit_blocks_list.add(e)
    #                 if col == "J":
    #                     j = JumpBlock(x, y)
    #                     self.jump_blocks_list.add(j)
    #                 if col == "S":
    #                     s = Structure(x, y)
    #                     self.platform_list.add(s)
    #                 if col == "Q":
    #                     q = EnemyStructure(x, y)
    #                     self.platform_list.add(q)
    #                     self.enemy_platform_list.add(q)
    #                 if col == "K":
    #                     k = KillBlock(x, y)
    #                     self.kill_blocks_list.add(k)
    #                     # self.enemy_platform_list.add(k)
    #                 if col == "I":
    #                     i = InvisibleBlock(x, y)
    #                     self.enemy_platform_list.add(i)
    #                 if col == "B":
    #                     b = Brick(x, y)
    #                     self.platform_list.add(b)
    #                     # self.enemy_platform_list.add(b)
    #                 if col == "U":
    #                     u = KillBlock2(x, y)
    #                     self.kill_blocks_list.add(u)
    #                     self.enemy_platform_list.add(u)
    #                 if col == "F":
    #                     f = FakePlatform(x, y)
    #                     self.fake_blocks_list.add(f)
    #                 x += PLATFORM_WIDTH
    #             y += PLATFORM_HEIGHT
    #             x = 0

    def build_level(self, Level):
        # build the level
        self.level_score = 0
        self.player_list.empty()
        self.player = Level().player
        self.player_list.add(self.player)
        self.player.ball_list = pygame.sprite.Group()
        self.invincible_enemy_list.empty()
        self.jump_blocks_list.empty()
        self.exit_blocks_list.empty()
        self.kill_blocks_list.empty()
        self.fake_blocks_list.empty()
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
                if col == "F":
                    f = FakePlatform(x, y)
                    self.fake_blocks_list.add(f)
                x += PLATFORM_WIDTH
            y += PLATFORM_HEIGHT
            x = 0


        self.total_level_width = len(Level().level[0]) * PLATFORM_WIDTH
        self.total_level_height = len(Level().level) * PLATFORM_HEIGHT

    def fade(self):
        blk = pygame.Surface(SIZE)
        #self.paused = True
        for i in range(255):
            blk.fill(BLACK)
            blk.set_alpha(i)
            self.print_msg_to_screen('YOU DIED', WHITE, blk, 'large')
            self.screen.blit(blk, (0, 0))
            pygame.display.update(blk.get_rect())
            pygame.time.delay(10)
        #self.paused = False

    def draw(self):
        #set background to blue
        self.screen.fill((173,216,230))
        #create camera that stops scrolling when you reach edges:
        camera = Camera(complex_camera, self.total_level_width, self.total_level_height)
        #create camera that is centered around the player:
        #camera = Camera(simple_camera, self.total_level_width, self.total_level_height)

        camera.update(self.player)

        #draw all the platforms to screen and apply camera to them
        for platform in self.platform_list:
            self.screen.blit(platform.image, camera.apply(platform))

        # draw the enemies to screen and apply camera to them. If enemy touches jump block then the enemy will jump
        for enemy in self.enemy_list:
            self.screen.blit(enemy.image, camera.apply(enemy))
            #if enemy hits a jump block, then jump.
            if pygame.sprite.spritecollideany(enemy, self.jump_blocks_list):
                enemy.jump()

        # draw the invincible enemies to screen and apply camera to them. If enemy touches jump block then the enemy will jump
        for enemy in self.invincible_enemy_list:
            self.screen.blit(enemy.image, camera.apply(enemy))
            if pygame.sprite.spritecollideany(enemy, self.jump_blocks_list):
                enemy.jump()

        #if player jumps on enemy's head, then kill the enemy. If player runs into enemy, then restart level and -100 points
        for player, enemies in pygame.sprite.groupcollide(self.player_list, self.enemy_list, False, False).items():
            if self.player.dy > 0:
                for e in enemies:
                    if e.rect.top+32 > self.player.rect.bottom:
                        #print(e.rect.top, self.player.rect.bottom)
                        self.score += 10
                        self.level_score += 10
                        self.player.dy = -10
                        self.enemy_list.remove(e)
                        pygame.mixer.music.load("data/Audio/Jump_on_enemy.wav")
                        pygame.mixer.music.play(1, 0)
            else:
                self.screen.fill((173,216,230))
                self.fade()
                self.score -= 100 + self.level_score
                self.build_level(self.levels[self.current_level])


        if pygame.sprite.groupcollide(self.invincible_enemy_list, self.player_list, False, False):
            self.screen.fill((173, 216, 230))
            self.fade()
            self.score -= 100 + self.level_score
            self.build_level(self.levels[self.current_level])


        #draw exit blocks to the screen. If player hits the block then go to next level.
        for exitblock in self.exit_blocks_list:
            self.screen.blit(exitblock.image, camera.apply(exitblock))
            if exitblock.rect.colliderect(self.player.rect):
                if ((exitblock.rect.centerx - 32) - (self.player.rect.centerx - 32))  < 32:
                    if self.current_level + 2 > len(self.levels):
                        print("No next level.")
                    else:
                        self.current_level += 1
                        self.score += 100
                        self.level_score += 100
                        self.build_level(self.levels[self.current_level])
                        pygame.mixer.music.load("data/Audio/Level_dunk.wav")
                        pygame.mixer.music.play(1, 0)

        # draw the player to screen and apply camera to them
        for player in self.player_list:
            self.screen.blit(player.image, camera.apply(player))

        for killblock in self.kill_blocks_list:
            self.screen.blit(killblock.image, camera.apply(killblock))

        for fakeblock in self.fake_blocks_list:
            self.screen.blit(fakeblock.image, camera.apply(fakeblock))

        for coin in self.coin_list:
            self.screen.blit(coin.image, camera.apply(coin))

        if pygame.sprite.groupcollide(self.kill_blocks_list, self.player_list, False, False):
            self.screen.fill((173, 216, 230))
            self.fade()
            self.score -= 100 + self.level_score
            self.build_level(self.levels[self.current_level])


        #+200 score if you get a coin
        if pygame.sprite.groupcollide(self.player_list, self.coin_list, False, True):
            self.score += 200
            self.level_score += 200
            pygame.mixer.music.load('data/Audio/Coin')
            pygame.mixer.music.play(1, 0)

        #draw all basketballs to the screen and apply camera, and check for collison
        #if ball hits platform, delete ball. if hits enenmy, delete enemy & ball
        for ball in self.player.ball_list:
            self.screen.blit(ball.image, camera.apply(ball))


        pygame.sprite.groupcollide(self.player.ball_list, self.platform_list, True, False)
        pygame.sprite.groupcollide(self.player.ball_list, self.invincible_enemy_list, True, False)

        #+10 score if you kill enemy
        if pygame.sprite.groupcollide(self.enemy_list, self.player.ball_list, True, True):
            self.score += 10
            self.level_score += 10
            pygame.mixer.music.load('data/Audio/Jump_on_enemy.wav')
            pygame.mixer.music.play(1,0)

        #print score and fps in top right corner.
        self.print_msg_to_screen('fps: '+self.printfps(), WHITE, self.screen, 'small', -HALF_WINDOW_WIDTH+60, -HALF_WINDOW_HEIGHT+70)
        self.print_msg_to_screen('Score:', WHITE, self.screen, 'small', -HALF_WINDOW_WIDTH +55, -HALF_WINDOW_HEIGHT + 20)
        self.print_msg_to_screen(str(self.score), WHITE, self.screen, 'small', -HALF_WINDOW_WIDTH + 150, -HALF_WINDOW_HEIGHT + 20)

        pygame.display.update()


    def display_main_menu(self):
        #display main menu
        main_menu_open = True
        at_menu_bottom = False
        at_menu_top = True
        #create menu surface
        bg = pygame.Surface(SIZE)
        pic = MAIN_MENU
        bg.blit(pic, (0,0))

        #blit all of the menu texts to the screen
        bg.blit(self.textOutline(XLFONT, 'SUPER', NAVY_BLUE, WHITE), (338,30))
        bg.blit(self.textOutline(XLFONT, 'HUSKY WORLD', NAVY_BLUE, WHITE,), (138, 115))
        bg.blit(self.textOutline(LARGEFONT, 'Play', NAVY_BLUE, WHITE), (HALF_WINDOW_WIDTH - 103, HALF_WINDOW_HEIGHT - 40))
        bg.blit(self.textOutline(LARGEFONT, 'Quit', NAVY_BLUE, WHITE), (HALF_WINDOW_WIDTH - 89, HALF_WINDOW_HEIGHT + 60))
        bg.blit(self.textOutline(LARGEFONT, 'Help', NAVY_BLUE, WHITE), (HALF_WINDOW_WIDTH - 103, HALF_WINDOW_HEIGHT + 160))
        bg.blit(self.textOutline(MEDIUMFONT, 'High Score:', NAVY_BLUE, WHITE), (45, 623))
        bg.blit(self.textOutline(MEDIUMFONT, str(self.get_high_score()), NAVY_BLUE, WHITE), (133, 700))
        #self.print_msg_to_screen('SUPER', NAVY_BLUE, bg, 'extralarge', 0, -300)
        #self.print_msg_to_screen('HUSKY WORLD', NAVY_BLUE, bg, 'extralarge', 0, -215)
        #self.print_msg_to_screen('Play', NAVY_BLUE, bg, 'large', 0, 0)
        #self.print_msg_to_screen('Quit', NAVY_BLUE, bg, 'large', 0, 100)
        #self.print_msg_to_screen('Help', NAVY_BLUE, bg, 'large', 0, 200)
        #self.print_msg_to_screen('High Score:', NAVY_BLUE, bg, 'small', -300, 250)

        bg_rect = bg.get_rect()

        # create mouse cursor arrow
        menu_cursor = MenuCursor()
        while main_menu_open:
            #draw menu arrow cursor on the screen
            #print(pygame.mouse.get_pos())
            self.screen.blit(bg, bg_rect)
            menu_cursor.draw(self.screen)
            keypressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if keypressed[K_s]:
                    if at_menu_bottom:
                        pass
                    else:
                        menu_cursor.moveDown()
                elif keypressed[K_w]:
                    if at_menu_top:
                        pass
                    else:
                        menu_cursor.moveUp()
                    #259 is the center y coordinate of the Play option
                if menu_cursor.rect.y == 359:
                    at_menu_bottom = False
                    at_menu_top = True
                    if keypressed[K_RETURN]:
                        main_menu_open = False
                    #359 is the center y coordinate of the quit option
                if menu_cursor.rect.y == 459:
                    at_menu_top = False
                    at_menu_bottom = False
                    if keypressed[K_RETURN]:
                        pygame.quit()
                    #459 is the center y coordinate of the Help option
                if menu_cursor.rect.y == 559:
                     at_menu_top = False
                     at_menu_bottom = True
                     if keypressed[K_RETURN]:
                        main_menu_open = False
                        self.display_help_menu()
            pygame.display.update()

    #display the help menu
    def display_help_menu(self):
        help_menu_open = True
        menu_image = HELP_MENU
        menu_rect = menu_image.get_rect()

        while help_menu_open:
            self.screen.blit(menu_image, menu_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                if pygame.key.get_pressed()[K_ESCAPE]:
                    help_menu_open = False
                    self.display_main_menu()
            pygame.display.update()

    #display game over screen
    def display_game_over_screen(self):
        #display the game over screen
        pass

    #display pause menu when escape is pressed
    def display_pause_menu(self):
        #pause the game when escape key is pressed
        self.paused = True
        bg = pygame.Surface([1024,768])
        bg.fill((173,216,230))

        self.print_msg_to_screen('Score:', WHITE, bg, 'small', -HALF_WINDOW_WIDTH + 55, -HALF_WINDOW_HEIGHT + 20)
        self.print_msg_to_screen(str(self.score), WHITE, bg, 'small', -HALF_WINDOW_WIDTH + 150, -HALF_WINDOW_HEIGHT + 20)
        self.print_msg_to_screen('Paused', NAVY_BLUE, bg, 'large', 0, -200)
        self.print_msg_to_screen('Resume', NAVY_BLUE, bg, 'large', 0, 0)
        self.print_msg_to_screen('Main Menu', NAVY_BLUE, bg, 'large', 0, 100)
        self.print_msg_to_screen('Quit', NAVY_BLUE, bg, 'large', 0, 200)


        bg_rect = bg.get_rect()
        pause_cursor = MenuCursor()
        pause_cursor.rect.x = 284
        pause_cursor.rect.y = 362
        at_menu_top = True
        at_menu_bottom = False

        while self.paused:
            self.screen.blit(bg, bg_rect)
            self.screen.blit(pause_cursor.image, (pause_cursor.rect.x, pause_cursor.rect.y))

            keypressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                if keypressed[K_s]:
                    if at_menu_bottom:
                        pass
                    else:
                        pause_cursor.moveDown()
                elif keypressed[K_w]:
                    if at_menu_top:
                        pass
                    else:
                        pause_cursor.moveUp()
                if pause_cursor.rect.y == 362:
                    pause_cursor.rect.x = 284
                    at_menu_bottom = False
                    at_menu_top = True
                    if keypressed[K_RETURN]:
                        self.paused = False
                if pause_cursor.rect.y == 462:
                    pause_cursor.rect.x = 224
                    at_menu_top = False
                    at_menu_bottom = False
                    if keypressed[K_RETURN]:
                        if self.score > self.get_high_score():
                            self.save_high_score(self.score)
                        self.new_game()
                if pause_cursor.rect.y == 562:
                     pause_cursor.rect.x = 349
                     at_menu_top = False
                     at_menu_bottom = True
                     if keypressed[K_RETURN]:
                         if self.score > self.get_high_score():
                            self.save_high_score(self.score)
                         pygame.quit()
                         
            pygame.display.update()


    #create hollow text
    def textHollow(self, font, message, fontcolor):
        notcolor = [c ^ 0xFF for c in fontcolor]
        base = font.render(message, 0, fontcolor, notcolor)
        size = base.get_width() + 2, base.get_height() + 2
        img = pygame.Surface(size, 16)
        img.fill(notcolor)
        base.set_colorkey(0)
        img.blit(base, (0, 0))
        img.blit(base, (2, 0))
        img.blit(base, (0, 2))
        img.blit(base, (2, 2))
        base.set_colorkey(0)
        base.set_palette_at(1, notcolor)
        img.blit(base, (1, 1))
        img.set_colorkey(notcolor)
        return img

    #create outlined text
    def textOutline(self, font, message, fontcolor, outlinecolor):
        base = font.render(message, 0, fontcolor)
        outline = self.textHollow(font, message, outlinecolor)
        img = pygame.Surface(outline.get_size(), 16)
        img.blit(base, (1, 1))
        img.blit(outline, (0, 0))
        img.set_colorkey(0)
        return img

    #function to create text object on screen with specific message, color, size(Sizes specific in constants script)
    def text_objects(self, msg, color, size):
        if size == 'small':
            text_surface = SMALLFONT.render(msg, True, color)
            return text_surface, text_surface.get_rect()
        elif size == 'medium':
            text_surface = MEDIUMFONT.render(msg, True, color)
            return text_surface, text_surface.get_rect()
        elif size == 'large':
            text_surface = LARGEFONT.render(msg, True, color)
            return text_surface, text_surface.get_rect()
        elif size == 'extralarge':
            text_surface = XLFONT.render(msg, True, color)
            return text_surface, text_surface.get_rect()

    # function to display text messages on screen.
    # (creates a message that can be offset based off of the center of the window using dx and dy)
    def print_msg_to_screen(self, msg, color, surface, size='large', dx=0, dy=0):
        text_surface, text_rect = self.text_objects(msg, color, size)
        # => get_rect().center returns a rectangle covering the surface, in this case it's the text ones
        text_rect.center = (HALF_WINDOW_WIDTH + dx), (HALF_WINDOW_HEIGHT + dy)
        surface.blit(text_surface, text_rect)
        return [text_rect.left, text_rect.centery]
