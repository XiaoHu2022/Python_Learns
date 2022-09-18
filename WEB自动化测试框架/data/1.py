# -*- coding: utf-8 -*-
"""
@Time ： 2022-08-14 2:20
@Auth ： 小胡
@File ：1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import inspect
import json

import yaml

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class T:
    _params = {}
    options = Options()
    options.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    def test_steps1(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            '''
                因为yaml文件中的字典名是以函数名命名的，为了读取yaml文件时，执行指定的函数，所以需要传入函数名
                inspect.stack()[1].function：
                    参数0，表示传入当前函数（如：test_step）本身的名字
                    参数1，如果a函数中调用了当前函数（如：test_step），就传入a函数的名字
            '''
            function_name = inspect.stack()[1].function
            # test_steps 的数据格式是：{'hhh': [{'by': 'a', 'locator': 'b', 'click': 'c'}, {'by': 'a1', 'locator': 'b1', 'click': 'c1'},...]}
            # dict.get() 方法：就是获取对应键名的 键值
            test_steps = yaml.safe_load(f)
            # 根据传入的函数名，获取yaml文件中指定的字典键值对
            # steps 的数据格式是列表套字典：[{'by': 'a', 'locator': 'b', 'click': 'c'}, {'by': 'a1', 'locator': 'b1', 'click': 'c1'}, ....]
            steps = test_steps.get(function_name)
        # 将yaml文件中读取的数据 转成json字符串
        raw = json.dumps(steps)
        # 循环读取BasePage类中_params 字典的键和值
        for key, value in self._params.items():
            # 这里的键名key，与yaml文件中的变量名一致，如：${name},然后用键值将它替换
            raw = raw.replace('${' + key + '}', str(value))
        # 重新加载
        steps = json.loads(raw)
        for step in steps:  # 依次循环 读取出来的测试步骤
            if 'click' == step.get('action'):
                self.find(step.get('by'), step.get('locator')).click()
            elif 'send_keys' == step.get('action'):
                self.find(step.get('by'), step.get('locator')).send_keys(step.get('value'))
            else:
                self.finds(step.get('by'), step.get('locator'))
    def find(self,by,locator):
        return self.driver.find_element(by,locator)
    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)
    def get_member(self):
        elements = self.test_steps1('get_members.yaml')
        li = []
        for element in elements:
            # 获取每个人的手机号
            element = element.get_attribute('title')
            li.append(element)
        print(li)
        # 计数，用于统计这是第几行的用户
        count = 0
        # 循环所有列表中定位
        for element in li:
            count = count + 1
            # self._params['count'] = count
            # 如果指定手机号，在这个定位的文本中
            if '18581548888' == element:
                # 定位这个手机号最前面的复选框，并点击
                self.driver.find_element(By.XPATH, f'//*[@id="member_list"]/tr[{count}]/td[1]').click()
                print('执行1')
if __name__ == '__main__':
    t = T()
    t.get_member()



