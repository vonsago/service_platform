#!/usr/bin/env python
# coding=utf-8
'''
> File Name: instance.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:52:52 2018
'''

from flask import g, request, flash
from app.docker_client.docker_ops import docker_client as docker
from .forms import CreateInstanceForm

def update_instance_status(image_tag):
    docker.exsit_container(image_tag)


def instance_create(instance_id):
    request_data = request.get_json()
    image = request_data.get("image")
    ports = request_data.get("ports")
    volumes = request_data.get("volumes")
    container = docker.run(image, ports=ports, volumes=volumes)

    form = SignupForm()
    if form.validate_on_submit():
        # We don't have anything fancy in our application, so we are just
        # flashing a message when a user completes the form successfully.
        #
        # Note that the default flashed messages rendering allows HTML, so
        # we need to escape things if we input user values:
        flash('Hello, {}. You have successfully signed up'
              .format(escape(form.name.data)))

        # In a real application, you may wish to avoid this tedious redirect.
        return redirect(url_for('.index'))

def instance_get(instance_id):
    return {}, 200
