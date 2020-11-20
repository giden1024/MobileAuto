#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/4/31:45 PM
@desc:
'''
from appium import webdriver
import time
import pytest,unittest
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LearnPO.driver.Appium import Appium
from LearnPO.Page.Search import Search
from LearnPO.Page.XueQiu import XueQiu
from LearnPO.Page.quotes import Quotes



class TestXueqiu(unittest.TestCase):
    def setUp(self):
        # 配置app的各项参数,初始化driver
        # Appium.initDriver()

        #  配置app的各项参数
        self.caps = {}
        self.caps["platformName"] = "android"
        self.caps["deviceName"] = "xueqiu"
        self.caps["appPackage"] = "io.appium.android.apis"
        self.caps["appActivity"] = ".ApiDemos"
        self.caps["autoGrantPermissions"] = "true"
        self.caps["uiautomationName"]="uiautomator2"
        self.caps["newCommandTimeout"] = 600

    def test_pdd(self):
        xueqiu = XueQiu()
        # xueqiu.agreed()
        search = xueqiu.to_serach()
        search.serach("pdd")
        search.choose()
        search.follow()
        search.evaluate()
        search.cancel()

        quotes = search.to_quotes()
        assert quotes.my_choose_value() == "拼多多"

    def test_2(self):
        xueqiu = XueQiu()
