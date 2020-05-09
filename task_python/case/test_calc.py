# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-8 20:04
@Author: guo
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
import yaml
sys.path.append('../task')
from task_python.task.calc import Calc

class TestCalc:
    '''
    测试calc文件
    '''
    def setup_class(self):
        self.calc = Calc()
        # print('../data/calc_add.yaml')

    @pytest.mark.parametrize('a,b,result',yaml.safe_load(open('../data/calc_add.yaml')))
    def test_add(self,a,b,result):
        # print(a,b,result)
        # print(type(result))
        res_tmp = self.calc.add(a,b)
        assert result == res_tmp

    @pytest.mark.parametrize('a,b,result',yaml.safe_load(open('../data/calc_div.yaml')))
    def test_div(self,a,b,result):
        # print(a,b,result)
        res_tmp = self.calc.div(a,b)
        assert result == res_tmp

if __name__ == '__main__':
    # 为啥经常push失败呢
    # pytest.main()
    # 校验一下，这是master主分支
    # 2020-05-09 11:31
    # 20200509 11:40 0801分支
    # 11:56 0801 分支
    # 12：01 master
    pytest.main()

