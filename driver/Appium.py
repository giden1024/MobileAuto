#!/user/bin/env python
#coding=utf-8
'''
@author: mayuyang
@file: Appium.py
@time: 2020/5/13 13:39
@desc:

'''

from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class Appium:
    "@type driver: WebDriver"
    driver: WebDriver

    @classmethod
    def init_driver(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["platformVersion"] = "5.1.1"
        caps["deviceName"] = "127.0.0.1:62001 device"
        caps["uiautomationName"] = "uiautomator2"
        caps["appPackage"] = "com.chinaredstar.shop.uat"  # 海狸逛逛uat包名
        caps["appActivity"] = "com.chinaredstar.shop.ui.home.MainActivity"  # 海狸逛逛Activity名称
        caps["skipServerInstallation"] = "true"  # 手机首次安装appium的时候需要安装，后续不再需要，将值设置为True
        caps["skipDeviceInitialization"] = "true"  # 手机首次安装appium的时候需要安装，后续不再需要，将值设置为True
        caps["autoGrantPermissions"] = "true"  # 启动时候弹窗权限默认为开启

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)  # 创建一个新的会话
        cls.driver.implicitly_wait(10)  # 隐式等待10秒

    @classmethod
    def get_driver(cls) -> WebDriver:
        return cls.driver


if __name__ == "__main__":
    a = Appium
    a.init_driver()
    print(type(a.get_driver()))
