class GameStats:
    #track stats

    def __init__(self, ai_game):
        #initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        #start alien invasion in an active state
        self.high_score = 0
        self.game_active = False
    def reset_stats(self):
        #initialzie static statistics
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
