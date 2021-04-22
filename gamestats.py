class GameStats:

    def __init__(self, ai_game):
        """"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """reset stats when new game starts"""
        self.game_active = False
        self.score = 0
        # get highscore
        #self.highscore = self._get_highscore()