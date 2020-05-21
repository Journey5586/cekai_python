# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-21 0:29
@Author: 郭志国 
@File：test_wx_addmember.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import time
import sys
sys.path.append('../')

from task_python.common.conf.init_driver import InitWebDriver
from task_python.po_page.wx_addmember import AddMember
from task_python.po_page.wx_index import Index
from task_python.po_page.wx_login import Login
from task_python.po_page.wx_menucontact import MenuContact


class TestAddmember:

    def setup_class(self):
        init = InitWebDriver()
        self._driver = init.init_webdriver()
        # self.index = Index(self._driver)
        self.login = Login(self._driver)
        self.contact = MenuContact(self._driver)
        self.addmember = AddMember(self._driver)

    def test_addmember(self):
        self.login.scanf()
        self.contact.goto_addmember()
        self.addmember.add_member()
        result = self.addmember.get_member()
        assert 'test1' in result

    def test_deldata(self):
        self.addmember.del_member()
        time.sleep(2)

    def teardown_class(self):
        self.login.quite()