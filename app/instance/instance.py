#!/usr/bin/env python
# coding=utf-8
'''
> File Name: instance.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:52:52 2018
'''

from flask import g, request
from app.docker import docker_client as docker

def update_instance_status(image_tag):
    docker.exsit_container(image_tag)


def instance_create(instance_id):
    request_data = request.get_json()
    image = request_data.get("image")
    docker.run(image)
    status = docker.get_image_tag_status(image)

    return {"status": status}, 201

def instance_get(instance_id):
    return {}, 200
