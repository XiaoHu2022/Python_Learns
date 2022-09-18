# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-15 15:36
@Auth ： 小胡
@File ：test_1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from time import sleep

import pytest
from selenium import webdriver

from WEB自动化测试框架.page.basepage import BasePage
from WEB自动化测试框架.page.login_later_main import LoginLaterMain

name = ('name','accounts')
passwd = ('name','pwd')
login_btn= ('xpath','/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button')
class Login(BasePage):
    def go_to_login_main(self,username='alive',password='123456'):
        '''
        登录成功后，跳转至登录后的首页
        :param username:
        :param password:
        :return:
        '''
        self.input_text(username, *name)
        self.input_text(password, *passwd)
        self.click(*login_btn)
        # return LoginLaterMain(self._driver)
    def login(self,username,password):
        '''
        执行用例的登录方法
        :param username:
        :param password:
        :return:
        '''
        self.input_text(username,*name)
        self.input_text(password,*passwd)
        self.click(*login_btn)
        sleep(2)
    # 执行登录用例后，获取元素定位，用于测试类中进行断言成功或失败
    def get_login_assert(self,by,locater):
        ele = self.get_element(by,locater).text
        return ele
# if __name__ == '__main__':
#     # pytest.main(['-s',__file__])
#     t = Test1()
#     t.test_login_success()