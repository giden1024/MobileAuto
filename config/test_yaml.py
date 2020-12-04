#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/11/25 13:51
@desc:
"""

import yaml

file = "data_yaml.yaml"
# with open(file,encoding="utf-8") as f:
#     r = yaml.load(f,Loader=yaml.FullLoader)
#     print(r)

with open(file,mode="w+",encoding="utf-8") as f1:
    s_dict = {"smscode":{"smscode":123456}}
    yaml.dump(s_dict,f1)


