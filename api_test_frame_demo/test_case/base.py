# -*- coding: utf-8 -*-
"""
@Time ： 2022-09-03 19:55
@Auth ： 小胡
@File ：base.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import json
import re

from jsonpath import jsonpath

from api_test_frame_demo.common import con_db,logger
from api_test_frame_demo import setting
from api_test_frame_demo.common.re_replace import re_replace
from api_test_frame_demo.common.send_request import send_http_request


class Base:
    logger = logger
    con_db = con_db
    setting = setting
    name = ''
    _params = {}
    def setup_class(self):
        pass
        self.logger.info(f'{self.name}接口开始执行')
    def teardown_class(self):
        self.logger.info(f'{self.name}接口执行结束')
    def get_tests_steps(self,data):
        self.logger.info(f'用例【{data["case_title"]}】-----开始执行')
        #绑定对象属性，便于下面的测试流程函数去处理
        self.data = data
        #1、接口依赖，测试数据的替换处理
        self.replace_test_data()
        #2、测试步骤
        self.step()
        #3、响应状态码断言
        self.assert_status_code()
        #4、响应数据断言
        self.assert_response_data()
        #5、数据库断言
        self.assert_db_true()
        #6、业务流测试中，提取上一个接口的响应数据，并保存到用例类属性中  --- excel文件中也需添加这一列
        self.get_extract_data()
        self.logger.info(f'用例【{data["case_title"]}】-----执行结束')
        return self.data,self.res

    def replace_test_data(self):
        '''
        接口依赖的参数是存在 全局变量self._params 中的，通过 此方法，对文件中的数据进行替换
        :return:
        '''
        raw = json.dumps(self.data)
        #循环读取BasePage类中_params 字典的键和值
        for key,value in self._params.items():
            #这里的键名key，与yaml文件中的变量名一致，如：${name},然后用键值将它替换
            #raw 是字符串
            raw = raw.replace(f'${{{key}}}',str(value))
        #json.loads：重新加载，将字符串转为json字典格式
        self.data = json.loads(raw)
        # print(self.data)
        #将data中的request，expect，转换为字典格式
        try:
            self.data['request'] =  json.loads(self.data['request'])
            self.data['expect'] =  json.loads(self.data['expect'])
            if self.data.get('sql'):
                self.data['sql'] = json.loads(self.data['sql'])
        except Exception as e:
            self.logger.exception(f'用例{self.data["case_title"]}的json数据格式不正确！')
            raise e
        # #拼接URL地址,判断文件中的url是否是全路径
        if not self.data['url'].startswith('http'):

            self.data['url'] = setting.PROJECT_HOST + setting.INTERFACES_URL[self.data['url']]
    def step(self):
        '''
        测试步骤
        :return:
        '''
        try:
            self.res = send_http_request(self.data['url'], self.data['method'], **self.data['request'])
            # print(f'res_json-----------:{self.res.json()}')
        except Exception as e:
            self.logger.exception(f'用例{self.data["case_title"]}发送http错误！')
            self.logger.debug(f'url:{self.data["url"]}')
            self.logger.debug(f'method:{self.data["method"]}')
            self.logger.debug(f'args:{self.data["request"]}')
            raise e
    def assert_status_code(self):
        '''
        响应状态码断言
        :return:
        '''
        # 3.1  响应状态码断言
        try:
            assert int(self.data['status_code']) == self.res.status_code
        except Exception as e:
            self.logger.exception(f'用例【{self.data["case_title"]}】---响应状态码断言失败！')
            raise e
        else:
            self.logger.info(f'用例【{self.data["case_title"]}】---响应状态码断言成功!')

    def assert_response_data(self):
        '''
        断言json响应数据
        :return:
        '''
        # 3.2  响应结果断言
        try:
            # 这里逻辑写死了，断言字段只针对当前项目
            assert self.data['expect']['errcode'] == self.res.json()['errcode']
            assert self.data['expect']['errmsg'] == self.res.json()['errmsg']
        except Exception as e:
            self.logger.exception(f'用例【{self.data["case_title"]}】----请求json结果断言失败！')
            raise e
        else:
            self.logger.info(f'用例【{self.data["case_title"]}】----请求json结果断言成功！')

    def assert_db_true(self):
        '''
        --- 校验一条或者多条sql语句，文件中的格式写成列表：['select * from class_room where class_id=1;',.......]
        读取excel文件中的sql字段
        通过执行sql查询语句，返回Ture或False,断言数据库是否存在该数据
        :return:
        '''
        # 数据库断言
        if self.data.get('sql'):
            # 因为需要列表，所以将json字符串格式的列表，转换成python的对象---列表
            sqls = json.loads(self.data['sql'])
            for sql in sqls:
                try:
                    assert True == self.con_db.exist_data(sql)
                except Exception as e:
                    self.logger.exception(f'用例【{self.data["case_title"]}】---数据库断言失败！')
                    raise e
                else:
                    self.logger.info(f'用例【{self.data["case_title"]}】--- 数据库断言成功')
    def get_extract_data(self):
        '''
        业务流测试中，提取上一个接口的响应数据，并保存到用例类属性中
        :return:
        '''
        if self.data.get('extract'):
            try:
                #将json格式数据转换成python对象
                exps = json.loads(self.data['extract'])
            except Exception as e:
                raise ValueError(f'用例{self.data["case_title"]}的extract提取表达式格式不正确',e)
            for item in exps:
                #要保存的类属性的名称
                name = item['name']
                #要提取数据的jsonpath表达式
                exp = item['exp']
                res_json = jsonpath(self.res.json(),exp)
                if res_json:
                    #保存到类属性
                    # setattr(self.__class__,name,res_json[0])
                    self._params[name] = res_json[0]
                else:
                    raise ValueError(f'用例{self.data["case_titl"]}提取表达式错误',exp)



