#!/user/bin/env python
#coding=utf-8
'''
@author: mayuyang
@file: base_page.py
@time: 2020/5/13 13:39
@desc:

'''
import yaml
from selenium.webdriver.common.by import By
from common.log import log
from driver.Appium import Appium
from appium.webdriver import WebElement
from common import utils
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self):
        Appium.init_driver()
        self.driver = Appium.get_driver()
        self.driver.implicitly_wait(10)  # 隐式等待10秒
        self.logger = log()


    def find(self,args,locater=None):
        try:
            if isinstance(args,tuple):
                ele = self.driver.find_element(*args)
            else:
                ele = self.driver.find_element(args,locater)
            return ele
        except NoSuchElementException as e:
            self.logger.error(e)
            return False


    def finds(self,args,locater=None,item=0):
        """

        :param args:
        :param locater:
        :param item: list中第几项
        :return:
        """
        if self.find(args,locater):
            if isinstance(args,tuple):
                ele = self.driver.find_elements(*args)[item]
            else:
                ele = self.driver.find_elements(args,locater)[item]
            ele.click()
            return ele
        else:
            return False

    def yaml_parse(self,path,module_name):
        with open(path,encoding="utf-8") as f:
            yaml_log = yaml.load(f,Loader=yaml.FullLoader)
            return self.parse(yaml_log[module_name])

    def parse(self,actions):
        ele: WebElement
        for action in actions:
            if action["action"] == "finds":
                ele = self.finds(action['by',action['locator'],action['item']])
            elif action["by"]:
                ele = self.find(action['by'],action['locator'])
            if action['action']:
                act = action['action']
                if act == "click":
                    self.click(ele)
                if act == "write":
                    self.write(ele,action['value'])
                elif act == "get_text":
                    text = self.get_text(ele)
                    # log.log().info(text)
                    return text
                elif act == "press_key":
                    self.press_key()

    def click(self,ele):
        ele.click()

    def get_text(self,ele,regex=None,save_file=None):
        ele_text = ele.text
        if regex:
            return utils.get_code(ele_text)
        return ele_text

    def write(self,ele,value):
        ele.send_keys(value)

    def press_key(self,*num):
        for x in num:
            self.driver.press_keycode(utils.get_press_key(x))

    def my_swipe(self,start_y=0.25, end_y=0.9, duration=1000):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x1 = int(x * 0.5)
        y1 = int(y * start_y)
        x2 = int(x * 0.5)
        y2 = int(y * end_y)
        self.driver.swipe(x1, y2, x2, y1, duration)

    def scroll_to_ele(self,start_locater,end_locater,duration=1000):
        end_ele = self.find(*end_locater)
        while not end_ele:
            self.my_swipe()
            end_ele = self.find(*end_locater)
            if end_ele:
                break
        start_ele = self.find(*start_locater)
        self.driver.scroll(start_ele,end_ele,duration=duration)


    def close_imageview(self):
        if self.find((By.ID,"activity_close_iv")):
            self.find((By.ID,"activity_close_iv")).click()
        else:
            self.logger.info("没有弹窗")


if __name__ == "__main__":
    b = BasePage()
    # b.find((By.ID,"name"))
    b.close_imageview()
    start_locater = (By.ID,"banner_image")
    b.find(start_locater)
    end_locater = (By.ID,"tv_loading_msg")
    b.find(end_locater)
    # b.my_swipe()
    # end_ele = b.find((By.ID,"home_item_goods_img_iv"))
    # print(end_ele)
    # b.scroll_to_ele(start_locater,end_locater)