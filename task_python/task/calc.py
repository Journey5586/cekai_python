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

    def add(self, a: int or float, b: int or float) -> int or float or None:
        '''
        进行简单的加法运算   \n
        :param a: 第一个参数
        :param b: 第二个参数
        :return: 整数或浮点数
        '''
        try:
            return round(a + b, 1)
        except Exception:
            print('出现了异常，数字不能与非数字相加，具体错误信息如下：\n\n', traceback.format_exc())
            return None

    def div(self, a: int or float, b: int or float) -> int or float or None:
        '''
        进行简单的除尘运算    \n
        :param a: 除数
        :param b: 被除数
        :return: 整数或浮点数
        '''
        try:
            return round(a / b, 1)

        except Exception:
            print('出现了异常，数字不能与非数字及0相除，具体错误信息如下：\n\n', traceback.format_exc())
            return None

    def add1(self, a: int or float, b: int or float) -> int or float or None:
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

    def div1(self, a: int or float, b: int or float) -> int or float or None:
        '''
        进行简单的除尘运算    \n
        :param a: 除数
        :param b: 被除数
        :return: 整数或浮点数
        '''
        try:
            return a / b

        except Exception:
            print('出现了异常，数字不能与非数字及0相除，具体错误信息如下：\n\n', traceback.format_exc())
            return None

    def sub(self, a: int or float, b: int or float) -> int or float or None:
        '''
        进行简单的减法运算
        :param a:
        :param b:
        :return:
        '''
        try:
            return round(a - b, 1)

        except Exception:
            print('出现了异常，数字不能与非数字相减，具体错误信息如下：\n\n', traceback.format_exc())
            return None

    def mul(self, a: int or float, b: int or float) -> int or float or None:
        '''
        进行简单的乘法运算
        :param a:
        :param b:
        :return:
        '''
        try:
            return round(a * b, 1)

        except Exception:
            print('出现了异常，数字不能与非数字相乘，具体错误信息如下：\n\n', traceback.format_exc())
            return None

# calc = Calc()
# try:
#     print(calc.add(1, '1'))
# except Exception:
#     print('afsafa:', traceback.format_exc())
