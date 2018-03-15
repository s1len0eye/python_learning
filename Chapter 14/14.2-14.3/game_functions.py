import sys
from time import sleep
import pygame
from random import randint

from bullet import Bullet
from Rectangle import Rectangle

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    
def check_keyup_events(event, ai_settings, screen, stats, ship, 
            rect, bullets):
    """响应松开"""
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, rect, bullets)

def start_game(ai_settings, screen, stats, ship, rect, bullets):
    ai_settings.initialize_dynamic_settings()
    # 隐藏光标
    pygame.mouse.set_visible(False)
    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True
    #清空子弹列表
    bullets.empty()
    # 矩形居中，并让飞船居中
    rect.center_rect()
    ship.center_ship()

def check_play_button(ai_settings, screen, stats, play_button, 
        ship, rect, bullets, mouse_x, mouse_y):
    """在玩家单击play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, rect, bullets)

def check_events(ai_settings, screen, stats, play_button, ship, 
            rect, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, stats, ship, 
                    rect, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, 
                ship, rect, bullets, mouse_x, mouse_y)
            
def update_screen(ai_settings, screen, stats, ship, rect, bullets, 
            play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rect.draw_rect()
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    
def check_bullet_rect_collisions(ai_settings, screen, ship, rect, bullets):
    """响应子弹和矩形的碰撞"""
    collision = pygame.sprite.spritecollideany(rect, bullets)
    # 改变矩形的颜色，删除子弹
    if collision:
        ai_settings.increase_speed()
        bullets.remove(collision)
        rect.rect_color = (randint(0, 255), randint(0, 255), randint(0, 255))

def update_bullets(ai_settings, screen, stats, ship, rect, bullets):
    """更新子弹的位置，并删除已消失子弹"""
    # 更新子弹位置
    bullets.update()
    # 删除已消失子弹
    for bullet in bullets.copy():
        if bullet.rect.right >= screen.get_rect().right:
            if stats.ships_left > 0:
                stats.ships_left -= 1
                bullets.remove(bullet)
            else:
                stats.game_active = False
                pygame.mouse.set_visible(True)
    check_bullet_rect_collisions(ai_settings, screen, ship, rect, bullets)
            
def change_rect_direction(ai_settings, rect):
    ai_settings.rect_direction *= -1

def check_rect_edges(ai_settings, rect):
    if rect.check_edges():
        change_rect_direction(ai_settings, rect)

def update_rect(ai_settings, stats, screen, ship, rect, bullets):
    check_rect_edges(ai_settings, rect)
    rect.update()

