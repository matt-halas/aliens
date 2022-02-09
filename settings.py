class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 60)

        self.bullet_speed = 1
        self.bullet_height = 30
        self.bullet_width = 300
        self.bullet_color = (0, 200, 0)
        self.bullets_allowed = 3

        self.alien_spacing = 1.5
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10

        self.star_spacing = 100

        self.lives = 3