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

    def exsit_container(self, image):
        for image in self.list_images():
            if image_tag in image.tags:
                LOG.info(f"{image_tag} is already running")
                return True
        return False

    def run(self, image_tag, backend=True):
        if not exsit_container(images_tag):
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

docker_client = DockerClient()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    docker_client.run("mysql:5.7.19")

    print(docker_client.list_container())

    docker_client.stop("mysql:5.7.19")

