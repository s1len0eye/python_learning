import sys
import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf
from Rectangle import Rectangle

def run_game():
    # 初始化游戏、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Shooting")
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船、一个子弹编组和一个矩形
    ship = Ship(ai_settings, screen)
    bullets = pygame.sprite.Group()
    rect = Rectangle(ai_settings, screen)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, 
                    rect, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, ship, rect, bullets)
            gf.update_rect(ai_settings, stats, screen, ship, rect, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, rect, bullets,
                        play_button)
        
run_game()
