#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/11/17 16:37
@desc:
"""

import logging


def log():
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # 创建一个logger
    logger = logging.getLogger("myloger")
    logger.setLevel(logging.DEBUG)

    # # 创建handler
    # all_handler = handlers.TimedRotatingFileHandler(filename="../file/log/"+"all.log")
    all_handler = logging.FileHandler(filename="../file/log/"+"all.log",encoding="utf-8")
    all_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))


    # 创建error_handler
    error_handler = logging.FileHandler(filename="../file/log/"+"error.log",encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d] - %(message)s"))

    # logger添加handler
    logger.addHandler(all_handler)
    logger.addHandler(error_handler)

    return logger


if __name__ == "__main__":
    l = log()
    l.info("new thing")

