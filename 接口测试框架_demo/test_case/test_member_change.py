# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-02 21:02
@Auth ： 小胡
@File ：test_member_change.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import json
import sys,os
import pytest

from 接口测试框架_demo.common.get_token import TestGetToken
from 接口测试框架_demo.common.read_excl import read_excel
from 接口测试框架_demo.test_case.base import Base


class TestMemberChange(Base):
    name = '成员管理业务流'
    def setup_class(self):
        self.access_token = TestGetToken.test_get_token(self)
        # print(self.access_token)
        self._params["access_token"] = self.access_token

    @pytest.mark.parametrize('data',read_excel(Base.setting.TEST_DATA_FILE['member_change']['file_path'],
                                               Base.setting.TEST_DATA_FILE['member_change']['sheet_name']['member_change']))
    def test_member(self,data):
        self.get_tests_steps(data)
#
# if __name__ == '__main__':
#     pytest.main(['-sv',__file__])