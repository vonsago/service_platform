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
    #ports = {"3306/tcp": 3306}
    form = CreateInstanceForm()
    s = form.validate_on_submit()
    if request.method == 'POST' and form.validate_on_submit():
        image = form.data.get("image")
        ports = {"3306/tcp": form.data.get("ports")}
        volumes = form.data.get("volumes").split(",")
        container = docker.run(image, ports=ports, volumes=volumes)

        flash('You have successfully create {}'
              .format(escape(form.image.data)))

        return redirect(url_for('dashboard.dashboard'))
    return render_template('create_instance.html', form=form)

def instance_get(instance_id):
    return {}, 200
