#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午8:58
# @Author  : Vassago
# @File    : dashboard_api.py
# @Software: PyCharm

from flask import Blueprint
from app.dashboard.dashboard import show_dashboard

dashboard_management = Blueprint("dashboard", __name__)

dashboard_management.add_url_rule(
        rule="/",
        view_func=show_dashboard,
        methods=["GET"]
        )