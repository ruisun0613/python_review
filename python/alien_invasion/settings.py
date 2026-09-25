class Setting:
    """
    A class to store all settings for Alien Invasion.
    """
    def __init__(self):
        """
        Initialize the game's stasic settings.
        """
        self.screen_width = 1200
        self.screen_height = 800 
        self.bg_color = (230, 230, 230)
        # 12-1. Blue Sky: Make a Pygame window with a blue background
        # self.bg_color = (0, 0, 255)

        # Ship settings
        self.ship_speed = 5.0
        self.ship_limit = 3

        # Bullets settings
        self.bullet_speed = 5.0
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # Alien settings
        self.alien_speed = 5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right, and -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speed up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase.
        self.point_scale = 1.5

        self.difficulty = 'Normal'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game.

        Define three difficulty: Easy, Normal, Hard
        """
        if self.difficulty == 'Easy':
            self.ship_speed = 4.0
            self.bullet_speed = 3.0
            self.alien_speed = 1.5
        elif self.difficulty == 'Normal':
            self.ship_speed = 3.0
            self.bullet_speed = 2.5
            self.alien_speed = 2.5
        elif self.difficulty == 'Hard':
            self.ship_speed = 2.0
            self.bullet_speed = 2.0
            self.alien_speed = 3.5

        # fleet_direction = 1 represents right, and -1 represents left  
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.point_scale)