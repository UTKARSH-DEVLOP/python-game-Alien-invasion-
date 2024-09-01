class GameStats:
    def __init__(self,ai_game):
        self.setting = ai_game.setting
        self.reset_stats()
        self.game_active = False
        self.highest_score = 0
    def reset_stats(self):
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1