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
        self.movement_speed = 1.1
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.rect.right >= self.screen_rect.right and self.moving_right:
            self.moving_right = False
        elif self.rect.left <= self.screen_rect.left and self.moving_left:
            self.moving_left = False
        if self.moving_right == True:
            self.x += self.movement_speed
        if self.moving_left == True:
            self.x -= self.movement_speed
        self.rect.x = self.x
    
    def blitme(self):
        '''Draw the ship'''
        self.screen.blit(self.image, self.rect)