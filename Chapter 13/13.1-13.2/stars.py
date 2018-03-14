import pygame
import sys

from star import Star
import game_functions as gf

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Stars")
    
    stars = pygame.sprite.Group()
        
    gf.create_fleet(screen, stars)
    # 开始游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环时都重绘屏幕
        #screen.fill((230, 230, 230))
        #stars.draw(screen)
        for star in stars.sprites():
            star.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()
        
run_game()

