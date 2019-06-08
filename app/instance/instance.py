#!/usr/bin/env python
# coding=utf-8
'''
> File Name: instance.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 三  8/29 19:52:52 2018
'''

import json
from flask import jsonify, request, flash, render_template, redirect, url_for, Response
from app.docker_client.docker_ops import DockerClient
from .forms import CreateInstanceForm
from .schema import InstanceSchema
from markupsafe import escape

def update_instance_status(image_tag):
    with DockerClient() as docker:
        docker.exsit_container(image_tag)


def instance_create():
    form = CreateInstanceForm()
    s = form.validate_on_submit()
    if request.method == 'POST' and form.validate_on_submit():
        image = form.data.get("image")
        port = {"3306/tcp": form.data.get("port")}
        volumes = form.data.get("volumes").split(",")
        with DockerClient() as docker:
            container = docker.run(image, ports=port, volumes=volumes)

        flash('You have successfully create {}'
              .format(escape(form.image.data)))

        return redirect(url_for('dashboard.dashboard'))
    return render_template('create_instance.html', form=form)


def instance_create_view():
    instance = request.get_json()
    image = instance.get("image")
    port = {"3306/tcp": instance.get("port")}
    volumes = instance.get("volumes").split(",")
    with DockerClient() as docker:
        container = docker.run(image, ports=port, volumes=volumes)
    return jsonify({}), 200


def list_instances():
    instances = []
    with DockerClient() as docker:
        containers = docker.list_containers()
        for container in containers:
            try:
                instance = {
                    "name": container.name,
                    "short_id": container.short_id,
                    "status":container.status,
                    "prots": json.dumps(container.ports),
                    "image": container.image.tags[0],
                    "created": container.attrs.get("Created")
                }
            except:
                #todo fix
                instance = {
                    "name": 'xxx',
                    "short_id": container.short_id,
                    "status": "xxx",
                    "prots": "xxx",
                    "image": "xxx",
                    "created": "xxx"
                }

            instances.append(instance)
    return jsonify(instances), 200
    #return render_template("list_instances.html", comments=comments)


def stop_instance(instance_id):
    with DockerClient() as docker:
        if instance_id == "Dangerous_All":
            docker.stop("", stop_all=True)
            flash(f"Stop All Instance Success.")
        elif docker.stop(instance_id):
            flash(f"Stop {instance_id} Success.")
        else:
            flash(f"Stop Failed.")
    return jsonify({}), 200


def restart_instance(instance_id):
    with DockerClient() as docker:
        if docker.restart(instance_id):
            flash(f"Restart Instance {instance_id} Success.")
    return jsonify({}), 200
