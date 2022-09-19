# Mkpid
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200       #屏幕宽度
        self.screen_height = 600       #屏幕高度
        self.bg_color = (230,230,230)  #背景色彩元组
        #飞船设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #外星人设置
        self.alien_speed_factor = 0.1
        self.fleet_drop_speed = 0.5
        self.fleet_direction = 1        # fleet_direction 为1表示向右移动，为-1表示向左移动

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # fleet_direction 为1表示向右移动，为-1表示向左移动

    def increase_speed(self):
        """提高所以对于设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale




