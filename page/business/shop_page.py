#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/11/19 17:47
@desc:
"""

from selenium.webdriver.common.by import By
from common import utils
from page.base_page import BasePage
from page.customer.user_page import UserPage


class ShopPage(UserPage):
    def nav_name(self):
        return self.find((By.ID,"nav_tv_title")).text