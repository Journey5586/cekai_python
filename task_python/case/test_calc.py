# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-8 20:04
@Author: 郭志国 
@File：test_calc.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import pytest
import sys
sys.path.append('./')
from task_python.task.calc import Calc

class TestCalc:
    '''
    测试calc文件
    '''
    def setup_class(self):
        self.calc = Calc()

    def test_add(self):
        result = self.calc.add(1,'2')

        assert 3 == result


if __name__ == '__main__':
    pytest.main()
