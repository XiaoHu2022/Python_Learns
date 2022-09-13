# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-02 21:55
@Auth ： 小胡
@File ：get_token.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import json
from api_test_frame_demo.common.read_excl import read_excel
from api_test_frame_demo.common.send_request import send_http_request
import pytest
from api_test_frame_demo.test_case.base import Base


class TestGetToken(Base):
    def setup_class(self):
        self.logger.info('---------获取token用例开始执行-----------')
    def teardown_class(self):
        self.logger.info('---------获取token用例执行结束-----------')
    def test_get_token(self):
        data = read_excel(Base.setting.TEST_DATA_FILE['member_change']['file_path'],
                          Base.setting.TEST_DATA_FILE['member_change']['sheet_name']['get_token'])[0]
        data['request'] = json.loads(data['request'])
        data['expect'] = json.loads(data['expect'])
        data['url'] = self.setting.PROJECT_HOST + self.setting.INTERFACES_URL[data['url']]
        r = send_http_request(data['url'],data['method'],**data['request'])
        access_token = r.json()['access_token']

        assert data['expect']['errcode'] == 0
        assert data['expect']['errmsg'] == 'ok'
        return access_token

if __name__ == '__main__':
    pytest.main(['-sv',__file__])