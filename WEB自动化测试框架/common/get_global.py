# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-17 17:50
@Auth ： 小胡
@File ：glo.py.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
新建一个文件，定义一个“全局变量管理模块” ，实现跨文件获取全局变量，并且调用。
如：从【文件1】通过 【set_value(key,value)】方法获取值，这时候global_dict字典中有值了
然后，在【文件2】调用 【get_value(key,defValue=None)】方法，并赋值给一个变量，实现变量值的调用
'''
def init():
    '''
    #初始化，先必须在主模块（文件1）初始化（只在文件1中执行一次一次即可）
    :return:
    '''
    global global_dict
    global_dict = {}
def set_value(key,value):  #set_value方法，必须写在【文件1】的函数中
    """ 定义一个全局变量 """
    global_dict[key] = value
def get_value(key,defValue=None):  #get_value方法，必须写在【文件2】的函数中
    '获得一个全局变量,不存在则返回默认值'
    print(f'get-value  key:{key}')
    browser = global_dict[key]
    try:
        return browser
    except KeyError as e:
        raise e

