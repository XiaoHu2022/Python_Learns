# -*- coding: utf-8 -*-
"""
@Time ： 2022-08-31 20:09
@Auth ： 小胡
@File ：setting.py.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os

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
PROJECT_HOST = 'https://qyapi.weixin.qq.com'
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
    'member_change':{
        'file_path':os.path.join(BASE_DIR,'data/excel.xlsx'),
        # sheet名
        'sheet_name':{
            'get_token':'get_token',
            'member_change':'member_change'
        }
    }
}

