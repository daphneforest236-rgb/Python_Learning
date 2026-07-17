import pygame
from pygame.sprite import Sprite

class AlienBomb(Sprite):
    """表示外星人炸弹的类"""
    
    def __init__(self, ai_game, alien):
        super().__init__()
        self.screen = ai_game.screen
        
        # 炸弹的外观：宽 5，高 15 的红色矩形
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, 5, 15)
        
        # 炸弹的初始位置：从投掷它的那个外星人底部正中央掉出来
        self.rect.midbottom = alien.rect.midbottom
        self.y = float(self.rect.y)
        
        # 炸弹的下落速度
        self.speed = 0.5

    def update(self):
        """向下移动炸弹"""
        self.y += self.speed
        self.rect.y = self.y

    def draw_bomb(self):
        """在屏幕上绘制炸弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)