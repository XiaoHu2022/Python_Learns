# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-09 20:14
@Auth ： 小胡
@File ：get_cookies.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import re

import requests


def get_cookies():
    # 获取cookie
    url = 'http://localhost/HHERP/'
    res = requests.get(url=url)
    cookie = re.findall("Id=(.*?);", res.headers['Set-Cookie'])[0]

    print(cookie)
    return cookie