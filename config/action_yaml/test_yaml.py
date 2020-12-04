#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/11/20 15:34
@desc:
"""
import yaml
from common.log import log

with open("test.yaml",encoding="utf-8") as f:
    yaml_log = yaml.load(f)
    log.log().info("test yaml")
    log.log().info(yaml_log)

with open("customer/user.yaml",encoding="utf-8") as f:
    yaml_log = yaml.load(f)
    log.log().info("test user yaml")
    log.log().info(yaml_log)