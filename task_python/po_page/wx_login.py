# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-20 15:45
@Author: 郭志国 
@File：wx_login.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import shelve
import time

from selenium.webdriver.common.by import By

from po_base.base import Base
from po_page.wx_register import Register


class Login(Base):

    # def __init__(self,driver):
    #     super().__init__(driver)

    def scanf(self):
        '''扫码登录'''
        # 企业微信的url
        w_url = 'https://work.weixin.qq.com/wework_admin/frame'
        # 用来存放cookie的伪数据库的文件名
        cookie_file = '../data/weixin_cookie0516'
        # 这些cookies的值，对应哪个key
        save_cookie_key = 'wei_cookie'
        index_locator = (By.ID, 'menu_index')
        # 通讯录定位器
        locator = (By.ID, 'menu_contacts')
        # 第一次登录的操作
        self.open_url(w_url)
        self.max_page()

        # # ------------------ 第一次运行时，要打开的代码，在第二次选择时，要注释掉-----------------------------
        # # 第一次使用时，使用显示等待，第二次运行时，要注释掉该行代码
        # # Wait(self.driver, 15, 0.5).until(EC.visibility_of_element_located(index_locator)).click()
        # self.click(index_locator)
        #
        # # 使用with来打开并读取文件
        # # 第一次登录时,当进行第二次登录时，要注释如下两行的代码
        # with shelve.open(cookie_file) as w_db:
        #     # w_db[save_cookie_key] = self.driver.get_cookies()
        #     w_db[save_cookie_key] = self.get_cookies()
        # # ------------------ 第一次运行时，要打开的代码，在第二次选择时，要注释掉-----------------------------

        # 第二次运行脚本次运行之前，要将上面代码注释掉
        with shelve.open(cookie_file) as w_db:
            cookies = w_db[save_cookie_key]
        # ------------分割线，下面的代码，在第一次执行时，可以不运行,但是w_db.close()要运行--------------
        for cookie in cookies:
            # expiry 的值为时间戳，无用字段，且会影响cookie，要去掉
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
                # print('cookie-----', cookie)
            # self.driver.add_cookie(cookie)
            self.add_cookie(cookie)

        self.open_url(w_url)
        time.sleep(2)
        self.click(locator)
        time.sleep(3)

    # def goto_register(self):
    #     '''注册'''
    #     return Register()