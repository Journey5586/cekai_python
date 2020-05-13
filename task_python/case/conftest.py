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


def pytest_collection_modifyitems(session, config, items:list):
    for item in items:
        case_name = item.name
        if 'add' in case_name:
            item.add_marker(pytest.mark.add)
        elif "sub" in case_name:
            item.add_marker(pytest.mark.sub)
        elif "div" in case_name:
            item.add_marker(pytest.mark.div)
        elif 'mul' in case_name:
            item.add_marker(pytest.mark.mul)
