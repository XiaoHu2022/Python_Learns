# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-02 21:16
@Auth ： 小胡
@File ：send_request.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
'''
1、根据用例发送对应的方法（get、post....）的http请求
2、能够动态的接收不同的请求参数：json、parmas、data、headers、cookies
'''
import requests
def send_http_request(url,method,**kwargs):
    session = requests.Session()
    #把方法名转化为小写，防止误传
    method = method.lower()
    #获取对应的方法
    return getattr(session,method)(url=url,**kwargs)
if __name__ == '__main__':
    print(send_http_request('http://www.baidu.com', 'GET'))
