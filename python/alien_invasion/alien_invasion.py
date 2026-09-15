# Configuration
import sys
import pygame

# 
from settings import Setting
from ship import Ship
# 
class AlienInvasion:
    """
    Overall class to manage the game assets and behavior.
    """
    def __init__(self):
        """ Initialize the game and create the game resources. """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Setting()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)


    def run_game(self):
        """
        Start main loop for the game.
        """
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """
        Respond to keypresses and mouse events.
        """
        for event in pygame.event.get():
            # Watch the keyborad and mouse events.
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
        
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
        

if __name__ == '__main__':
    # Make an instance of the game then run the game.
    ai = AlienInvasion()
    ai.run_game()