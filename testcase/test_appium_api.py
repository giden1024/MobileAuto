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
from appium.webdriver.extensions.android.power import Power
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common import utils
from driver.Appium import Appium
from lxml import etree
a = Appium
a.init_driver()
driver = a.get_driver()
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']

base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


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

    # 获取页面资源并且存储在某个位置
    pagesource1 = driver.page_source
    with open("soure1.text",mode="w",encoding="utf-8") as f1:
        f1.write(pagesource1)

    # 获取会话的capabilities
    print(driver.session)
    time.sleep(2)

    # 用手势下滑
    my_swipe(driver)
    # my_scroll(driver)

    # 获取元素，点击进入下一页
    driver.find_elements(By.ID,"home_item_goods_img_iv")[1].click()

    # 获取页面资源并且存储在某个位置，这个是点击元素进入的元素详情页面
    pagesource2 = driver.page_source
    with open("soure1.text",mode="w",encoding="utf-8") as f2:
        f1.write(pagesource2)

    # 隐式等待5秒
    driver.implicitly_wait(5)

    # 获取截图
    driver.get_screenshot_as_file(path + "/new.png")  # 这里是相对路径的话，截图会失败。
    driver.save_screenshot(path + "/new2.png")

    # 获取设备方向，默认为竖屏方向
    print("当前设备方向：%s" % driver.orientation)

    # 设置设备方向为横屏方向
    # driver.orientation = "LANDSCAPE"

    # 获取定位
    location = driver.location
    print("当前定位：%r" % location)

    # 日志类型
    log_types = driver.log_types
    print("日志类型是:%r" % log_types)

    # 获取设置数据
    setting = driver.get_settings()
    print(setting)

    # 回退到后一步
    driver.back()


def test_device():
    # # 获取当前的activity
    # curr_activity = driver.current_activity
    # print("当前activity是%s"%curr_activity)
    #
    # curr_package = driver.current_package
    # print("当前package是%s"%curr_package)
    #
    # # 启动另一个activity,海狸逛逛生产包
    # driver.start_activity("com.chinaredstar.shop", ".ui.home.MainActivity")
    #
    # # 获取当前的activity
    # curr_activity = driver.current_activity
    # print("当前activity是%s"%curr_activity)
    #
    # curr_package = driver.current_package
    # print("当前package是%s"%curr_package)
    #
    # # 切换到uat环境的package
    # driver.start_activity("com.chinaredstar.shop.uat", "com.chinaredstar.shop.ui.home.MainActivity")
    #
    # driver.terminate_app("com.chinaredstar.shop.uat")
    # driver.close_app()

    # 将应用放到后台
    # driver.background_app(10)

    # 根据当前的capabilities重新启动应用
    # driver.launch_app()

    # driver.is_app_installed("com.chinaredstar.shop.uat")

    # 将应用从当前运行的设备上移除
    # driver.remove_app("com.chinaredstar.shop.uat")

    # 根据对应地址的apk文件安装该应用
    # driver.install_app(base_path + "/file/apk/uat.apk")

    # 重启app，测试是否保留数据
    close_toast()
    print(driver.session)
    # test_login()
    driver.reset()
    print(driver.session)

    # 获取app状态
    print(driver.query_app_state("com.chinaredstar.shop.uat"))

    # 获取app字符串的值
    driver.app_strings("en")


def test_interactions():
    # # 手机摇动
    # driver.shake()

    # 手机锁定
    driver.lock()

    # 判断手机是否锁定
    print("------------------")
    print("手机是否锁定：%r"%driver.is_locked())

    # 手机解锁
    driver.unlock()

    # 设置剪切板内容
    driver.set_clipboard_text("从client设置剪切板内容")

    # 获取剪切板内容
    print(driver.get_clipboard_text())

    # # 设置手机模拟电池数据
    # driver.set_power_ac(Power.AC_ON)
    # driver.set_power_capacity(50)

    # 文件操作相关
    driver.pull_file("/sdcard/DCIM/new.txt")
    # driver.push_file("")

def test_element():
    pass

def test_context():
    pass



def test_web():
    pass


def test_login():
    driver.find_elements_by_id("nav_iv_icon")[4].click()
    time.sleep(3)
    driver.find_element_by_id("my_login_state_out_tv").click()
    driver.find_element_by_id("login_phone_et").send_keys("18721705015")
    driver.find_element_by_id("login_btn").click()
    smscode_msg = driver.find_element_by_id("tip_content_tv").text
    smscode = utils.get_code(smscode_msg)
    driver.find_element_by_id("tip_dtn").click()
    for x in smscode:
        driver.press_keycode(utils.get_press_key(x))


def close_toast():
    try:
        time.sleep(10)
        ele = driver.find_element("activity_close_iv")
        ele.click()
    except NoSuchElementException as e:
        print("无法找到元素")


def is_exist_01(ele):
    try:
        driver.find_element(*ele)
        return False
    except NoSuchElementException as e:
        return True


if __name__ == "__main__":
    test_interactions()

