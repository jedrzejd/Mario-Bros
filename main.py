import sys

import pygame

from end_screen import End_Screen
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
        self.enemy_kills = 0
        self.score = 0

        # audio
        self.level_bg_music = pygame.mixer.Sound('audio/music_main_theme.ogg')
        self.overworld_bg_music = pygame.mixer.Sound('audio/overworld_music.MP3')
        self.menu_music = pygame.mixer.Sound('audio/menu_music.mp3')
        self.end_game_music = pygame.mixer.Sound('audio/win.mp3')

        # overworld creation
        self.menu = Menu(screen, self.create_overworld, 0)
        self.menu_music.play(loops=-1)
        self.status = 'menu'

        # user interface
        self.ui = UI(screen, 'game')

    def create_level(self, current_level):
        self.level = Level(screen, current_level, self.create_overworld, self.change_coins, self.change_health,
                           self.change_enemy_kills, self.create_end_screen, self.change_score)
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

    def create_end_screen(self):
        self.status = 'end_game'
        self.level_bg_music.stop()
        self.end_game_music.play()
        self.end_screen = End_Screen(screen)

    def change_coins(self, amount):
        self.coins += amount

    def change_health(self, amount):
        self.curr_health += amount

    def change_enemy_kills(self, amount):
        self.enemy_kills += amount

    def change_score(self, amount):
        self.score += amount

    def check_game_over(self):
        if self.curr_health <= 0:
            self.curr_health = 100
            self.coins = 0
            self.max_level = 0
            self.enemy_kills = 0
            self.score = 0
            self.overworld = Overworld(0, self.max_level, screen, self.create_level, self.create_menu)
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)

    def run(self):
        if self.status == 'menu':
            self.menu.run()
        elif self.status == 'overworld':
            self.overworld.run()
        elif self.status == 'end_game':
            self.end_screen.run()
            self.ui.change_status('end_game')
            self.ui.show_score(self.score)
            self.ui.show_health(self.curr_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.ui.show_enemy_kills(self.enemy_kills)

        else:
            self.level.run()
            self.ui.show_health(self.curr_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.ui.show_enemy_kills(self.enemy_kills)
            self.ui.show_score(self.score)
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
