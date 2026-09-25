# Configuration
import sys
import pygame
import json
from time import sleep
from pathlib import Path
from pygame import mixer

from settings import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

path = Path('python/alien_invasion/data/high_score.json')

class AlienInvasion:
    """
    Overall class to manage the game assets and behavior.
    """
    def __init__(self):
        """ Initialize the game and create the game resources. """
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Setting()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Full screen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)        # Create an instance to store game statistics.

        self.sb = Scoreboard(self)

        self.ship = Ship(self)

        self._create_fleet()

        self.shoot_voice = mixer.Sound('python/alien_invasion/sound/shoot.wav')
        self.explosion_voice = mixer.Sound('python/alien_invasion/sound/explosion.wav')

        # Start Alien Invasion in an inactive state.
        self.game_active = False
        self.choosing_difficulty = False
        self.play_button = Button(self, msg = 'Play')
        self._choose_difficulty_button()
        
    def run_game(self):
        """
        Start main loop for the game.
        """
        while True:
            self._check_events()

            if self.game_active == True:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """
        Respond to keypresses and mouse events.
        """
        for event in pygame.event.get():
            # Watch the keyborad and mouse events.
            if event.type == pygame.QUIT:
                self.stats.high_score_information = json.dumps(self.stats.high_score)
                path.write_text(self.stats.high_score_information)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_events_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.choosing_difficulty:
                    self._check_choose_difficulty_button(mouse_pos)
                else:
                    self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
           self.choosing_difficulty = True

    def _check_choose_difficulty_button(self, mouse_pos):
        difficulty_selected = False

        if self.easy_button.rect.collidepoint(mouse_pos):
            self.settings.difficulty = 'Easy'
            difficulty_selected = True
        elif self.normal_button.rect.collidepoint(mouse_pos):
            self.settings.difficulty = 'Normal'
            difficulty_selected = True
        elif self.hard_button.rect.collidepoint(mouse_pos):
            self.settings.difficulty = 'Hard'
            difficulty_selected = True

        if difficulty_selected:
            self._start_game()

    def _choose_difficulty_button(self):
        self.easy_button = Button(self, "Easy")
        self.normal_button = Button(self, "Normal")
        self.hard_button = Button(self, "Hard")

        self.easy_button.rect.centery = self.screen.get_rect().centery - 100
        self.normal_button.rect.centery = self.screen.get_rect().centery
        self.hard_button.rect.centery = self.screen.get_rect().centery + 100


        self.easy_button.msg_image_rect.centery = self.easy_button.rect.centery
        self.normal_button.msg_image_rect.centery = self.normal_button.rect.centery
        self.hard_button.msg_image_rect.centery = self.hard_button.rect.centery

    def _start_game(self):
        # Reset the game statistics
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Reset the game dynamic
        self.settings.initialize_dynamic_settings()

        self.game_active = True
        
        # Get rid of any remainig bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()
        
        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()
        
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        self.choosing_difficulty = False

    def _check_events_keydown(self, event):
        """
        Respond to keypresses.

        12-4. 
        Update the ship up and down
        """
        if event.key == pygame.K_RIGHT:
             # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
        # elif event.key == pygame.K_UP:
        #     # Move the ship to the up
        #     self.ship.moving_up = True
        # elif event.key == pygame.K_DOWN:
        #     # Move the ship to the down
        #     self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            # Make sure press spacebar that the ship will fire the bullet
            self._fire_bullets()
        elif event.key == pygame.K_q:
            self.stats.high_score_information = json.dumps(self.stats.high_score)
            path.write_text(self.stats.high_score_information)
            sys.exit()
        elif event.key == pygame.K_p and self.game_active == False:
            self.choosing_difficulty = True
        
        elif self.choosing_difficulty:
            difficulty_selected = False
            if event.key == pygame.K_1:
                self.settings.difficulty = 'Easy'
                difficulty_selected = True
            elif event.key == pygame.K_2:
                self.settings.difficulty = 'Normal'
                difficulty_selected = True
            elif event.key == pygame.K_3:
                self.settings.difficulty = 'Hard'
                difficulty_selected = True
            if difficulty_selected:
                self._start_game()

    def _check_events_keyup(self, event):
        """
        Respond to key release.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # elif event.key == pygame.K_UP:
        #     self.ship.moving_up = False
        # elif event.key == pygame.K_DOWN:
        #     self.ship.moving_down = False

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height= alien.rect.size
        current_x, current_y= alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edge(self):
        """
        Respond appropriately if any aliens have reached an edge.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        Drop the entire fleet and change the fleet's direction.
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            
    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.shoot_voice.play()

    def _ship_hit(self):
        """
        Respond to the ship being hit by an alien.
        """
        if self.stats.ship_left > 0:
            # Decrement ships_left, and update scoreboard
            self.stats.ship_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_bullet(self):
        self.bullets.update()
        # Get rid of bullets that have disappered
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )
        if not self.aliens:
            """
            Destroy existing bullets and create new fleet.
            """
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

        if collision:
            self.explosion_voice.play()
            for aliens in collision.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _check_aliens_bottom(self):
        """
        Check if any aliens have reached the bottom of screen.
        """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _update_aliens(self):
        """
        Update the position of all aliens in the fleet.

        Check if the fleet is at an edge, then update positions. 
        """
        self._check_fleet_edge()

        self.aliens.update()

        # Look for the alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()

        self.aliens.draw(self.screen)

        self.sb.draw_score()

        # Draw the button if the game is inactive.
        if not self.game_active:
            if self.choosing_difficulty:
                self.easy_button.draw_button()
                self.normal_button.draw_button()
                self.hard_button.draw_button()
            else:
                self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
        

if __name__ == '__main__':
    # Make an instance of the game then run the game.
    ai = AlienInvasion()
    ai.run_game()