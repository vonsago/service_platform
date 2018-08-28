#!/usr/bin/env python
# coding=utf-8
'''
> File Name: docker_ops.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 二  8/28 10:08:15 2018
'''
import docker

class DcokerClient():
    def __init__(self):
        self.client = docker.from_env()

    def pull_images(self, images):
        images = [client.images.pull(im) for im in images]
        return images
