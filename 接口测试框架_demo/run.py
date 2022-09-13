# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-13 15:00
@Auth ： 小胡
@File ：run.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
'''run文件，主程序执行入口'''
import pytest
from 接口测试框架_demo.test_case.test_member_change import TestMemberChange

class Run():
    def setup_class(self):
        self.member_change = TestMemberChange
    def run(self):
        #运行整个类下面的用例
        self.member_change()
if __name__ == '__main__':
    pytest.main(['-s', '-v', '--alluredir=reporter/myreport', '--junitxml=reporter/result.xml', __file__])
    os.popen('allure generate reporter/myreport -o reporter/report --clean')
    os.popen('allure open reporter/report')