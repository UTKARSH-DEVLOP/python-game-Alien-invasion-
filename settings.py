class Settings:
    """"A class to store all the settings of class ."""
    def __init__(self):
        self.screen_width = 1350
        self.screen_height = 650
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed = 2
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.max_bullets_allowed = 100

        #alien settings
        self.alien_speed_X= 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1