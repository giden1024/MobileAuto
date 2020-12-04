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
    driver = None
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

    el1 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView[1]")
    el1.click()
    el2 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/cn.bingoogolapple.swipebacklayout.BGASwipeBackLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout")
    el2.click()