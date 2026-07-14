import sys
import pygame
from settings import Settings

class AlienInvasion:
    """管理游戏资源和行为的总体类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings() # 实例化设置类

        # 创建显示窗口
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("外星人入侵")

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 1. 侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 2. 每次循环时都重绘屏幕背景
            self.screen.fill(self.settings.bg_color)

            # 3. 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

'''pygame.init()：这是 Pygame 的启动引擎，必须在做任何操作前调用，它会让 Pygame 准备好底层的显卡、声卡等硬件接口。

无限循环 while True:：这是游戏的“心跳”。所有的电子游戏底层都是一个死循环，它在一秒钟内运行几十次（帧率），不断做三件事：接收玩家输入 -> 更新游戏状态 -> 重新渲染画面。

pygame.event.get()：这是接收玩家输入的地方。当玩家点击窗口右上角的 X 时，会触发 pygame.QUIT 事件，我们调用 sys.exit() 安全结束程序。

pygame.display.flip()：这是游戏开发中常用的“双缓冲”技术。我们在内存中画好一帧（填上浅灰色），然后调用 flip() 将其推送到显示器上。这能防止玩家看到画面一点点画出来的闪烁感。'''