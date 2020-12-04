#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/11/19 17:18
@desc:
"""
from selenium.webdriver.common.by import By
from common import utils
from page.base_page import BasePage


class UserPage1(BasePage):
    def to_user_page(self):  # 跳转到我的页面
        self.find((By.ID,"main_item_user"))

    def to_login_text(self):  # 点击登录按钮
        self.find((By.ID,"my_login_state_out_tv"))

    def send_mobile(self,mobile):
        mobile_text = self.find((By.ID,"login_phone_et"))
        mobile_text.send_keys(mobile)

    def send_sms_code(self):
        self.find((By.ID,"login_btn"))
        self.find((By.ID,"tip_content_tv"))
        code_msg = self.find((By.ID,"tip_content_tv")).text  # 获取验证码信息
        code = utils.get_code(code_msg) # 根据正则表达式获取到6位验证码数字

        self.find((By.ID,"tip_dtn"))  # 获取到确认框，并且点击
        self.find((By.ID,"et_code"))

        for x in code:
            self.press_key(utils.get_press_key(x))


class UserPage(BasePage):
    def login(self):
        LOGIN_FILEPATH = "../../config/action_yaml/customer/" + "user.yaml"
        self.yaml_parse(LOGIN_FILEPATH,"Login")


if __name__ == "__main__":
    u = UserPage()
    u.login()