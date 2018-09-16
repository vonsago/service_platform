#!/usr/bin/env python
# coding=utf-8
'''
> File Name: instance.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:52:52 2018
'''

from flask import g, request
from app.docker_client.docker_ops import docker_client as docker

def update_instance_status(image_tag):
    docker.exsit_container(image_tag)


def instance_create(instance_id):
    request_data = request.get_json()
    image = request_data.get("image")
    ports = request_data.get("ports")
    volumes = reuest_data.get("volumes")
    container = docker.run(image, ports=ports, volumes=volumes)
    if not container:
        return {"get container error"}, 500
    status = container.status 
    short_id = container.short_id

    return {"status": status, "short_id": short_id}, 201

def instance_get(instance_id):
    return {}, 200
