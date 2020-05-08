# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-8 19:59
@Author: 郭志国 
@File：calc.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""

class Calc:
    '''
    一个简单的计算器，只进行简单的加和除的运算
    '''

    def add(self,a:int or float,b:int or float) ->int or float:
        '''
        进行简单的加法运算   \n
        :param a: 第一个参数
        :param b: 第二个参数
        :return: 整数或浮点数
        '''
        return a+b