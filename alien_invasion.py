import sys

import pygame

from settings import Settings
from ship import Ship

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
                # change the ship speed if a key is held
                if event.key == pygame.K_RIGHT:
                    self.ship.speed = 1
                if event.key == pygame.K_LEFT:
                    self.ship.speed = -1
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT):
                    self.ship.speed = 0
            
    
    def _update_screen(self):
        '''Updates the game screen'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
 