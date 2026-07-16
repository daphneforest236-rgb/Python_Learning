import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard:
    """显示得分信息的类"""
    
    def __init__(self, ai_game):
        """初始化显示得分涉及的属性"""
        self.ai_game = ai_game  # 存下游戏主体
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        
        # 显示得分信息时使用的字体设置（深灰色，大小48）
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font(None, 48)
        
        # 准备初始得分图像
        self.prep_score()
        # 一启动就准备好飞船图标
        self.prep_ships()       
        #一启动就准备好最高分
        self.prep_high_score()

    def prep_score(self):
        """将得分转换为渲染的图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color)
        
        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """在屏幕上绘制得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)  # 新增：画出最高分
    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)
        
        # 将最高得分放在屏幕顶部正中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """检查是否诞生了新的最高得分"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    def prep_ships(self):
        """显示还剩下多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            # 让小飞船排在屏幕左上角，每艘之间留点空隙
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    def show_score(self):
        """在屏幕上绘制得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)  # 新增：画出代表生命值的小飞船