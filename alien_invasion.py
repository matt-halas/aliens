import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    # class to manage game assets and behavior
    def __init__(self):
        # initializes background settings needed for pygame to work
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = []

    def run_game(self):
        # main loop that runs the game and detects input
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
    
    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Detects keypresses
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
    
    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            bullet = Bullet(self)
            bullet.__init__(self)
            self.bullets.append(bullet)
    
    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _update_screen(self):
        '''Updates the game screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self._update_bullets()
        pygame.display.flip()
    
    def _update_bullets(self):
        '''updates all instances of bullets'''
        for bullet in self.bullets:
            bullet.update()
            bullet.draw_bullet()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
 