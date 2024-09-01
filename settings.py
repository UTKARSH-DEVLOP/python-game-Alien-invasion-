class Settings:
    """"A class to store all the settings of class ."""
    def __init__(self):
        self.screen_width = 1350
        self.screen_height = 650
        self.bg_color = (110, 162, 250)

        #ship settings
       
        self.ship_limit = 3

        #bullet settings
        
        self.bullet_width = 7
        self.bullet_height = 15
        self.bullet_color = (255, 189, 25)
        self.max_bullets_allowed = 50

        #alien settings
        
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
        


        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
         self.ship_speed = 2
         self.bullet_speed = 2
         self.alien_speed_X= 1
         self.alien_points =50
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale 
        self.bullet_speed *= self.speedup_scale 
        self.alien_speed_X *= self.speedup_scale 
        self.alien_points =self.alien_points* self.score_scale
    