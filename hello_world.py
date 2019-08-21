#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 10:00
# @Author  : Andrew.chu
# @Site    : Schindler
# @File    : hello_world.py
# @Software: PyCharm
"""
Description:

"""
from datetime import datetime
with open("output/test.txt", "a") as f:
    f.write("\nhello "+datetime.now().strftime("%H:%M:%S"))