# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-20 16:14
@Author: 郭志国 
@File：base.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import traceback

from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as Wait, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
import sys

sys.path.append('../')
from common.conf.get_conf_data import GetConfData
from common.conf.init_driver import InitWebDriver

conf = GetConfData()
wait_time = conf.get_wait_timeout()
implicitly_time = conf.get_implicitly_timeout()


class Base():
    __driver = None
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    # def __init__(self):
    #     self.__driver = InitWebDriver().init_webdriver()

    def open_url(self, url):
        ''''''
        self.__driver.get(url)

    def max_page(self):
        ''''''
        self.__driver.maximize_window()

    def quite(self):
        ''''''
        self.__driver.quit()

    def close(self):
        ''''''
        self.__driver.close()

    def find(self, locator: tuple) -> WebElement:
        '''
        请传入定位器 (By.ID,'username')   \n
        :param locator: (By.ID,'username')
        :return: WebElement or False
        '''
        if self.__locator_is_tuple(locator):
            try:
                ele = Wait(self.__driver, wait_time,0.5).until(EC.visibility_of_element_located(locator))
                # 当在实际运行脚本的时候，要注释下面这行代码，把使用上面那行代码
                # 之所以使用下面那行代码，是为了方便在写脚本的时候，可以进行提示，而上面那行代码则不会
                # ele = self.__driver.find_element(*locator)
                return ele
            except Exception:
                print(f'发生了异常，具体错误信息如下：\n{self.__print_detail_msg()}')
                return False
        else:
            print(f'传入的不是tuple类型的定位器，具体值如下：\n{locator}')
            return False

    def finds(self, locator: tuple) -> WebElement:
        ''''''
        if self.__locator_is_tuple(locator):
            try:
                print('finds: ',locator)
                # eles = Wait(self.__driver, wait_time).until(EC.visibility_of_all_elements_located(locator))
                eles = Wait(self.__driver, wait_time).until(EC.visibility_of_any_elements_located(locator))
                return eles
            except Exception:
                print('发生了异常，具体错误信息如下：\n')
                print(self.__print_detail_msg())
                return False
        else:
            print(f'你传入的不是tuple类型的定位器，你传入的定位器如下：\n{locator}')
            return False

    def send_keys(self, locator: tuple, key_value):
        ''''''
        ele = self.find(locator)
        ele.clear()
        ele.send_keys(key_value)

    def click(self,locator:tuple):
        ''''''
        print('click locator is:',locator)
        ele = self.find(locator)
        ele.click()

    def clicks(self,locator:tuple,index):
        ''''''
        eles = self.finds(locator)
        eles[index].click()

    def get_cookies(self):

        return self.__driver.get_cookies()

    def add_cookie(self,cookie):
        self.__driver.add_cookie(cookie)

    def __locator_is_tuple(self, locator) -> bool:
        ''''''
        if isinstance(locator, tuple):
            return True
        else:
            return False

    def __print_detail_msg(self):
        ''''''
        return traceback.format_exc()
