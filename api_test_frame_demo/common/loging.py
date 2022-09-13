# -*- coding: utf-8 -*-
"""
@Time ： 2022-08-31 17:02
@Auth ： 小胡
@File ：loging.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
''' 封装日志模块 '''
import logging
def get_logging(name,filename,mode='a',encoding='utf8',fmt=None,debug=False):
    '''
    :param name: 日志器名字
    :param filename: 创建的日志文件名
    :param mode: 操作日志的方式，默认为 追加
    :param encoding: 字符编码，默认为utf-8
    :param fmt:输出 日志的 格式
    :param debug:调试模式
    :return:
    '''
    #创建日志器
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #如果 debug参数为True,写入文件的等级为 DEBUG，控制台输出等级为DEBUG
    if debug is True:
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else: #如果 debug参数为False,写入文件的等级为 WARNING，控制台输出等级为INFO
        file_level = logging.WARNING
        console_level = logging.INFO
    if fmt is None:
        fmt = '%(levelname)s  %(asctime)s-[%(filename)s-->line:%(lineno)d]:%(message)s'
    #创建日志处理器
    witer_log = logging.FileHandler(filename=filename,mode=mode,encoding=encoding)
    witer_log.setLevel(file_level)
    console_log = logging.StreamHandler()
    console_log.setLevel(console_level)
    #创建格式化器
    formater = logging.Formatter(fmt=fmt)
    #将格式化器添加到日志处理器上
    witer_log.setFormatter(formater)
    console_log.setFormatter(formater)
    #将日志处理器添加到日志器上
    logger.addHandler(witer_log)
    logger.addHandler(console_log)
    return logger

if __name__ == '__main__':
    logger = get_logging('test','../log/test.log',debug=True)
    logger.debug('debug')
    logger.info('info')
    logger.warning('警告')
    logger.error('error')
    logger.critical('严重')