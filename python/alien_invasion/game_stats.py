from pathlib import Path
import json

class GameStats:
    def __init__(self, ai_game):
        """
        Initialize statistics
        """
        self.settings = ai_game.settings

        # Save the high score to json file.
        path = Path('python/alien_invasion/data/high_score.json')
        if path.exists():
            high_score = path.read_text()
            high_score_information = json.loads(high_score)
            self.high_score = high_score_information
        else:
            self.high_score = 0
            
        self.reset_stats()

    def reset_stats(self):
        """
        Initialize statistics that can change during the game.
        """
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1