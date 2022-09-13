# -*- coding: utf-8 -*-
"""
@Time ： 2022-08-31 19:31
@Auth ： 小胡
@File ：__init__.py.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from api_test_frame_demo import setting
from api_test_frame_demo.common.con_db import Con_DB

'''
将公共的参数写入 __init__  文件，调用时只执行一次
'''
from api_test_frame_demo.common.config import get_config
from api_test_frame_demo.common.loging import get_logging

#1、普通调用日志方法，其他文件只需导入：from  lemon接口测试.common import logger 包，然后将logger 赋值
# logger = get_logging('test','log/test.log',debug=True)
#2、通过解析ini、yaml类型的配置文件的方式，动态传参调用
# config = get_config('config.ini')
# print(config)
# logger = get_logging(**config['log'])
#3、通过解析py 类型的配置文件的方式，动态传参调用 ----  推荐使用
logger = get_logging(**setting.LOG_CONFIG)
#动态传入数据库参数
con_db = Con_DB(**setting.DB_MYSQL)
