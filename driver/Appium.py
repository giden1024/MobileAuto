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
        # caps["appActivity"] = ".main.MainActivity"
        caps["skipServerInstallation"] = True  # 手机首次安装appium的时候需要安装，后续不再需要，将值设置为True
        caps["skipDeviceInitialization"] = True  # 手机首次安装appium的时候需要安装，后续不再需要，将值设置为True
        caps["autoGrantPermissions"] = True  # 启动时候弹窗权限默认为开启
        caps['newCommandTimeout'] = 600  # 代码执行完成之后的等待时间，单位是秒
        caps['noReset'] = True  # 应用启动不重新设置
        # caps['fullReset'] = False
        caps['dontStopAppOnReset'] = True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)  # 创建一个新的会话
        cls.driver.implicitly_wait(10)  # 隐式等待10秒

    @classmethod
    def get_driver(cls) -> WebDriver:
        return cls.driver


if __name__ == "__main__":
    a = Appium
    a.init_driver()
    print(type(a.get_driver()))
