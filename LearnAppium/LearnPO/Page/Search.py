#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/4/26:16 PM
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy

from LearnPO.driver.Appium import Appium
from LearnPO.Page.quotes import Quotes
from Page.base_page import BasePage


class Search(BasePage):

    _search_input = (MobileBy.ID, "search_input_text")
    _choose_icon = (MobileBy.ID,"name")
    _follow_btn = (MobileBy.ID,"")

    def serach(self,keyword):
        self.find(*self._search_input).send_keys(keyword)
        return self

    def choose(self):
        self.finds(*self._choose_icon)[0].click()
        return self

    def follow(self):
        # if Appium.driver.find_element_by_xpath()
        return Appium.driver.find_element_by_id("follow_btn").click()

    # 点击取消按钮
    def cancel(self):
        Appium.driver.find_element_by_id("action_close").click()
        return self

    # 暂时不评价
    def evaluate(self):
        Appium.driver.find_element_by_id("tv_left").click()
        return self

    # 跳转到自选页面
    def to_quotes(self):
        Appium.driver.find_elements_by_id("tab_name")[1].click()
        return Quotes()