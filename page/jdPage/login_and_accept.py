#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/12/13 13:48
@desc:
"""

from selenium.webdriver.common.by import By
from common import utils
from page.base_page import BasePage
from page.customer.user_page import UserPage

class JdPage(BasePage):
    def accept(self):
        self.find(By.ID,"bpu").click()

    def close(self):
        if self.find(By.XPATH, "//*[text()='立即领取']"):
            self.find(By.ID,"mj").click()

    def login(self):
        self.find(By.ID,"a50").click()


