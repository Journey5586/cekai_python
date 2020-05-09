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

items = yaml.safe_load_all(open('../data/calc.yaml'))
add_dict = None
div_dict = None
add_key = 'add'
div_key = 'div'

# 获取yaml文件里的 各个方法对应的数据源
for item in items:
    if isinstance(item,dict):
        if add_key in item.keys():
            add_dict = item.get(add_key)
        elif div_key in item.keys():
            div_dict = item.get(div_key)

print(add_dict)
print(div_dict)

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

    @pytest.mark.parametrize('add_dict_tmp',add_dict)
    def test_add_01(self,add_dict_tmp):
        '''
        此时的dict为一个字典。   \n
        :param dict_tmp: 数据源字典
        :return: None
        '''
        dict_tmp = add_dict_tmp
        a = dict_tmp.get('a')
        b = dict_tmp.get('b')
        result = dict_tmp.get('result')
        res_tmp = self.calc.add(a,b)
        assert  result == res_tmp

    @pytest.mark.parametrize('div_dict_tmp',div_dict)
    def test_div_01(self,div_dict_tmp):
        dict_tmp = div_dict_tmp
        a = dict_tmp.get('a')
        b = dict_tmp.get('b')
        result = dict_tmp.get('result')
        print(a,b,result)
        res_tmp = self.calc.div(a,b)
        assert result == res_tmp

if __name__ == '__main__':
    # 为啥经常push失败呢
    # pytest.main()

    pytest.main(['-vs','test_calc.py'])

