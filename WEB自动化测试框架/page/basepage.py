# -*- coding: utf-8 -*-
"""
@Time ： 2022-06-01 21:11
@Auth ： 小胡
@File ：basepage.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import inspect
import json
import os
import time
from random import random
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from WEB自动化测试框架.common import logger, con_db, get_global
from WEB自动化测试框架.common import setting

class BasePage():
    logger = logger
    con_db = con_db
    base_url = ''

    def __init__(self,driver:WebDriver=None):
        # 调用【get_value】方法，从跨模块全局变量中获取【浏览器驱动】的名字：如edge
        self.browser = get_global.get_value("browser")
        self._driver = ""
        if driver is None:
            #判断浏览器名称，执行对应浏览器的驱动方法，生成driver
            if self.browser == 'chrome':
                self._driver = webdriver.Chrome(setting.BROWSER_DRIVER_PARH['chrome'])
            elif self.browser == 'edge':
                self._driver = webdriver.Edge(setting.BROWSER_DRIVER_PARH['edge'])
            elif self.browser == 'firefox':
                #使用路径变量时，Firefox 里面一定要加：executable_path，不然会报错： NotADirectoryError: [WinError 267] 目录名称无效。: 'E:\\Python_Learns\\WEB自动化测试框架\\driver\\geckodriver.exe'
                self._driver = webdriver.Firefox(executable_path=setting.BROWSER_DRIVER_PARH['firefox'])
            else:
                print('没有找到浏览器驱动')
        else:
            self._driver = driver
        if self.base_url != '':
            self._driver.get(self.base_url)
            self._driver.maximize_window()


    def get_element(self, *locator, wait_time=20, per_time=1):
        '''
         查找获取单个元素
        :param locator: 元素的定位方式 和 元素属性 ，元组的形式
        :param wait_time: 显示等待时间
        :param per_time: 查找间隔时间
        :return:
        '''
        ele = WebDriverWait(self._driver, wait_time, per_time).until(lambda dr: dr.find_element(*locator))
        logger.info(f'定位元素：{locator}')
        return ele
    def get_elements(self, *locator, wait_time=20, per_time=1):
        '''
        查找获取多个元素 （值 为列表）
        :param locator: 元素的定位方式 和 元素属性 ，元组的形式
        :param wait_time: 显示等待时间
        :param per_time: 查找间隔时间
        :return:
        '''
        ele = WebDriverWait(self._driver, wait_time, per_time).until(lambda dr: dr.find_elements(*locator))

        return ele
    def input_text(self, value, *locator):
        '''
        封装 文本框输入 方法
        :param value: 输入的内容
        :param locator: 元素定位方法和属性
        :return:
        '''
        ele = self.get_element(*locator)
        # 清空元素
        ele.clear()
        # 输入文本内容
        ele.send_keys(value)
        logger.info(f'输入数据：{value}')
    def click(self,*locator):
        '''
        封装  点击操作 方法
        :param locator: 元素定位方法和属性
        :return:
        '''
        self.get_element(*locator).click()
        logger.info(f'执行点击操作')
    def select_by_value(self, value,*locator ):
        '''
        下拉框选择 --- 通过文本值选择
        :param value: 文本值
        :param locator: 元素定位方法和属性
        :return:
        '''
        Select(self.get_element(*locator)).select_by_value(value)
        logger.info(f'通过文本选择下拉框成功')
    def select_by_index(self, *locator):
        '''
        下拉框选择---- 通过index下标随机选择
        :param locator: 元素定位方法和属性
        :return:
        '''
        indexs = Select(self.get_element(*locator)).options
        index = random.randint(1, len(indexs) - 1)
        Select(self.get_element(*locator)).select_by_index(index)
        logger.info(f'通过index下标随机选择下拉框成功，下标为：{index}')
    def switch_to_frame(self,*locator):
        '''
        封装 切换到指定的frame框架 的方法
        :param locator:
        :return:
        '''
        iframe = self.get_element(*locator)
        self._driver.switch_to.frame(iframe)
        logger.info('frame框架切换成功')
    def switch_to_default_frame(self):
        '''
        切换到最外层框架（从frame切换出去）
        :return:
        '''
        self._driver.switch_to.default_content()
        logger.info('成功切换出frame框架')
    # js操作
    def execute_js(self, js):
        '''
        执行 js 语句操作
        :param js:
        :return:
        '''
        self._driver.execute_script(js)
        logger.info('执行js操作成功')
    def page_source(self):
        '''
        封装 获取页面源码 的方法
        :return:
        '''
        page_source =self._driver.page_source
        logger.info('获取页面源码成功')
        return page_source
    # 截图并保存
    def sav_png(self):
        logger.info('调用截图操作...')
        # 生成图片名称
        picture_name = '失败截图：' + time.strftime("%Y-%m-%d %H-%M-%S") + '.png'
        # 获取保存图片的路径
        picture_path = os.path.join(setting.SAVE_SCREENSHOT_PATH, picture_name)
        self._driver.get_screenshot_as_file(picture_path)
        logger.info(f'截图保存成功,图片路径：{picture_path}')
        # return picture_name
    #清空文本框数据
    def clear(self, *locator):
        ele = self.get_element(*locator)
        ele.clear()

    # 关闭浏览器
    def quit_browser(self):
        '''
        关闭浏览器，清楚残余的 driver.exe
        :return:
        '''
        self._driver.quit()
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im chromedriver.exe")
        logger.info('关闭浏览器')
    def should_element_contain(self, caseid, how, what, expt):
        '''
        封装断言方法 --- 包含
        :param caseid:
        :param how:
        :param what:
        :param expt:
        :return:
        '''
        # 通过参数how、what得到实际结果 => 元素的文本内容
        try:
            ele = self.get_element(how, what)
            self.rest = ele.text
        except Exception as e:
            logger.exception(f'预期结果的定位元素【{what}】没找到')
            self.sav_png()
            raise e
        try:
            # 断言
            assert expt in self.rest
            logger.info(f"断言成功，【{caseid}】 测试通过！")
        except Exception as e:
            logger.info(f"断言失败，【{caseid}】 测试失败！期望结果为：{expt},实际结果为：{self.rest}")
            # 截图操作
            self.sav_png()
            raise e
