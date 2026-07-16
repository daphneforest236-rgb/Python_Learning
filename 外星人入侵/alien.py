import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像，并缩小到合适尺寸（宽60，高60）
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        # 让每个外星人最初都出现在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 新增：将横坐标转换为小数，方便进行细微的加速计算
        self.x = float(self.rect.x)
    def check_edges(self):
        """如果外星人碰到了屏幕边缘，就返回 True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False

    '''def update(self, speed, direction):
        """向左或向右移动外星人"""
        self.rect.x += speed * direction'''

    def update(self, speed, direction):
        """向左或向右移动外星人"""
        self.x += speed * direction
        self.rect.x = self.x