import sys

import pygame

from button import Button


class Menu:
    def __init__(self, surface, create_overworld, current_level):
        self.display_surface = surface
        self.background = pygame.image.load("assets/background.png")

        self.create_overworld = create_overworld
        self.current_level = current_level

        self.depth = 0
        self.setup_buttons()

    def setup_buttons(self):
        self.play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                                  text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4",
                                  hovering_color="White")
        self.options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                     text_input="CREDITS", font=self.get_font(75), base_color="#d7fcd4",
                                     hovering_color="White")
        self.quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                                  text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4",
                                  hovering_color="White")

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def play(self):
        self.create_overworld(self.current_level, 0)

    def check_menu_option(self):
        menu_mouse_pos = pygame.mouse.get_pos()
        self.display_surface.blit(pygame.transform.scale(self.background, (1200, 704)), (0, 0))

        if self.depth == 0:
            for button in [self.play_button, self.options_button, self.quit_button]:
                button.changeColor(menu_mouse_pos)
                button.update(self.display_surface)

            menu_text = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            menu_rect = menu_text.get_rect(center=(640, 100))

            self.display_surface.blit(menu_text, menu_rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                self.play()
            if keys[pygame.K_2]:
                self.depth = 1
            if keys[pygame.K_3]:
                pygame.quit()
                sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.checkForInput(menu_mouse_pos):
                        self.play()
                        break
                    if self.options_button.checkForInput(menu_mouse_pos):
                        self.depth = 1
                        break
                    if self.quit_button.checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()

        elif self.depth == 1:
            options_text = self.get_font(30).render("Gra Została stworzona na zajęcia KCK", True, "Black")
            options_text1 = self.get_font(30).render("przez Jędrzeja 'Yendrula' Dudzicza", True, "Black")
            options_rect = options_text.get_rect(center=(600, 200))
            options_rect1 = options_text.get_rect(center=(600, 300))
            self.display_surface.blit(options_text, options_rect)
            self.display_surface.blit(options_text1, options_rect1)

            options_back = Button(image=None, pos=(640, 460),
                                  text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

            options_back.changeColor(menu_mouse_pos)
            options_back.update(self.display_surface)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.depth = 0
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if options_back.checkForInput(menu_mouse_pos):
                        self.depth = 0
                        break

    def run(self):
        self.check_menu_option()
