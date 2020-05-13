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
import allure
import pytest
import sys
import yaml

sys.path.append('../task')
from task_python.task.calc import Calc

add_key = 'add'
div_key = 'div'
sub_key = 'sub'
mul_key = 'mul'
data_list = []
yaml_path = '../data/calc.yaml'
yaml_datas = yaml.safe_load_all(open(yaml_path))

# 获取yaml文件里所有的数据
for item in yaml_datas:
    data_list.append(item)
yaml_datas.close()


# 获取yaml文件里的 各个方法对应的数据源
def get_data(key):
    value = None
    for item in data_list:
        if key in item.keys():
            value = item.get(key)
            return value
    return value


# @pytest.fixture()
# def init_calc():
#     calc = Calc()
#     return calc


@allure.feature('计算器')
class TestCalc:
    '''
    测试calc文件
    '''

    # @allure.story('初始化')
    # def setup_class(self):
    #     self.calc = Calc()
    #     # print('../data/calc_add.yaml')

    # def setup_class(self,init_calc):
    #     self.calc = init_calc

    @allure.story('加法运算')
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../data/calc_add.yaml')))
    def test_add(self, init_calc, a, b, result):
        # print(a,b,result)
        # print(type(result))
        self.calc = init_calc
        res_tmp = self.calc.add(a, b)
        assert result == res_tmp

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../data/calc_div.yaml')))
    def test_div(self, init_calc, a, b, result):
        # print(a,b,result)
        self.calc = init_calc
        res_tmp = self.calc.div(a, b)
        assert result == res_tmp

    @allure.story('加法运算2')
    @pytest.mark.parametrize('add_dict_tmp', get_data(add_key))
    def test_add_01(self, init_calc, add_dict_tmp):
        '''
        此时的dict为一个字典。   \n
        :param dict_tmp: 数据源字典
        :return: None
        '''
        dict_tmp = add_dict_tmp
        a = dict_tmp.get('a')
        b = dict_tmp.get('b')
        result = dict_tmp.get('result')
        self.calc = init_calc
        res_tmp = self.calc.add(a, b)
        print(a,b,result,res_tmp)
        assert result == res_tmp

    @allure.story('除法运算2')
    @pytest.mark.parametrize('div_dict_tmp', get_data(div_key))
    def test_div_01(self, init_calc, div_dict_tmp):
        print(div_key, '============', div_dict_tmp)
        dict_tmp = div_dict_tmp
        a = dict_tmp.get('a')
        b = dict_tmp.get('b')
        result = dict_tmp.get('result')
        print(a, b, result)
        self.calc = init_calc
        res_tmp = self.calc.div(a, b)
        assert result == res_tmp

    @allure.story('乘法运算')
    @pytest.mark.parametrize('dict_tmp', get_data(mul_key))
    def test_mul(self, init_calc, dict_tmp):
        a = dict_tmp.get('a')
        b = dict_tmp.get('b')
        result = dict_tmp.get('result')
        self.calc = init_calc
        res_tmp = self.calc.mul(a, b)

        assert result == res_tmp

    @allure.story('减法运算')
    @pytest.mark.parametrize('dict_tmp', get_data(sub_key))
    def test_sub(self, init_calc, dict_tmp):
        a = dict_tmp.get('a')
        b = dict_tmp.get('b')
        result = dict_tmp.get('result')
        self.calc = init_calc
        res_tmp = self.calc.sub(a, b)

        assert result == res_tmp


if __name__ == '__main__':
    # 为啥经常push失败呢
    # pytest.main()

    pytest.main(['-vs', 'test_calc.py'])
