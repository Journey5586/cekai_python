# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-20 17:05
@Author: 郭志国 
@File：init_driver.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
from selenium import webdriver
import sys,os

from selenium.webdriver.remote.webdriver import WebDriver

sys.path.append('../')

from common.conf.get_conf_data import GetConfData

# print(os.path.dirname(os.path.realpath(__file__)))
class InitWebDriver:

    def init_webdriver(self)->WebDriver:

        conf = GetConfData()
        browser = conf.get_browser()
        if 'firefox' == browser:
            __driver = webdriver.Firefox(executable_path=conf.get_firefox_driver())
        else :
            print(conf.get_chrome_driver())
            __driver = webdriver.Chrome(executable_path=conf.get_chrome_driver())

        return __driver

