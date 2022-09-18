# -*- coding: utf-8 -*-
"""
@Time ： 2022-08-31 20:09
@Auth ： 小胡
@File ：setting.py.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os
import time

'使用python文件设置 配置文件的参数'
#项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
#日志文件的配置参数
LOG_CONFIG = {
    'name':'test5',
    'filename':os.path.join(BASE_DIR,'log/test5.log'),
    'debug':False
}
print(LOG_CONFIG['filename'])
#数据库的参数
DB_MYSQL = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123456',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}
#项目ip地址
PROJECT_HOST = 'http://shop-xo.hctestedu.com/'
#接口url路径
INTERFACES_URL = {
    'add_member':'/cgi-bin/user/create',
    'query_member':'/cgi-bin/user/get',
    'update_member':'/cgi-bin/user/update',
    'delete_member':'/cgi-bin/user/delete',
    'get_token':'/cgi-bin/gettoken'
}
#测试数据文件的路径配置
TEST_DATA_FILE = {
    'test_login':{
        'file_path':os.path.join(BASE_DIR,'data/login.xlsx'),
        # sheet名
        'sheet_name':{
            'login':'login',
        }
    }
}
# 保存失败截图的文件夹路径
SAVE_SCREENSHOT_PATH = os.path.join(BASE_DIR,'image')
print(SAVE_SCREENSHOT_PATH)

#不同浏览器驱动的路径
BROWSER_DRIVER_PARH = {
    'chrome':os.path.join(BASE_DIR,'driver/chromedriver.exe'),
    'firefox':os.path.join(BASE_DIR,r'driver/geckodriver.exe'),
    'edge':os.path.join(BASE_DIR,'driver/msedgedriver.exe')
}
print(BROWSER_DRIVER_PARH)


