# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-13 19:09
@Author: 郭志国 
@File：conftest.py
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

sys.path.append('../task')

from task_python.task.calc import Calc

@pytest.fixture()
def init_calc():
    calc = Calc()
    return calc
