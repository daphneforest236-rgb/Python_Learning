import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.color = (255, 0, 0)  # 红色子弹
        # 制造一个宽3像素、高15像素的子弹矩形
        self.rect = pygame.Rect(0, 0, 3, 15)
        # 让子弹的初始位置，正好贴在飞船的顶部正中央
        self.rect.midtop = ai_game.ship.rect.midtop
    
    def update(self):
        """让子弹一直向上飞"""
        self.rect.y -= 2

    def draw_bullet(self):
        """在屏幕上画出子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)