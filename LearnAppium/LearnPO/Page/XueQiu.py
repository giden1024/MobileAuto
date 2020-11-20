#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/4/26:16 PM
@desc:
'''
from LearnPO.driver.Appium import Appium
from LearnPO.Page.Search import Search
from LearnPO.Page.quotes import Quotes
from Page.base_page import BasePage


class XueQiu(BasePage):



    # 同意协议
    def agreed(self):
        self.find("tv_agree").click()
        # return self

    # 跳转到查询页面
    def to_serach(self):
        self.find("com.xueqiu.android:id/tv_search").click()
        return Search()







if __name__ == "__main__":
    x = XueQiu()
    x.agreed()