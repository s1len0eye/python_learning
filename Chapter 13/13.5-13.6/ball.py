import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('ball.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = 0

        self.y = float(self.rect.y)
         
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        else:
            return False
    
    def update(self):
        self.y += self.ai_settings.ball_speed_factor
        self.rect.y = self.y
