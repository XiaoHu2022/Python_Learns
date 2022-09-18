# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-16 22:17
@Auth ： 小胡
@File ：conftest.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

from WEB自动化测试框架.common import get_global

def pytest_addoption(parser):
    '''
    hook 函数，自定义配置命令行参数
    :param parser:
    :return:
    '''
    #配置执行浏览器命令行参数：--browser ,默认为谷歌浏览器驱动
    parser.addoption("--browser",action="store",dest='browser',default='chrome')
def pytest_configure(config):
    '''
    pytest_configure函数，接收命令行参数信息
    :param config:
    :return:
    '''
    # print(f'======================,{config.getoption("--browser")}')
    #获取【控制台输入】并存储在pytest.main([])中的命令行参数：--browser 的值，如：edge ，并赋值给browser
    browser = config.getoption("--browser")
    #调用get_global文件中定义的 跨模块全局变量
    get_global.init()  # 先必须在主模块初始化（只在Main模块需要一次即可
    # 将【浏览器驱动类型】的名称如：edge，存储在跨模块全局变量中
    get_global.set_value('browser',browser)
    # print(f"----------------gol.get_value:{gol.get_value('browser')}")




