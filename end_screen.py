import sys

import pygame


class End_Screen:
    def __init__(self, surface):
        self.display_surface = surface
        self.background = pygame.image.load("assets/background.png")

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)

    def display(self):
        self.display_surface.blit(pygame.transform.scale(self.background, (1200, 704)), (0, 0))

        options_text = self.get_font(30).render("Gratulacje wygrałeś gre", True, "Black")
        options_rect = options_text.get_rect(center=(620, 200))
        self.display_surface.blit(options_text, options_rect)

        back = pygame.image.load("assets/Play Rect.png")
        self.display_surface.blit(pygame.transform.scale(back, (290, 150)), (530, 240))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def run(self):
        self.display()
