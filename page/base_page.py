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

from driver.Appium import Appium
from appium.webdriver import WebElement
from common import utils
from common.log import log

class BasePage:

    def __init__(self):
        Appium.init_driver()
        self.driver = Appium.get_driver()
        self.driver.implicitly_wait(10)  # 隐式等待10秒

    def yaml_parse(self,path,module_name):
        with open(path,encoding="utf-8") as f:
            yaml_log = yaml.load(f,Loader=yaml.FullLoader)
            return self.parse(yaml_log[module_name])

    def parse(self,actions):
        ele: WebElement = None
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

    def find(self,args,locater=None) -> WebElement:
        ele = None
        if isinstance(args,tuple):
            ele = self.driver.find_element(*args)
        else:
            ele = self.driver.find_element(args,locater)
        return ele

    def finds(self,args,locater=None,item=0):
        """

        :param args:
        :param locater:
        :param item: list中第几项
        :return:
        """
        ele = None
        if isinstance(args,tuple):
            ele = self.driver.find_elements(*args)[item]
        else:
            ele = self.driver.find_elements(args,locater)[item]
        ele.click()
        return ele

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


if __name__ == "__main__":
    b = BasePage()
    b.find((By.ID,"name"))