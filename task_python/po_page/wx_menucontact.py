# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-20 20:26
@Author: 郭志国 
@File：wx_menucontact.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from po_base.base import Base
from po_page.wx_addmember import AddMember


class MenuContact(Base):

    __add_member = (By.XPATH,'//a[text()="添加成员"]')
    def __init__(self,driver):

        self.__driver = driver
        super().__init__(driver)

    def goto_addmember(self):


        self.clicks(self.__add_member,0)
        time.sleep(2)

        return AddMember(self.__driver)
