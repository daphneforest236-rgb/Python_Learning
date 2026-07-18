class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        
        # 既然我们用星空图片了，就不需要纯灰色背景了，把它注释掉：
        # self.bg_color = (230, 230, 230)  
        
        # （可选）你可以把背景图的路径存在设置里，方便以后管理
        self.bg_image_path = 'images/bg_image.png'