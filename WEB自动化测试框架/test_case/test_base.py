# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-16 18:48
@Auth ： 小胡
@File ：test_base.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from WEB自动化测试框架.common import logger


class TestBase:
    name = ''
    logger = logger
    def setup_class(self):
        logger.info(f'【{self.name}】开始测试')
    def teardown_class(self):
        logger.info(f'【{self.name}】测试结束')