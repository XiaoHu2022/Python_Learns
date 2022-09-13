# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-03 16:06
@Auth ： 小胡
@File ：re_replace.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
找出excel文件中每条数据中的所有需要替换的参数，使用正则表达式进行替换
'''
import re
def re_replace(json_data,obj):
    #1、找出所有的槽位中的变量名
    args = re.findall('#(.*?)#',json_data)
    print(f'====================={args}====================')
    for arg in args:
        #使用反射，找到obj中对应的arg属性的值,没有找到返回None
        value = getattr(obj,arg,None)
        print(f'______________________{value}')
        if value:
            json_data = json_data.replace(f'#{arg}#',str(value))
    return json_data