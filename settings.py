class Settings:
    """"A class to store all the settings of class ."""
    def __init__(self):
        self.screen_width = 1375
        self.screen_height = 690
        self.bg_color = (230,230,230)
        self.ship_speed=1.5

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.max_bullets_allowed = 100