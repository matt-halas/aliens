import pygame
from settings import Settings

class Lives:
    '''Class describing the life display system'''
    def __init__(self, ai_game):
        self.screen = ai_game.screen

        IMAGE_SIZE = (36, 64)
        self.image = pygame.image.load('aliens-game/images/ship.bmp')
        self.image = pygame.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        
        self.settings = Settings()

        self.n_lives = self.settings.lives

    def blitme(self):
        for life in range(self.n_lives):
            self.rect.left = 10 + life * self.rect.width
            self.rect.top = 10
            self.screen.blit(self.image, self.rect)
    
