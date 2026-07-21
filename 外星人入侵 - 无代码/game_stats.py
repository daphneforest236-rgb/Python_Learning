class GameStats:
    def __init__(self, ai_game):
        self.game_active = False
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = 3
        self.score = 0