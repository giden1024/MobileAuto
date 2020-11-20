#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/3/3110:53 PM
@desc:
'''
from appium import webdriver
import time
import pytest,unittest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestDemoApi(unittest.TestCase):
    def setUp(self):
        #  配置app的各项参数
        self.caps = {}
        self.caps["platformName"] = "android"
        self.caps["deviceName"] = "demo1"
        self.caps["appPackage"] = "io.appium.android.apis"
        self.caps["appActivity"] = ".ApiDemos"
        self.caps["autoGrantPermissions"] = "true"
        self.caps["uiautomationName"]="uiautomator2"
        self.caps["newCommandTimeout"] = 600


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)

    def test_toast(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_android_uiautomator\
            ('new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "Popup Menu")').click()
        self.driver.find_element_by_accessibility_id("Make a Popup!").click()
        # time.sleep(1000)
        self.driver.find_element_by_xpath("//*[@text='Search']").click()
        print(self.driver.find_element_by_xpath("//*[contains(@text,'Clicked')]").text)

        # toast_message = 'Clicked popup menu item Search'
        # message = "//*[@text={}]".format(toast_message)
        # self.driver.find_element_by_xpath(message)

        # toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
        #toast在锤子手机上无法识别
        # self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']")
        # time.sleep(1000)


    def test_webview(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_android_uiautomator\
            ('new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "WebView")').click()
        # self.driver.find_element_by_xpath("//*[contains[@text,'i am a link']").click()
        self.driver.find_element_by_accessibility_id("i am a link").click()
        page_text = self.driver.find_element_by_accessibility_id("I am some other page content").text
        print(page_text)

