import pygame

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.setting = ai_game.setting  # Access settings without parentheses
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
    
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50, 40))  # Resize image
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current position."""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x
    
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x=float(self.rect.x)
