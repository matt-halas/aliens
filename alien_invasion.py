import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star

from numpy.random import random

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_fleet()
        self._draw_stars()

    def run_game(self):
        # main loop that runs the game and detects input
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
            self._fire_bullet()
    
    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _update_screen(self):
        '''Updates the game screen'''
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
    
    def _create_fleet(self):
        '''Creates the alien fleet!'''
        alien = Alien(self)
        available_space_x = self.settings.screen_width - 2 * alien.rect.width
        available_space_y = self.settings.screen_height - 2 * self.ship.rect.height

        n_rows = int(available_space_y // (alien.rect.height \
            * self.settings.alien_spacing))
        n_aliens_per_row = int(available_space_x // (alien.rect.width \
            * self.settings.alien_spacing))
        
        for row in range(n_rows):    
            for n in range(n_aliens_per_row):
                self._create_alien(n, row)
    
    def _create_alien(self, alien_number, row):
        '''Creates an instance of alien'''
        alien = Alien(self)
        alien.rect.x = (1 + alien_number) * alien.rect.width \
            * self.settings.alien_spacing
        alien.rect.y = row * alien.rect.height * self.settings.alien_spacing
        self.aliens.add(alien)
    
    def _fire_bullet(self):
        '''creates new instance of bullet'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        self.bullets.update()
        '''removes bullets that have moved off da screen'''
        for bullet in self.bullets.copy():
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)
        
    def _draw_stars(self):
        n_stars_x = self.settings.screen_width // self.settings.star_spacing
        n_stars_y = self.settings.screen_height // self.settings.star_spacing
        for i in range(n_stars_y):
            for j in range(n_stars_x):
                star = Star(self)
                star.rect.y = self.settings.star_spacing * (i + random())
                star.rect.x = self.settings.star_spacing * (j + random())
                self.stars.add(star)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
 