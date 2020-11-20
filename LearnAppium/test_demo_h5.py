#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/4/23:59 PM
@desc:
'''

import unittest
import pytest
from appium import webdriver

class TestXueqieweb(unittest.TestCase):

    def setUp(self):
        # 配置app的各项参数
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo1"
        caps["browserName"] = "Browser"
        caps['noRest'] = "true"
        caps['fullReset'] = "false"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_login(self):
        self.driver.get("https://www.snowballsecurities.com/activity/open/open-v10?r=30004001&utm_campaign=M1-khh5&utm_medium%E2%80%A6")
        username = self.driver.find_elements_by_xpath('//*[@class="open_input-wrapper_13S"]/input')[0]
        username.click()
        username.send_keys("18721705015")

        pwd = self.driver.find_elements_by_xpath('//*[@class="open_input-wrapper_13S"]/input')[1]
        pwd.click()
        pwd.send_keys("888888")

        self.driver.find_element_by_xpath('//*[@class="open_form-submit_1Ms"]').click()


