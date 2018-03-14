import sys
import pygame

from settings import Settings
from person import Person
import game_functions as gf
from game_stats import GameStats

def run_game():
    # 初始化游戏、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch")
    stats = GameStats(ai_settings)
    # 创建一个小人和一个球组
    person = Person(ai_settings, screen)
    balls = pygame.sprite.Group()
    # 创建球
    gf.create_ball(ai_settings, screen, person, balls)
    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, person, balls)
        if stats.game_active:
            person.update()
            gf.update_balls(ai_settings, screen, person, balls, stats)
        gf.update_screen(ai_settings, screen, person, balls)
        
run_game()
