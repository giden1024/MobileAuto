#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/3/262:47 PM
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
from Page.Search import Search
from Page.XueQiu import XueQiu
from Page.quotes import Quotes



class TestXueqiu(unittest.TestCase):
    def setUp(self):
        # 配置app的各项参数

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "domo"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["automationName"] = "UiAutomator2"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        

    def test_pdd(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/splash_text_tv")
        # el1.click()
        # el3 = self.driver.find_element_by_id("tv_search")


        # el3.click()
        # self.driver.save_screenshot("/search.png")

        # el4 = self.driver.find_element_by_id("search_input_text")
        # el4.send_keys("alibaba")

        # self.driver.press_keycode(66)

        # self.driver.save_screenshot("/pdd.png")

        # el5 = self.driver.find_element_by_id("follow_btn")
        # el5.click()

    def swipe(self,by,director):
        self.driver.swipe()

    def test_my(self):
        self.driver.implicitly_wait(5)
        ele1 = self.driver.find_elements_by_id("tab_name")[1]
        ele1.click()
        ele2 = self.driver.find_element_by_id("portfolio_stockName")
        assert ele2.text == "拼多多"
    def test_new(self):
        pass

    def test_device(self):
        element = self.driver.find_element_by_id("")
        print(self.mycaps)
        self.driver.lock(5)
        self.driver.unlock()
        self.driver.quit()
        self.driver.find_element_by_id("")
        TouchAction(self.driver).long_press(element).perform()

    def test_alibaba_search(self): #  寻找alibaba
        pass

    def test_ele(self):  # 寻找元素
        self.driver.swipe(200,200,200,10000)
        print(self.driver.location())

#     def test_action(self):
#         self.driver.execute_script("mobile:shell",{
#     'command': 'echo',
#     'args': ['arg1', 'arg2'],
#     'includeStderr': True,
#     'timeout': 5000
# })
    def find(self,*args):
        try:
            self.driver.find_element(*args)
        except Exception:
            print()

    def loaded(self):
        locations = ["x","y"]
        while locations[-1] != locations[-2]:
            element = self.driver.find_element_by_xpath("//*[@text='交易' and contains(@resourse-id,'tab_name')]")
            locations.append(element)

    def test_xueqiu_zixuan(self):
        self.driver.find_element_by_id("tv_agree").click()
        self.driver.implicitly_wait(3)
        # self.loaded()
        # self.driver.find_element_by_xpath('//*[@text="交易" and contains(@resourse-id,"tab_name")]').click()
        self.driver.find_elements_by_id("tab_name")[2].click()
        # self.driver.find_element_by_xpath('//*[@[text="交易"]').click()
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_accessibility_id("A股开户 万2.5佣金，低息融资，高级行情免费领 免费领 ").click()
        for i in range(5):
            time.sleep(0.5)
            print(self.driver.contexts) # 打印所有的上下文
            self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
            print(self.driver.current_context) # 打印当前的上下文
            print(self.driver.page_source)
        try:
            # 显式等待
            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".trade_home_agu_3ki")))
            element.click()
        finally:
            print(1)

if __name__ == "__main__":
    t = TestXueqiu()
    t.test_ele()

