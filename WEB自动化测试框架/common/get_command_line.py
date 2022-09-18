# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-17 12:50
@Auth ： 小胡
@File ：tt.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import sys
def get_options(name):
    '''
    获取控制台传入的命令行的参数
    :param name: 传入的参数名 如：--browser
    :return:
    '''
    #从第一个开始切片，执行命令 python run.py --browser edge ，sys.argv方法获取的数据是[run.py,--browser,edge]，第一个不需要
    args = sys.argv[1:]
    if name in args:
        #返回参数值，如：edge  -----   args.index(name)+1 ：返回参数名【对应下标+1】的下标
        return args[args.index(name)+1]
    else:
        return ''
if __name__ == '__main__':
    res = sys.argv
    print(res)