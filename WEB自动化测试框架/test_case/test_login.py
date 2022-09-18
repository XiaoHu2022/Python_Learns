# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-01 21:34
@Auth ： 小胡
@File ：test_login.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from time import sleep

import pytest

from WEB自动化测试框架 import setting
from WEB自动化测试框架.common.read_excl import read_excel
from WEB自动化测试框架.page.main import Main
from WEB自动化测试框架.test_case.test_base import TestBase


class TestLogin(TestBase):
    name = '登录页面'
    def setup(self):
        self.main = Main()
    @pytest.mark.parametrize('data', read_excel(setting.TEST_DATA_FILE['test_login']['file_path'],
                                                setting.TEST_DATA_FILE['test_login']['sheet_name']['login']))
    def test_login(self,data):
        self.main.goto_login().login(data['test_data']['username'],data['test_data']['password'])
        #断言
        self.main.should_element_contain(data['case_id'],data['exp']['by'],data['exp']['locater'],data['exp']['exp_value'])
        self.main.quit_browser()
if __name__ == '__main__':
    pytest.main(['-s','-v',__file__])
