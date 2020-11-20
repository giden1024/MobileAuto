#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/11/19 10:40
@desc:
"""



from selenium.webdriver.common.by import By

from page.business.shop_page import ShopPage
from page.customer.user_page import UserPage


def test_login_success():

    u = ShopPage()
    u.to_user_page()
    u.to_login_text()
    u.send_mobile("18721705015")
    u.send_sms_code()
    assert u.nav_name() == "店铺"

    #
    # shop_name = driver.find((By.ID,"nav_tv_title")).text
    #
    # assert shop_name == "店铺"

