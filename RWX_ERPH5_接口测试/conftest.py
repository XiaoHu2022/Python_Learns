# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-09 15:40
@Auth ： 小胡
@File ：conftest.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import re

import pytest
import requests



# @pytest.fixture(scope='session')
# def get_cookies(self):
# 	#获取cookie
# 	url = 'http://localhost/HHERP/'
# 	res = requests.get(url=url)
# 	cookie = re.findall("Id=(.*?);",res.headers['Set-Cookie'])[0]
# 	self.params['cookie'] = cookie
# 	print(cookie)
# 	yield cookie


from RWX_ERPH5_接口测试.test_case.base import Base


@pytest.fixture(scope='session')
def user_login():
	url = 'http://localhost/HHERP/CarpaServer/CarpaServer.LoginService.ajax/UserLogin'
	headers = {
		"Cookie": f"BS0518=00000; BS0513=00000; LoginDataBase=BS0518; ASP.NET_SessionId={Base.cookie}"
	}
	data = {
		"user": {
			"isChange": "",
			"password": "",
			"database": "BS0518",
			"name": "管理员",
			"userid": "00000",
			"KeyNo": "err",
			"Level": -1,
			"HardDiskNo": "errdisk",
			"MacAddress": "errmac"
		}
	}
	# self.session = requests.Session()
	res = requests.post(url=url, json=data, headers=headers)
	print(Base.cookie)
	print(res.json())

# if __name__ == '__main__':
#     user_login()