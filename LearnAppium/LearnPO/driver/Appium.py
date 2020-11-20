#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/4/25:49 PM
@desc:
'''

from appium.webdriver.webdriver import WebDriver
from appium import webdriver
import time
import pytest,unittest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Appium:

    # driver = None
    # """:type : WebDriver"""
    "@type driver: WebDriver"
    driver:WebDriver


    @classmethod
    def initDriver(cls) -> WebDriver:
        # 配置app的各项参数
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "demo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(5)
        return cls.driver




