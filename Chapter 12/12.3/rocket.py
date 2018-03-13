import sys
import pygame

from rocket_class import Rocket
import game_functions as gf

def run_game():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rocket")
    
    rocket = Rocket(screen)
    
    while True:
        gf.check_event(rocket)
        rocket.update()
        gf.update_screen(screen, rocket)
        
run_game()
