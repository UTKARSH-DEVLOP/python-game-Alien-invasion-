import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.setting
        self.stats = ai_game.stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.prep_score()
        self.prep_highScore()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        rounded_score = round(self.stats.score,-1)
        score_str = "{:,}".format(rounded_score)
        score_str =str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_ships(self):
        self.ships=Group()
        for ship_number in range (self.stats.ships_left):
            ship=Ship(self.ai_game)
            ship.rect.x = 10+ ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_highScore(self):
        rounded_highscore = round(self.stats.highest_score,-1)
        highscore_str = "{:,}".format(rounded_highscore)
        self.highscore_image = self.font.render(highscore_str,True,self.text_color,self.settings.bg_color)
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.center = self.screen_rect.center
        self.highscore_rect.top = self.score_rect.top

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)  # Corrected here
        self.ships.draw(self.screen)


    def check_high_score(self):
        if self.stats.score > self.stats.highest_score:
            self.stats.highest_score = self.stats.score
            self.prep_highScore()
