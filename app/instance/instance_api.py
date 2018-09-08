#!/usr/bin/env python
# coding=utf-8
'''
> File Name: instance_api.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:53:13 2018
'''

from flask import Blueprint
from .instance import instance_create, instance_get

instance_management = Blueprint("instance_management", __name__)

instance_management.add_url_rule(
        rule="/v1/instance/<instance_id>",
        view_func=instance_create,
        method=["POST"]
        )

instance_management.add_url_rule(
        rule="/v1/instance/<instance_id>",
        view_func=instance_get,
        method=["GET"]
        )
