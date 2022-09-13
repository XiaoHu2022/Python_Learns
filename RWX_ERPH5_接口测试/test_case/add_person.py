# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-02 21:02
@Auth ： 小胡
@File ：test_member_change.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import json
import re
import sys,os
import pytest
import requests

from RWX_ERPH5_接口测试.test_case.base import Base


class TestMemberChange(Base):
    # name = '新增商品'
    params = {}
    def test_add_person(self,user_login):
        print(self.cookie)
        # session = requests.Session()
        url = 'http://localhost/HHERP/CarpaServer/CarpaServer.Base.EtypeEditService.ajax/SaveEtypeDataCreate'
        headers = {

            "Cookie": f"BS0518=00000; BS0513=00000; LoginDataBase=BS0518; ASP.NET_SessionId={self.cookie}"

        }
        print(headers)
        data = {
            "obj": {
                "efullname": "test_1",
                "eusercode": "001",
                "dtypeid": "",
                "enamepy": "test_1",
                "birthday": "1980-01-01",
                "tel": "",
                "toptotal": 0,
                "duty": "",
                "lowlimitdiscount": 0,
                "address": "",
                "isstop": 0,
                "ecomment": "",
                "commissionData": [],
                "typeIDR": "00001",
                "cmode": "E",
                "rowIndex": 0,
                "filename": None,
                "isSuccess": False,
                "pagestatus": 0,
                "parid": "00000"
            }
        }
        print(data)
        res = requests.post(url=url,json=data,headers=headers)
        print(f'------------{res.json()}')
        assert res.status_code == 200
        assert  res.json()['@errorvalue'] is None
        self.params['keyValues'] = res.json()['@rlttypeid']
        print(self.params['keyValues'])
    def test_update_person(self,user_login):
        url = 'http://localhost/HHERP/CarpaServer/CarpaServer.Base.EtypeEditService.ajax/SaveEtypeDataModify'
        data = {
            "obj": {
                "esonnum": 0,
                "etypeid": f"{self.params['keyValues']}",
                "parid": "00000",
                "esonnum2": 0,
                "eusercode": "002",
                "efullname": "test_2",
                "ename": "",
                "enamepy": "test_2",
                "ecomment": "",
                "dtypeid": "",
                "dfullname": "",
                "birthday": "1980-01-01",
                "tel": "",
                "address": "",
                "toptotal": 0,
                "isstop": 0,
                "duty": "",
                "lowlimitdiscount": 0,
                "savemenid": 0,
                "commissionData": [],
                "typeIDR": "00017",
                "cmode": "E",
                "rowIndex": 1,
                "filename": None,
                "isSuccess": False,
                "pagestatus": 2,
                "deleteFlag": False,
                "typeid": "00017"
            }
        }
        headers = {
            "Cookie": f"BS0518=00000; BS0513=00000; LoginDataBase=BS0518; ASP.NET_SessionId={self.cookie}"
        }
        res = requests.post(url=url,json=data,headers=headers)
        print(res.text)
    def test_delete_pereson(self):
        url = 'http://localhost/HHERP/CarpaServer/CarpaServer.Report.GetBaseGroupService.ajax/BasicInfoDelete'
        headers = {
            "Cookie": f"BS0518=00000; BS0513=00000; LoginDataBase=BS0518; ASP.NET_SessionId={self.cookie}"
        }
        data = {"obj":{"typeid":f"{self.params['keyValues']}","dbname":"Employee","type":"etype","mode":"E"}}
        res = requests.post(url=url,json=data,headers=headers)
        print(res.json())
if __name__ == '__main__':
    pytest.main(['-sv',__file__])
