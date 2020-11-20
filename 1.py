#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/11/18 16:24
@desc:
"""
import re
str1 = "【海狸逛逛E端】验证码: 734856。有效时间5分钟。"
print(re.findall(".*(\d{6})", str1))

number_key = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16}
print(number_key['0'])