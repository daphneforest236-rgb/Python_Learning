import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import time
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import random
from alien_bomb import AlienBomb


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
        self.ship = Ship(self) #把 Ship 类实例化，放进游戏里
        self.bullets = pygame.sprite.Group()#给飞船准备一个“弹夹”
        self.alien_bombs = pygame.sprite.Group()#为外星人炸弹建立一个专属空弹夹：
        self.firing = False
        self.last_shot_time = 0

        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)#计分板
        self.play_button = Button(self, "Play")# 创建 Play 按钮
        # 创建存储游戏统计信息的实例，并创建记分牌
        self.sb = Scoreboard(self)
        
        
        self._create_fleet()#多个
        # 舰队的移动设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 代表向右移动，-1 代表向左移动

        # 难度升级与分数倍率设置
        self.speedup_scale = 1.2  # 每次升级，外星人提速 20%
        self.alien_points = 50    # 第一波外星人的基础击杀分数
        self.score_scale = 1.5    # 每次升级，击杀分数变为 1.5 倍

        '''alien = Alien(self)
        self.aliens.add(alien)#单个'''

        self.clock = pygame.time.Clock()
        # 初始化 Pygame 的混音器
        pygame.mixer.init()
        
        # 加载背景音乐和音效
        pygame.mixer.music.load('sounds/bg_music.ogg')
        self.laser_sound = pygame.mixer.Sound('sounds/laser.ogg')
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion.ogg')
        
        # 设置音量（0.0 到 1.0 之间）
        pygame.mixer.music.set_volume(0.3)
        self.laser_sound.set_volume(0.4)
        self.explosion_sound.set_volume(0.5)

        # 让背景音乐无限循环播放（-1 代表无限循环）
        pygame.mixer.music.play(-1)
    def _check_fleet_edges(self):
        """如果有任何一个外星人到达边缘，就让整个舰队下移，并改变方向"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                # 让所有外星人往下掉一点
                for a in self.aliens.sprites():
                    a.rect.y += self.fleet_drop_speed
                # 掉完之后，全体反方向移动
                self.fleet_direction *= -1
                break

    def _update_aliens(self):
        """检查是否有外星人到达边缘，然后更新所有外星人的位置"""
        self._check_fleet_edges()
        # 让编组里的所有外星人都执行移动动作
        self.aliens.update(self.alien_speed, self.fleet_direction)
        
        # 检查是否有外星人撞到了飞船
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        # 检查是否有外星人到达了屏幕底部
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 只要有一个外星人触底，就等同于飞船被撞毁，执行死亡后果
                self._ship_hit()
                break
        # 新的智能投弹机制：确保编组里还有存活的外星人
        if self.aliens.sprites():
            # 整个外星人舰队每刷新一帧，只有 3% 的总概率投下一颗炸弹
            if random.randint(1, 100) <= 3:
                # 随机抽取一个外星人作为投弹手，打破“死板的竖线”
                random_alien = random.choice(self.aliens.sprites())
                new_bomb = AlienBomb(self, random_alien)
                self.alien_bombs.add(new_bomb)
    #处理“挨揍”的全新动作
    def _ship_hit(self):
        """响应飞船被外星人撞到，或者外星人到达底部"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1  # 扣除一条命
            self.sb.prep_ships()        # 立刻刷新左上角的小飞船！

            self.bullets.empty()        # 清空屏幕上的子弹
            self.aliens.empty()         # 清空屏幕上的外星人
            self.alien_bombs.empty()
            
            # 把飞船重新放回屏幕底部中央，并重新召唤满编舰队
            self.ship.rect.midbottom = self.screen.get_rect().midbottom
            self._create_fleet()
            
            # 暂停 0.5 秒钟，让玩家喘口气知道自己死了一次
            time.sleep(0.5)
        else:
            # 命用光了，游戏停止，显示鼠标，让玩家可以重新点 Play 按钮
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 让所有子弹往上飞
        self.bullets.update()
        
        # 删除飞出屏幕边缘的子弹（不然它们会在后台无限飞，让电脑越来越卡）
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # 检查是否有子弹击中了外星人，如果有，就让子弹和外星人一起消失
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.explosion_sound.play()  #只要发生碰撞，立刻播放轰隆声！
            # 遍历字典里的所有击中记录，确保每个死亡的外星人都算分
            for aliens_hit in collisions.values():
                self.stats.score += self.alien_points * len(aliens_hit)
            self.sb.prep_score()
            if collisions:
                # 遍历字典里的所有击中记录，确保每个死亡的外星人都算分
                for aliens_hit in collisions.values():
                    self.stats.score += self.alien_points * len(aliens_hit)
                self.sb.prep_score()
                self.sb.check_high_score()  # 新增：立刻检查是否破了纪录！
            
        # 如果外星人军团死光了（编组为空）
        if not self.aliens:
            # 清空屏幕上可能还剩下的残余子弹
            self.bullets.empty()
            # 重新召唤一支满编的全新舰队！
            self._create_fleet()
            # 升级：提升舰队速度，并增加下一波的击杀奖励！
            self.alien_speed *= self.speedup_scale
            self.alien_points = int(self.alien_points * self.score_scale)
    def _update_alien_bombs(self):
        """更新外星人炸弹的位置，处理越界和碰撞"""
        self.alien_bombs.update()
        
        # 删除掉出屏幕底部的炸弹（回收内存）
        screen_rect = self.screen.get_rect()
        for bomb in self.alien_bombs.copy():
            if bomb.rect.top >= screen_rect.bottom:
                self.alien_bombs.remove(bomb)
                
        # 检查炸弹是否精准命中了你的飞船！
        if pygame.sprite.spritecollideany(self.ship, self.alien_bombs):
            self._ship_hit()

    def _create_fleet(self):
        """自动计算屏幕大小，并排满外星人舰队"""
        # 1. 先造一个“模版”用来测量单兵尺寸
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        
        # 2. 计算横向能排多少个（左右各留出安全距离）
        available_space_x = self.screen.get_rect().width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # 3. 计算纵向能排多少行（下方给飞船留出活动空间）
        ship_height = self.ship.rect.height
        available_space_y = self.screen.get_rect().height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        
        # 4. 真正开始批量制造并排好队形
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                new_alien = Alien(self)
                # 计算出精确的小数坐标，并存入 self.x 中
                new_alien.x = float(alien_width + 2 * alien_width * alien_number)
                new_alien.rect.x = new_alien.x  # 让物理框跟上小数坐标
                new_alien.rect.y = alien_height + 2 * alien_height * row_number
                
                self.aliens.add(new_alien)
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 1. 侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_SPACE:
                        '''制造一颗新子弹，并把它塞进弹夹里
                        new_bullet = Bullet(self)
                        self.bullets.add(new_bullet)'''
                        self.firing = True
                elif event.type == pygame.KEYUP:    #松开按键
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_SPACE:
                        self.firing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 获取鼠标点击的坐标
                    mouse_pos = pygame.mouse.get_pos()
                    # 如果点中了 Play 按钮，而且当前游戏是停止的
                    if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
                        # 重置生命值，开启游戏开关，隐藏鼠标
                        self.stats.reset_stats()
                        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
                            self.stats.reset_stats()
                            self.stats.game_active = True
                            pygame.mouse.set_visible(False)
                        
                        # 新增：重置游戏的初始速度和初始分数
                        self.alien_speed = 1.0
                        self.alien_points = 50
                        self.sb.prep_score()
                        self.sb.prep_ships()  # 点击重玩时，恢复满血的3艘飞船
                        self.stats.game_active = True
                        pygame.mouse.set_visible(False)
                        
                        # 清空残余的子弹和外星人
                        self.bullets.empty()
                        self.aliens.empty()
                        self.alien_bombs.empty()
                        
                        # 重新把飞船放好，召唤新舰队
                        self._create_fleet()
                        self.ship.rect.midbottom = self.screen.get_rect().midbottom

            if self.firing:
                # 获取现在的游戏时间
                current_time = pygame.time.get_ticks()
                # 如果距离上次开火超过了 200 毫秒（数字越大，子弹越稀疏）
                if current_time - self.last_shot_time > 200:
                    new_bullet = Bullet(self)
                    self.bullets.add(new_bullet)
                    # 记录下这次真正的开火时间
                    self.last_shot_time = current_time
                    self.laser_sound.play()  # 每次制造子弹，就播放一次激光声！
            # 只有游戏激活时，才更新这些物体的位置
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()#每次循环时让子弹“飞起来”
                self._update_bullets()
                self._update_aliens()  # 呼叫外星人大军移动！
                self._update_alien_bombs()  # 让炸弹飞起来
            
            # 2. 每次循环时都重绘屏幕背景
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            #外星人军团（目前只有一个）
            self.aliens.draw(self.screen)
            # 画出外星人的红色炸弹
            for bomb in self.alien_bombs.sprites():
                bomb.draw_bomb()
            # 画出得分
            self.sb.show_score()

            # 如果游戏处于非活动状态，就绘制 Play 按钮
            if not self.stats.game_active:
                self.play_button.draw_button()


            self.ship.blitme()#每次刷新屏幕时，都调用飞船的专属画图动作

            # 3. 让最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(250)

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

'''pygame.init()：这是 Pygame 的启动引擎，必须在做任何操作前调用，它会让 Pygame 准备好底层的显卡、声卡等硬件接口。

无限循环 while True:：这是游戏的“心跳”。所有的电子游戏底层都是一个死循环，它在一秒钟内运行几十次（帧率），不断做三件事：接收玩家输入 -> 更新游戏状态 -> 重新渲染画面。

pygame.event.get()：这是接收玩家输入的地方。当玩家点击窗口右上角的 X 时，会触发 pygame.QUIT 事件，我们调用 sys.exit() 安全结束程序。

pygame.display.flip()：这是游戏开发中常用的“双缓冲”技术。我们在内存中画好一帧（填上浅灰色），然后调用 flip() 将其推送到显示器上。这能防止玩家看到画面一点点画出来的闪烁感。'''