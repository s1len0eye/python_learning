import sys
import pygame
from random import randint

from drop import Drop

def update_screen(ai_settings, screen, drops):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    for drop in drops.sprites():
        drop.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    
def check_fleet_edges(ai_settings, drops):
    for drop in drops.copy():
        if drop.check_edges():
            drops.remove(drop)
    
def check_drops_newline(ai_settings, drops):
    change_status = True
    for drop in drops.sprites():
        if drop.rect.top < drop.rect.height*1.5:
            change_status = False
    if change_status:
        ai_settings.new_drops_line = True
    
def update_drops(ai_settings, drops):
    check_fleet_edges(ai_settings, drops)
    check_drops_newline(ai_settings, drops)
    drops.update()
    
def get_number_drops_x(ai_settings, drop_width):
    available_space_x = ai_settings.screen_width
    number_drops_x = int(available_space_x / (2 * drop_width))

    return number_drops_x
    
def create_drop(ai_settings, screen, drops, drop_number):
    drop = Drop(ai_settings, screen)
    drop_width = drop.rect.width
    randomx = randint(-drop_width, drop_width)
    drop.x = drop_width + 2 * drop_width * drop_number + randomx
    drop.rect.top = -2 * drop.rect.height
    drop.rect.x = drop.x
    drops.add(drop)
    
def create_drops(ai_settings, screen, drops):
    drop = Drop(ai_settings, screen)
    number_drops_x = get_number_drops_x(ai_settings, drop.rect.width)
    #print(str(number_drops_x))
    for drop_number in range(number_drops_x):
        create_drop(ai_settings, screen, drops, drop_number)
