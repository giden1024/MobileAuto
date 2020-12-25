#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/11/17 16:37
@desc:
"""

import logging,os,datetime


def log():
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    date_fill_name = datetime.date.today().__format__("%Y%m%d")
    log_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + "/file/log/")

    # 创建一个logger
    logger = logging.getLogger("myloger")
    logger.setLevel(logging.DEBUG)

    # # 创建handler
    # all_handler = handlers.TimedRotatingFileHandler(filename="../file/log/"+"all.log")
    all_handler = logging.FileHandler(filename=log_path + "/" + date_fill_name + "all.log",encoding="utf-8")
    all_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))


    # 创建error_handler
    error_handler = logging.FileHandler(filename=log_path + "/" + date_fill_name + "error.log",encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[%(lineno)d] - %(message)s"))

    # logger添加handler
    logger.addHandler(all_handler)
    logger.addHandler(error_handler)
    print(date_fill_name)
    return logger


if __name__ == "__main__":
    l = log()
    l.error("new error")
    l.info("new infomation")


