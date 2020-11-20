#!/user/bin/env python
#coding=utf-8
'''
@author: mayuyang
@file: base_page.py
@time: 2020/5/13 13:39
@desc:

'''
import yaml

from driver.Appium import Appium
from appium.webdriver.webelement import WebElement
from common import utils

class BasePage:

    def __init__(self):
        Appium.init_driver()
        self.driver = Appium.get_driver()
        self.driver.implicitly_wait(10)  # 隐式等待10秒

    def yaml_parse(self,path,module_name):
        with open(path,encoding="utf-8") as f:
            yaml_log = yaml.load(f)
            self.parse(yaml_log[module_name])

    def parse(self,actions):
        for action in actions:
            if action["action"] == "find":
                self.find((action['by'],action['locator']))
            elif action["action"] == "write":
                self.write((action['by',action['locator']]),action['value'])
            elif action["action"] == "get_text":
                self.get_text((action['by',action['locator']],action['expression']))
            elif action["action"] == "press_key":
                self.press_key()

    def find(self,locate) -> WebElement:
        """

        :param locate:
        :return: ->
        """
        ele = self.driver.find_element(*locate)
        ele.click()
        return ele

    def find_without_click(self,locate) -> WebElement:
        ele = self.driver.find_element(*locate)
        return ele

    def get_text(self,locate,expression=None):
        text = self.find(*locate).text
        if expression == "get_code":
            return utils.get_code(text)

    def write(self,ele,value):
        ele.send_keys(value)

    def press_key(self,*num):
        for x in num:
            self.driver.press_keycode(utils.get_press_key(x))


