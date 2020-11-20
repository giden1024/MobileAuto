#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/4/42:43 PM
@desc:
'''
from selenium.webdriver.common.by import By
from driver.Appium import Appium
from lxml import etree


class BasePage:
    black_list = ["//*[@li]"]

    def __init__(self):
        Appium.initDriver()

    def find(self,locate):
        try:
            Appium.driver.find_element(locate)
        except Exception as e:
            psource = Appium.driver.page_source
            html = etree.parse(psource)
            for x in self.black_list:
                if html.xpath(x):
                    Appium.driver.find_element(By.xpath,x)

    def find_one(self,locate,num):
        Appium.driver.find_elements(locate)[int(num)]
