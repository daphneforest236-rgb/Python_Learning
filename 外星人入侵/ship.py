import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        # 获取屏幕的外框，方便我们参考位置
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()

        # 将每艘新飞船放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 持续移动的开关
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据开关状态持续移动飞船
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        不仅要求开关是打开的，还要确保飞船没有越过边界。"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
            
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)