class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # High score should never be reseted.
        self.high_score = self.get_high_score()
        
    def get_high_score(self):
        """Read the high score from the high_score.txt."""
        with open('high_score.txt') as f_obj:
            contents = f_obj.read()
        return int(contents)
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
