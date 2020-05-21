# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020-5-20 20:32
@Author: 郭志国 
@File：wx_addmember.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
from selenium.webdriver.common.by import By
from po_base.base import Base


class AddMember(Base):
    __username = (By.ID,'username')
    __memberid = (By.ID,'memberAdd_acctid')
    __phone = (By.ID,'memberAdd_phone')
    __save = (By.XPATH,'//a[text()="保存"]')
    __del = (By.XPATH,'//a[text()="删除"]')
    __submit= (By.XPATH,'//a[text()="确认"]')
    username= 'test1'
    memberid = 'test1'
    phone = 12345678001

    def add_member(self):
        # 参数化，先不进行，后续再补
        self.send_keys(self.__username,self.username)
        self.send_keys(self.__memberid,self.memberid)
        self.send_keys(self.__phone,self.phone)
        self.clicks(self.__save,0)
        return True

    def get_member(self):
        ''''''
        # 参数化及一些校验，暂时工作太忙，没有时间写，后续再补
        eles = self.finds((By.XPATH,'//span[text()="'+self.username+'"]'))
        namelist = []
        for ele in eles:
            namelist.append(ele.text)

        return namelist

    def del_member(self):
        ''''''
        print('//span[text()="'+self.username+'"]/../preceding-sibling::td[1]]')
        self.find((By.XPATH,'//span[text()="'+self.username+'"]/../preceding-sibling::td[1]')).click()
        self.click(self.__del)
        self.click(self.__submit)
        return True




