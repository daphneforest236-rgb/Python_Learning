class GameStats:
    """跟踪游戏的统计信息"""
    
    def __init__(self, ai_game):
        # 游戏刚启动时，处于“未激活”状态（显示Play按钮）
        self.game_active = False
        # 新增：任何情况下都不应该重置最高得分
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = 3
        self.score = 0  # 新增：每次重新开始时，分数为 0