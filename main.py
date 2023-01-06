import pygame
import sys

from level import Level
from menu import Menu
from overworld import Overworld
from settings import *
from ui import UI


class Game:
    def __init__(self):
        # game attributes
        self.max_level = 0
        self.max_health = 100
        self.curr_health = 100
        self.coins = 0

        # audio
        self.level_bg_music = pygame.mixer.Sound('audio/level_music.wav')
        self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.wav')
        self.menu_music = pygame.mixer.Sound('resources_music_main_theme.ogg')

        # overworld creation
        # self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.menu = Menu(screen, self.create_overworld, 0)
        self.menu_music.play(loops=-1)
        self.status = 'menu'

        # user interface
        self.ui = UI(screen)

    def create_level(self, current_level):
        self.level = Level(screen, current_level, self.create_overworld, self.change_coins, self.change_health)
        self.status = 'level'
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops=-1)

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level, self.create_menu)
        self.status = 'overworld'
        self.level_bg_music.stop()
        self.menu_music.stop()
        self.overworld_bg_music.play(loops=-1)

    def create_menu(self, screen, current_level):
        self.status = 'menu'
        self.menu = Menu(screen, self.create_overworld, current_level)
        self.overworld_bg_music.stop()
        self.menu_music.play(loops=-1)

    def change_coins(self, amount):
        self.coins += amount

    def change_health(self, amount):
        self.curr_health += amount

    def check_game_over(self):
        if self.curr_health <= 0:
            self.curr_health = 100
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(0, self.max_level, screen, self.create_level, self.create_menu)
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)

    def run(self):
        if self.status == 'menu':
            self.menu.run()
        elif self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.curr_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    game.run()

    pygame.display.update()
    clock.tick(60)
