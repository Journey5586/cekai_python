# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-20 15:45
@Author: 郭志国 
@File：wx_index.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
from po_base.base import Base
from po_page.wx_login import Login
from po_page.wx_register import Register


class Index(Base):

    def goto_login(self):
        '''登录'''
        return Login()

    def goto_register(self):
        '''去注册'''
        return Register()

