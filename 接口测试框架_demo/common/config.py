# -*- coding: utf-8 -*-
"""
@Time ： 2022-08-31 19:37
@Auth ： 小胡
@File ：config.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
 解析配置文件中的数据
'''
from configparser import ConfigParser

import yaml
def get_config(filename,encoding='utf-8'):
    #1、获取文件后缀名
    suffix = filename.split('.')[-1]
    #2、判断这个配置文件的类型
    if suffix in ['ini','cfg','cnf']:
        # ini文件格式化
        conf = ConfigParser()
        conf.read(filename,encoding=encoding)
        #将 ini 文件中的内容，解析成一个大字典

        data = {}
        for section in conf.sections():
            data[section] = dict(conf.items(section))
    elif suffix in ['yaml','yml']:
        #yaml文件格式
        with open(filename,encoding=encoding) as f:
            data = yaml.safe_load(f)
    else:
        print('暂不支持这种类型的配置文件！')
    return data
if __name__ == '__main__':
    print(get_config('../config.yaml'))
    print(get_config('../config.ini'))