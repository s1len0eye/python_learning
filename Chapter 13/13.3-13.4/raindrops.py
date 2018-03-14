import sys
import pygame

from settings import Settings
import game_functions as gf
from drop import Drop

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Raindrops")
    
    drops = pygame.sprite.Group()
    #gf.create_drops(ai_settings, screen, drops)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if ai_settings.new_drops_line:
            gf.create_drops(ai_settings, screen, drops)
            ai_settings.new_drops_line = False
        gf.update_drops(ai_settings, drops)
        gf.update_screen(ai_settings, screen, drops)
        
run_game()
