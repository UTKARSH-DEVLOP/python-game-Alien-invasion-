import sys 
import pygame

from settings import Settings
from ship import Ship
  
class AlienInvasion:
    """ Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game,  and create game resources"""    
        self.setting=Settings()
        pygame.init()
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230,2,230)
        
        self.ship=Ship(self)

    def run_game(self):
        """start the main loop for the game"""

        while True:
            #watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()
            pygame.display.flip()
if __name__ == '__main__':
    ai=AlienInvasion()
    ai.run_game()