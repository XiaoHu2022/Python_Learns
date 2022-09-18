# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-16 18:58
@Auth ： 小胡
@File ：run.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from WEB自动化测试框架.common.get_command_line import get_options
from WEB自动化测试框架.test_case.test_login import TestLogin
import pytest
'''run文件，主程序执行入口'''
class Run():
    def setup_class(self):
        self.test_login = TestLogin
    def run(self):
        #运行整个类下面的用例
        self.test_login()
if __name__ == '__main__':
    args = ['-s', '-v', '--alluredir=reporter/myreport', '--junitxml=reporter/result.xml', __file__]
    arg = get_options('--browser')  #从控制台命令行中，获取命令行参数，如：python run.py --browser edge,  获取浏览器驱动【edge】的名字，执行对应浏览器
    if arg:
        args.insert(0,f'--browser={arg}') #将命令行参数的值如：edge，插入到pytest命令行中：--browser=edge
    print(args)
    pytest.main(args)
    os.popen('allure generate reporter/myreport -o reporter/report --clean')
    os.popen('allure open reporter/report')