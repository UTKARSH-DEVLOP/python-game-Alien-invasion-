import pygame

class Ship:
    def __init__(self,ai_game):
        """"Initialize the ship and set it's starting position"""
        
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
    
        #load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50,40))
        self.rect = self.image.get_rect()
        
        #start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """"draw the ship at its current position"""
        self.screen.blit(self.image,self.rect)