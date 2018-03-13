
import pygame

class Character():
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('test.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.bottom = self.screen_rect.bottom
        self.rect.right = self.screen_rect.right
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
