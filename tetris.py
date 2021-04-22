import pygame
import sys
from button import Button
from settings import Settings
from gamestats import GameStats
from game_windows import *
import os
from block import *


class Tetris:

    def __init__(self):
        """initialize game and create game resources"""
        pygame.init()  # initialize background settings
        self.settings = Settings()  # load settings
        self.stats = GameStats(self)  # initial game statistics
        self.stats.game_active = False
        #self.stats.highscore = self.stats._get_highscore()  # get highscore
        # self.stats.game_active = False  # game is active
        self.clock = pygame.time.Clock()  # get clock for fps limitation
        self._set_screen()  # set game window resolution and title
        #self.scoreboard = Scoreboard(self)  # set scoreboard
        #self.scoreboard.prep_score()
        #self.scoreboard.prep_highscore()
        #self.ship = Ship(self)  # initialize ship
        #self.bullets = pygame.sprite.Group()  # create sprite group for bullets
        #self.aliens = pygame.sprite.Group()  # create sprite group for aliens
        self.segment_stack = []
        self.play_button = Button(self, "Start Game")
        self.play_button.draw_button()
        pygame.display.flip()  # only make recently drawn screen visible

    def run_game(self):
        """start main loop for game"""
        while True:
            self._check_events()  # check user input
            self.dt = self.clock.tick(self.settings.fps)  # limit game fps
            if self.stats.game_active:
                self._update_physics(self)
                self._update_screen()  # screen updater
                # self._update_physics()  # check game mechanics physics

    def _set_screen(self):
        """set screen properties"""
        # set game window to predefined resolution in 'settings'
        # the self.screen object here is a 'surface'
        # any visual element in the game window is its own surface
        if self.settings.screen_mode == 'fullscreen':
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        elif self.settings.screen_mode == 'window':
            self.screen = pygame.display.set_mode(
                (self.settings.window_screen_width, self.settings.window_screen_height))
        # save screen resolution
        displayInfo = pygame.display.Info()
        self.settings.screen_width = displayInfo.current_w
        self.settings.screen_height = displayInfo.current_h
        # set window title
        pygame.display.set_caption("Tetris")
        # load background image and scale
        self.screen.fill(self.settings.bg_color)
        # create game window
        self.game_window = GameWindow(self)
        # create next block window
        self.next_window = NextWindow(self)
        self.game_window.draw()
        self.next_window.draw()




        #path = os.path.dirname(__file__)
        #self.background_image = pygame.image.load(rf"{path}\images\background.png")
        #self.background_image = pygame.transform.scale(self.background_image, (
        #self.settings.screen_width + 2, self.settings.screen_height + 2))

    def _play_music(self):
        """play background music in endless loop"""
        path = os.path.dirname(__file__)
        pygame.mixer.music.load(rf"{path}\theme.mp3")
        pygame.mixer.music.play(-1, 0.0)

    def _check_events(self):
        """event loop to listen to user input"""
        for event in pygame.event.get():  # watch for keyboard and mouse events
            if event.type == pygame.QUIT:  # check game exit by hitting 'x'
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # check if key is pressed down
                self._check_keydown_events(event)
            elif event.type == pygame.K_SPACE:  # check if key is pressed down
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # check if key is released again
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # check if mouse button pressed
                self._check_mousebutton_events(event)

    def _check_keydown_events(self, event):
        """event checks when keys are pressed"""
        if event.key == pygame.K_ESCAPE:  # check game exit by typing 'esc'
            sys.exit()
        elif event.key == pygame.K_LEFT:  # check move left
            print("left")
            # self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:  # check move right
            print("right")
            #self.ship.moving_right = True
        elif event.key == pygame.K_SPACE:
            self.new_block = Block(self)
        elif event.key == pygame.K_DOWN:  # check move down
            print("down")

    def _check_keyup_events(self, event):
        """event checks when keys are released"""
        if event.key == pygame.K_LEFT:  # check move left
            print("losgelassen")
            # self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:  # check move right
            print("losgelassen")
            #self.ship.moving_right = False
        elif event.key == pygame.K_DOWN:  # check move down
            print("losgelassen")

    def _check_mousebutton_events(self, event):
        """"""
        mouse_pos = pygame.mouse.get_pos()  # get position of mouse cursor
        self._check_on_button(mouse_pos)

    def _check_on_button(self, mouse_pos):
        """"""
        # check if play button
        if self.stats.game_active == False:
            # 'collidepoint()' checks collision of a rectangle with a point
            if self.play_button.rect.collidepoint(mouse_pos):
                self.stats.game_active = True
                self._play_music()  # set background music

    def _update_physics(self, ai_game):
        if self.stats.game_active and not hasattr(ai_game, 'new_block'):
            ai_game.new_block = Block(ai_game)
        else:
            ai_game.new_block.move(self.dt)



    def _update_screen(self):
        """update screen object surfaces"""
        # self.screen.blit(self.background_image, [-2, -2])  # background
        self.game_window.draw()
        self.next_window.draw()
        self.new_block.draw()
        if self.stats.game_active == False:
            self.play_button.draw_button()  # button

        # if self.stats.game_active == False:
        #     self.play_button.draw_button()  # button
        # else:
        #     pygame.mouse.set_visible(False)  # make mouse invisible
        # self.ship.blitme()  # draw ship
        # for bullet in self.bullets.sprites():  # draw bullets
        #     bullet.draw_bullet()
        # self.aliens.draw(self.screen)  # draw aliens
        # self.scoreboard.show_score()  # scoreboard
        # self.scoreboard.show_highscore()  # scoreboard
        # self._show_remaining()  # show remaining lifes
        pygame.display.flip()  # only make recently drawn screen visible

