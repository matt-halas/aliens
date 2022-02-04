import pygame

class Ship:
    '''A class to manage the ship.'''
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the image and get its rect
        self.image = pygame.image.load('aliens-game\images\ship.bmp')
        IMAGE_SIZE = (73, 128)
        self.image = pygame.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.speed = 0
    
    def update(self):
        self.rect.x += self.speed
    
    def blitme(self):
        '''Draw the ship'''
        self.screen.blit(self.image, self.rect)