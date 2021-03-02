# -*- coding: UTF-8 -*-

"""

@Project Name: alien_invasion
@File Name:    game_stats

@User:         smile
@Author:       Smile
@Email:        Xiaofei.Smile365@Gmail.com

@Date Time:    2021/2/22 10:38
@IDE:          PyCharm

"""


import json


class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高分
        # 读取json文件存档，获得最高分
        try:
            with open("./image/high_score.json") as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
