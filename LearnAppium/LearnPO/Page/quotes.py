#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/4/31:29 PM
@desc:
'''

from LearnAppium.LearnPO.driver.Appium import Appium


class Quotes:

    def my_choose_value(self):
        return Appium().driver.find_element_by_id("portfolio_stockName").text