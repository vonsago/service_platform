#!/usr/bin/env python
# coding=utf-8
'''
> File Name: docker_ops.py
> Author: vassago
> Mail: f811194414@gmail.com
> Created Time: 二  8/28 10:08:15 2018
'''
import docker
import logging

LOG = logging.getLogger(__name__)

class DockerClient():
    def __init__(self):
        try:
            self.client = docker.from_env()
        except Exception as e:
            LOG.info("docker service is not available")

    def pull_images(self, images):
        images = [self.client.images.pull(im) for im in images]
        LOG.info(f"pull images: {images} succeed")
        return images

    def list_containers(self):
        return self.client.containers.list()

    def list_images(self):
        return self.client.images.list()

    def run(self, image_tag, backend=True):
        exsit_container = False
        for image in self.list_images():
            if image_tag in image.tags:
                exsit_container = True
                LOG.info(f"{image_tag} is already running")
                break
        if not exsit_container:
            self.pull_images([image_tag])

        if backend:
            self.client.containers.run(image_tag, detach=True)
            LOG.info(f"container: {image_tag} is running in backend")

    def stop(self, image_tag, stop_all = False):
        for container in self.list_containers():
            if stop_all:
                container.stop()
                LOG.info("stop all of containers")
            elif image_tag in container.image.tags:
                container.stop()
                LOG.info(f"stop {image_tag} success")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    docker = DockerClient()

    docker.run("mysql:5.7.19")

    docker.stop("mysql:5.7.19")

