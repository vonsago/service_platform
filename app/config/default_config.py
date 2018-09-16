#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午9:22
# @Author  : Vassago
# @File    : default_config.py
# @Software: PyCharm

import os

from app.config.base_config import Base, get_full_path, str2bool, str2int

class DefaultConfig():
    CONFIG_NAME = 'DEFAULT'
    DEBUG = True
    TEMPLATE_DIR = "."
    STATIC_DIR = "."