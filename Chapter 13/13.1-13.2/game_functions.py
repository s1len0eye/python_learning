import sys
import pygame
from random import randint

from star import Star

def get_number_stars_x(screen, star_width):
    available_space_x = screen.get_rect().width - 2 * star_width
    number_stars_x = int(available_space_x / (4 * star_width))
    return number_stars_x
    
def get_number_rows(screen, star_height):
    available_space_y = (screen.get_rect().height - (2 * star_height))
    number_rows = int(available_space_y / (4 * star_height))
    return number_rows

def create_star(screen, stars, star_number, row_number):
    star = Star(screen)
    star_width = star.rect.width
    star.x = star_width + 4 * star_width * star_number
    random_x = randint(-30,30)
    random_y = randint(-30,30)
    star.rect.x = star.x + random_x
    star.rect.y = star.rect.height + 4 * star.rect.height * row_number + random_y
    stars.add(star)
    
def create_fleet(screen, stars):
    star = Star(screen)
    number_stars_x = get_number_stars_x(screen, star.rect.width)
    number_rows = get_number_rows(screen, star.rect.height)

    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(screen, stars, star_number, row_number)
