#!/usr/bin/env python
# coding=utf-8
'''
> File Name: instance_api.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:53:13 2018
'''

from flask import Blueprint
from .instance import instance_create, list_instances

instance_management = Blueprint("instance_management", __name__)

instance_management.add_url_rule(
        rule="/v1/instance",
        endpoint="create_instance",
        view_func=instance_create,
        methods=["GET", "POST"]
        )

instance_management.add_url_rule(
        rule="/v1/instance_view",
        endpoint="list_instances",
        view_func=list_instances,
        methods=["GET"]
        )
