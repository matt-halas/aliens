import pygame.font

class Scoreboard:
    '''A class for tracking and displaying score and level'''
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.score = ai_game.score
        self.level = ai_game.level
        
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_level()

    def prep_score(self):
        self.score = int(self.score)
        score_str = str(self.score)
        self.score_img = self.font.render(score_str, True, self.text_color,
            self.settings.bg_color)
        
        self.score_rect = self.score_img.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - 20
    
    def prep_level(self):
        level_str = 'Lvl: ' + str(self.level)
        self.level_img = self.font.render(level_str, True, self.text_color,
            self.settings.bg_color)
        
        self.level_rect = self.level_img.get_rect()
        self.level_rect.top = self.score_rect.bottom + 20
        self.level_rect.right = self.screen_rect.right - 20
    
    def show_scoreboard(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.level_img, self.level_rect)