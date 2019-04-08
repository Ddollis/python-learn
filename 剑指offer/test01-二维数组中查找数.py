# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array) - 1
        cols = len(array[0]) - 1
        i = rows
        j = 0
        while j <= cols and i >= 0:
            if target < array[i][j]:
                i -= 1
            elif target > array[i][j]:
                j += 1
            else:
                return True
        return False
