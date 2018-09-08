#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午8:57
# @Author  : Vassago
# @File    : dashboard.py
# @Software: PyCharm

from flask import render_template


def show_dashboard():
    return render_template("index.html")