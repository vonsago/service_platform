#!/usr/bin/env python
# coding=utf-8
'''
> File Name: instance.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:52:52 2018
'''

from flask import g, request, flash, render_template, redirect, url_for
from app.docker_client.docker_ops import docker_client as docker
from .forms import CreateInstanceForm
from markupsafe import escape

def update_instance_status(image_tag):
    docker.exsit_container(image_tag)


def instance_create():
    # request_data = request.get_json()
    # image = request_data.get("image")
    # ports = request_data.get("ports")
    # volumes = request_data.get("volumes")
    # container = docker.run(image, ports=ports, volumes=volumes)
    form = CreateInstanceForm()
    s = form.validate_on_submit()
    if request.method == 'POST' and form.validate_on_submit():
        
        #docker.run()

        flash('You have successfully create {}'
              .format(escape(form.image.data)))

        return redirect(url_for('dashboard.dashboard'))
    return render_template('create_instance.html', form=form)

def instance_get(instance_id):
    return {}, 200
