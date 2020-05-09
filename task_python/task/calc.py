# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-8 19:59
@Author: guo
@File：calc.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import traceback


class Calc:
    '''
    一个简单的计算器，只进行简单的加和除的运算
    '''

    def add(self, a: int or float, b: int or float) -> int or float:
        '''
        进行简单的加法运算   \n
        :param a: 第一个参数
        :param b: 第二个参数
        :return: 整数或浮点数
        '''
        try:
            return a + b
        except Exception:
            print('出现了异常，数字不能与非数字相加，具体错误信息如下：\n\n', traceback.format_exc())
            return None

    def div(self, a: int or float, b: int or float) -> int or float:
        '''
        进行简单的除尘运算    \n
        :param a: 除数
        :param b: 被除数
        :return: 整数或浮点数
        '''
        try:
            return a/b

        except Exception:
            print('出现了异常，数字不能与非数字相除，具体错误信息如下：\n\n', traceback.format_exc())
            return None


# calc = Calc()
# try:
#     print(calc.add(1, '1'))
# except Exception:
#     print('afsafa:', traceback.format_exc())
