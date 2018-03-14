import sys
import pygame
from random import randint
from time import sleep

from ball import Ball

def check_keydown_events(event, ai_settings, screen, person, balls):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        person.moving_right = True
    elif event.key == pygame.K_LEFT:
        person.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
        
        
def check_keyup_events(event, person):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        person.moving_right = False
    elif event.key == pygame.K_LEFT:
        person.moving_left = False

def check_events(ai_settings, screen, person, balls):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, person, balls)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, person)

def update_screen(ai_settings, screen, person, balls):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    person.blitme()
    balls.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_balls(ai_settings, screen, person, balls, stats):
    check_ball_person_collisions(ai_settings, screen, person, balls)
    for ball in balls.sprites():
        if ball.check_edges():
            if stats.person_left > 0:
                stats.person_left -= 1
                balls.empty()
                create_ball(ai_settings, screen, person, balls)
                sleep(0.5)
                person.center_person()
            else:
                stats.game_active = False
                break
    balls.update()

def check_ball_person_collisions(ai_settings, screen, person, balls):
    collisions = pygame.sprite.groupcollide([person], balls, False, True)
    # 生成新的球
    if len(balls) == 0:
        create_ball(ai_settings, screen, person, balls)

def create_ball(ai_settings, screen, person, balls):
    ball = Ball(ai_settings, screen)
    ball.x = randint(0, ai_settings.screen_width)
    ball.rect.x = ball.x
    balls.add(ball)
