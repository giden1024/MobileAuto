#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/11/19 16:31
@desc:
"""

from page.base_page import BasePage


class Search(BasePage):
    MAIN_FILEPATH = "../../config/action_yaml/customer/"
    def get_shop_list_info(self):
        pass

    def main(self):
        file = self.MAIN_FILEPATH + "main.yaml"
        self.yaml_parse(file, "FirstView")
        self.yaml_parse(file, "GetLoginTitle")

    def search(self):
        file = file = self.MAIN_FILEPATH + "search.yaml"
        return self.yaml_parse(file,"SearchShop")


class ChooseCity():
    pass


if __name__ == "__main__":
    S = Search()
    print(S.search())

