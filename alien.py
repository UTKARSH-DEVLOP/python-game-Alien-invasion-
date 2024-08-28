import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """"A class to represent  a sinngle alien in the fleet"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (30, 30))

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.settings = ai_game.setting

    

    def update(self):
        self.x += (self.settings.alien_speed_X * self.settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right>= screen_rect.right or self.rect.left <= 0:
            return True