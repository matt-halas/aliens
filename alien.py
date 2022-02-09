import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    '''Class that will handle all alien instances'''
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = Settings()

        # load the alien and get its rect
        self.image = pygame.image.load("aliens-game/images/alien.bmp")
        IMAGE_SIZE = (64, 32)
        self.image = pygame.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()

        # initialize a test alien in the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.speed = self.settings.alien_speed

    def update(self):
        self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        '''draw the alien'''
        self.screen.blit(self.image, self.rect)

# TODO: improve filepathing