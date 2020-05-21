# !/usr/bin/python
# -*- coding: UTF-8 -*- 
# 设置utf-8  显示中文
"""
@Create Time: 2020/5/14 18:29
@Author: 郭志国 
@File：get_conf_data.py
@Description: 
1.
2.
@Modify Time:  
@Modify Description: 
1.
2.
"""
import yaml
import os


class GetConfData:
    # driver节点 key
    __node_driver = 'Driver'
    # browser的key
    __broswer = 'browser'
    # timeout 的key(这为显示等待超时时间)
    __driver_wait_timeout = 'wait_timeout'
    # implicitly timeout 的key(这为隐式等待超时时间)
    __driver_implicitly_timeout = 'implicitly_timeout'
    # 驱动exe 名称对应的key
    __driver_chrome_name = 'chrome_driver_name'
    __driver_firefox_name = 'firefox_driver_name'
    __driver_ie_name = 'ie_driver_name'
    # url
    __url = 'url'

    def __init__(self):
        '''
        在这里将进行读取数据的初始化动作
        '''
        self.__root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        yaml_file_name = 'run_property.yaml'
        yaml_file_dir = 'conf'
        ymal_file_path = os.path.abspath(os.path.join(self.__root_path, os.path.join(yaml_file_dir, yaml_file_name)))
        self.__driver_dir = 'driver'
        self.__driver_path = os.path.join(self.__root_path, self.__driver_dir)
        self.yaml_datas = yaml.safe_load(open(ymal_file_path))
        self.keys_list = self.__get_ymal_kyes()
        self.driver_data = self.__get_driver_dict()

    def __get_ymal_kyes(self):
        '''
        获取yaml文件最外层的keys
        :return:
        '''
        __keys_list = []
        for key in self.yaml_datas.keys():
            __keys_list.append(key)
        return __keys_list

    def __get_driver_dict(self):
        '''
        获取Driver节点的所有的配置数据
        :return:
        '''
        driver_data = None

        for key in self.yaml_datas.keys():
            if self.__node_driver == key:
                driver_data = self.yaml_datas.get(key)
                return driver_data
        return driver_data

    def __get_driver_file_path(self, driver_name):
        return os.path.join(self.__driver_path, driver_name)

    def get_browser(self):
        '''
        获取浏览器名称
        :return:
        '''
        browser = None
        for key in self.driver_data.keys():
            if key == self.__broswer:
                browser = self.driver_data.get(key)
                return browser
        return browser

    def get_chrome_driver(self):
        '''
        获取chrome 浏览器的driver exe路径
        :return:
        '''
        driver_name = None
        for key in self.driver_data.keys():
            if key == self.__driver_chrome_name:
                driver_name = self.driver_data.get(key)
                # return driver_name

                return self.__get_driver_file_path(driver_name)

        return driver_name

    def get_firefox_driver(self):
        '''
        获取firefox浏览器的driver exe路径
        :return:
        '''
        driver_name = None
        for key in self.driver_data.keys():
            if key == self.__driver_firefox_name:
                driver_name = self.driver_data.get(key)
                # return driver_name
                return self.__get_driver_file_path(driver_name)
        return driver_name

    def get_wait_timeout(self):
        '''
        获取显示等待时间
        :return:
        '''
        wait_timeout = None

        for key in self.driver_data.keys():

            if key == self.__driver_wait_timeout:
                wait_timeout = self.driver_data.get(key)
                return wait_timeout
        return wait_timeout

    def get_implicitly_timeout(self):
        '''
        获取浏览器名称
        :return:
        '''
        implicitly_timeout = None
        for key in self.driver_data.keys():
            if key == self.__driver_implicitly_timeout:
                implicitly_timeout = self.driver_data.get(key)
                return implicitly_timeout
        return implicitly_timeout

    def get_url(self):
        '''
        获取url
        :return:
        '''
        url = None
        for key in self.driver_data.keys():
            if key == self.__url:
                implicitly_timeout = self.driver_data.get(key)
                return url
        return url
