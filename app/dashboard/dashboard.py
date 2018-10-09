#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/8 下午8:57
# @Author  : Vassago
# @File    : dashboard.py
# @Software: PyCharm

from flask import render_template, flash
from app.docker_client.docker_ops import DockerClient

def show_dashboard():
    with DockerClient() as docker:
        if not docker:
            flash("Error: Docker Service Is Not Available !")
    return render_template("index.html")