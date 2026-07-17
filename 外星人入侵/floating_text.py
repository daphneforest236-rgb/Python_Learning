import pygame
from pygame.sprite import Sprite

class FloatingText(Sprite):
    """显示击杀后悬浮弹出的加成提示"""
    
    def __init__(self, ai_game, msg, center_pos):
        super().__init__()
        self.screen = ai_game.screen
        
        # 设置帅气的金黄色和稍微小一点的字体
        self.color = (255, 215, 0)
        self.font = pygame.font.Font(None, 28)
        
        # 将文字变成图片，并放在刚刚死去的外星人位置上
        self.image = self.font.render(msg, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = center_pos
        
        self.y = float(self.rect.y)
        
        # 特效存活时间（大约 30 帧，也就是半秒钟）
        self.timer = 30

    def update(self):
        """让文字缓慢向上漂浮，并且生命值减少"""
        self.y -= 1.5
        self.rect.y = self.y
        self.timer -= 1