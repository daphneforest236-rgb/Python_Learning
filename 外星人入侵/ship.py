import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__() # 激活分身
        self.screen = ai_game.screen
        # 获取屏幕的外框，方便我们参考位置
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()

        # 将每艘新飞船放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        # ==================== 修改点 1 ====================
        # 在飞船的属性 x 中存储小数值（解决报错的关键）
        self.x = float(self.rect.x)
        # ==================================================

        # 持续移动的开关
        self.moving_right = False
        self.moving_left = False

        # 飞船的基础初始速度
        self.speed = 3.0

    def update(self):
        """根据开关状态持续移动飞船"""
        # 更新飞船的小数位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
            
        # ==================== 修改点 2 ====================
        # 根据 self.x 更新 rect 对象（解决飞船原地不动的问题）
        self.rect.x = self.x
        # ==================================================
            
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)