#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/12/4 10:10
@desc:
"""
import os
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from driver.Appium import Appium

a = Appium
a.init_driver()
driver = a.get_driver()
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']


def my_swipe(newdriver,start_y = 0.25,end_y = 0.9,duration = 5000):
    x1 = int(x * 0.5)
    y1 = int(y * start_y)
    x2 = int(x * 0.5)
    y2 = int(y * end_y)
    newdriver.swipe(x1,y2,x2,y1,duration)


def my_scroll(newdriver):
    start_ele = driver.find_element(By.ID,"banner_image")
    try:
        end_ele = driver.find_element(By.ID,"tv_loading_msg")
        if end_ele:
            newdriver.scroll(start_ele, end_ele, duration=100000)
        else:
            my_swipe(newdriver)
    except NoSuchElementException as no:
        print("没有这个")



def test_session():
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)
    print(driver.session) # 获取会话的capabilities
    time.sleep(2)
    my_swipe(driver)
    # my_scroll(driver)
    driver.find_elements(By.ID,"home_item_goods_img_iv")[1].click()
    driver.implicitly_wait(5)
    # driver.set_page_load_timeout(5)
    pagesource1 = driver.page_source
    with open("soure1.text",mode="w",encoding="utf-8") as f1:
        f1.write(pagesource1)
    driver.back() # 回退到后一步
    pagesource2 = driver.page_source
    with open("soure2.text",mode="w",encoding="utf-8") as f2:
        f2.write(pagesource2)
    time.sleep(2)
    driver.get_screenshot_as_file(path + "/new.png")  # 这里是相对路径的话，截图会失败。
    driver.save_screenshot(path + "/new2.png")

    # 获取设备方向
    print(driver.orientation)
    # driver.orientation = "LANDSCAPE"

    # 获取定位
    location = driver.location
    print(location)

    # driver.set_location(116.397128, 39.916527)

    # with open("new.png",mode="w",encoding="utf-8") as f:
    #     f.write(img)
    # driver.swipe()


if __name__ == "__main__":
    test_session()