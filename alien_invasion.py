import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self): 
        """Initialize the game and create game resources."""
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting.screen_height = self.screen.get_rect().height
        self.setting.screen_width = self.screen.get_rect().width  # Initialize screen before Ship
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)  # Now Ship can access the screen

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.setting.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
