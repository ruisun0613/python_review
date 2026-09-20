class Setting:
    """
    A class to store all settings for Alien Invasion.
    """
    def __init__(self):
        """
        Initialize the game's settings.
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