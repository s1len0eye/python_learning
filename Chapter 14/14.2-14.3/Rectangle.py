import pygame
from pygame.sprite import Sprite

class Rectangle():
    """表示单个矩形的类"""
    def __init__(self, ai_settings, screen):
        """初始化矩形并设置其起始位置"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置矩形的尺寸和其他属性
        self.width, self.height = 50, 200
        self.rect_color = (0, 255, 0)
        # 创建矩形使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
        self.y = float(self.rect.y)
         
    def draw_rect(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.rect_color, self.rect)
        
    def check_edges(self):
        """如果矩形位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True
        else:
            return False
    
    def update(self):
        self.y += (self.ai_settings.rect_speed_factor * 
                self.ai_settings.rect_direction)
        self.rect.y = self.y
        
    def center_rect(self):
        self.center = self.screen_rect.centery
