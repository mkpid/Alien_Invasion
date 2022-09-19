# Mkpid
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """ 初始化游戏，创建一个屏幕对象"""
    pygame.init()                                     #初始化背景设置
    ai_settings = Settings()
    #创建屏幕对象
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")            #主题

    play_button = Button(ai_settings,screen,'Play')   #创建play按钮对象
    stats = GameStats(ai_settings)                    #创建游戏统计信息对象
    sb = Scoreboard(ai_settings,screen,stats)         #创建记分牌
    ship = Ship(ai_settings,screen)                   #创建飞船对象
    bullets = Group()                                 #创建存储子弹的编组
    aliens = Group()                                  #创建存储外星人的编组
    gf.create_fleet(ai_settings,screen,ship,aliens)   #创建外星人群

    #开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()