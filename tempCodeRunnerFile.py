import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien 
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self): 
        """Initialize the game and create game resources."""
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        self.setting.screen_height = self.screen.get_rect().height
        self.setting.screen_width = self.screen.get_rect().width  # Initialize screen before Ship
        
        pygame.display.set_caption("Alien Invasion")
       
        self.stats = GameStats(self)
        self.sb =Scoreboard(self)
        self.ship = Ship(self)                                    # Now Ship can access the screen
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self,"play")

               
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()  # Update bullet positions
                self._update_aliens()
                
            self._update_screen()  # Redraw screen with updated positions
            
          

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key ==pygame.K_SPACE:
                    self.fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT: 
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen and flip to the new screen ."""
        self.screen.fill(self.setting.bg_color)

        if self.stats.game_active:
            self.ship.blitme()
            for bullet in self.bullets.sprites():  
                bullet.draw_bullet()
            self.aliens.draw(self.screen) 
            self.sb.show_score()
        else:
            # Draw the play button if the game is inactive
            self.play_button.draw_button()


        pygame.display.flip()

    def _check_play_button(self,mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.setting.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            pygame.mouse.set_visible(False)

            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.sb.prep_ships()

    def _create_fleet(self):
        """"create the fleet of aliens"""
        #make an alien
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.setting.screen_width - (2*alien_width)
        number_of_aliens_x = available_space_x // (2*alien_width - 3)
        available_space_y = self.setting.screen_height - (3*alien_height)-self.ship.rect.height
        number_of_aliens_y = available_space_y // ((2 * alien_height))
        
        for row_number in range(number_of_aliens_y):
            for alien_number in range(number_of_aliens_x):
                self._create_alien(alien_number,row_number)
        
    def _create_alien(self,alien_number ,row_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + (2*alien_width) * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (1.5*alien_height)* row_number
        self.aliens.add(alien)
        


    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        collisions  = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            self.stats.score += self.setting.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.setting.increase_speed()

            #increase level
        self.stats.level+=1
        self.sb.prep_level()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        self._check_alien_bottom()
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """changes fleet dirction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    def _ship_hit(self):
        """respond to ship hit by aliens"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            #get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()

            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_alien_bottom(self):
        """checks if  any aliens has reached bottom of screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def fire_bullet(self):
        """"create a new bullet and add it  to bullet group"""
        if self.setting.max_bullets_allowed >= len(self.bullets):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

   


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
 