# coding=utf-8
from random import randint


class Die(object):
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面之间的随机值"""
        return randint(1, self.num_sides)
