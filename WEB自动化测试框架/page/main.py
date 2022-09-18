# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-01 21:16
@Auth ： 小胡
@File ：main.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from WEB自动化测试框架.page.basepage import BasePage
from WEB自动化测试框架.page.login import Login

login_btn = ('xpath','//*[@class="am-btn-primary btn am-fl"]')

class Main(BasePage):
    base_url = BasePage.setting.PROJECT_HOST
    def goto_login(self):
        '''
        首页，点击登录按钮，跳转至登录页面
        :return:
        '''
        self.click(*login_btn)
        return Login(self._driver)
if __name__ == '__main__':
    m = Main()
    m.goto_login()
