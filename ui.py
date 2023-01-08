import pygame


class UI:
    def __init__(self, surface, status):
        # setup
        self.display_surface = surface

        # health
        self.health_bar = pygame.image.load('graphics/ui/health_bar.png').convert_alpha()
        self.health_bar_topleft = (54, 39)
        self.bar_max_width = 152
        self.bar_height = 4

        # coins
        self.coin = pygame.image.load('graphics/ui/coin.png').convert_alpha()
        self.coin_topleft = (60, 101)
        self.coin_rect = self.coin.get_rect(topleft=self.coin_topleft)

        # enemy_kills
        self.enemy_kills = pygame.image.load('graphics/enemy/run/0/enemy_run1.png').convert_alpha()
        self.enemy_kills_topleft = (42, 141)
        self.enemy_kills_rect = self.enemy_kills.get_rect(topleft=self.enemy_kills_topleft)

        # score
        self.score = 0
        self.score_topleft = (22, 61)
        self.score_surf = self.get_font(30).render("Score: ", False, '#33323d')
        self.score_rect = self.score_surf.get_rect(topleft=self.score_topleft)

        self.status = status

    def get_font(self, size):
        return pygame.font.Font("graphics/ui/ARCADEPI.TTF", size)

    def show_health(self, current, full):
        if self.status == 'game':
            self.display_surface.blit(self.health_bar, (20, 10))
            current_health_ratio = current / full
            current_bar_width = self.bar_max_width * current_health_ratio
            health_bar_rect = pygame.Rect(self.health_bar_topleft, (current_bar_width, self.bar_height))
            pygame.draw.rect(self.display_surface, '#dc4949', health_bar_rect)
            pygame.draw.rect(self.display_surface, '#dc4949', health_bar_rect)

    def change_status(self, status):
        self.status = status

    def show_coins(self, amount):
        if self.status == 'game':
            self.display_surface.blit(self.coin, self.coin_rect)
            coin_amount_surf = self.get_font(30).render(str(amount), False, '#33323d')
            coin_amount_rect = coin_amount_surf.get_rect(midleft=(self.coin_rect.right + 4, self.coin_rect.centery))
            self.display_surface.blit(coin_amount_surf, coin_amount_rect)
        else:
            self.coin_topleft = (600, 291)
            self.coin_rect = self.coin.get_rect(topleft=self.coin_topleft)
            self.display_surface.blit(self.coin, self.coin_rect)
            coin_amount_surf = self.get_font(36).render(str(amount), False, '#33323d')
            coin_amount_rect = coin_amount_surf.get_rect(midleft=(self.coin_rect.right + 4, self.coin_rect.centery))
            self.display_surface.blit(coin_amount_surf, coin_amount_rect)

    def show_enemy_kills(self, amount):
        if self.status == 'game':
            self.display_surface.blit(self.enemy_kills, self.enemy_kills_rect)
            enemy_kills_amount_surf = self.get_font(30).render(str(amount), False, '#33323d')
            enemy_kills_amount_rect = enemy_kills_amount_surf.get_rect(
                midleft=(self.enemy_kills_rect.right + 4, self.enemy_kills_rect.centery))
            self.display_surface.blit(enemy_kills_amount_surf, enemy_kills_amount_rect)
        else:
            self.enemy_kills_topleft = (600, 331)
            self.enemy_kills_rect = self.enemy_kills.get_rect(topleft=self.enemy_kills_topleft)

            self.display_surface.blit(self.enemy_kills, self.enemy_kills_rect)
            enemy_kills_amount_surf = self.get_font(36).render(str(amount), False, '#33323d')
            enemy_kills_amount_rect = enemy_kills_amount_surf.get_rect(
                midleft=(self.enemy_kills_rect.right + 4, self.enemy_kills_rect.centery))
            self.display_surface.blit(enemy_kills_amount_surf, enemy_kills_amount_rect)

    def show_score(self, amount):
        if self.status == 'game':
            self.display_surface.blit(self.score_surf, self.score_rect)
            score_amount_surf = self.get_font(30).render(str(amount), False, '#33323d')
            score_amount_rect = score_amount_surf.get_rect(midleft=(self.score_rect.right + 4, self.score_rect.centery))
            self.display_surface.blit(score_amount_surf, score_amount_rect)
        else:
            self.score_topleft = (550, 251)
            self.score_surf = self.get_font(36).render("Score:", False, '#33323d')
            self.score_rect = self.score_surf.get_rect(topleft=self.score_topleft)

            self.display_surface.blit(self.score_surf, self.score_rect)
            score_amount_surf = self.get_font(36).render(str(amount), False, '#33323d')
            score_amount_rect = score_amount_surf.get_rect(midleft=(self.score_rect.right + 4, self.score_rect.centery))
            self.display_surface.blit(score_amount_surf, score_amount_rect)
