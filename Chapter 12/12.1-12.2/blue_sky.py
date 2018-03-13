import pygame
import sys

from game_character import Character

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blue Background")

color = (255, 209, 15)
character = Character(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    screen.fill(color)
    character.blitme()
    pygame.display.flip()
