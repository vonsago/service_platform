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
        LOG.info("pull images: {} succeed".format(images))
        return images

    def list_containers(self):
        return self.client.containers.list()

    def list_images(self):
        return self.client.images.list()

    def exsit_image(self, image_tag):
        for image in self.list_images():
            if image_tag in image.tags:
                LOG.info("image: {} is already pulled".format(image_tag))
                return True
        return False

    def exsit_container(self, image_tag):
        for container in self.list_containers():
            if image_tag in container.image.tags:
                LOG.info("container: {} is already running".format(image_tag))
                return True
        return False

    def get_image_tag_status(self, image_tag):
        pass

    def get_container(self, image_tag):
        for container in self.list_containers():
            if image_tag in container.tags:
                return container
        return None

    def run(self, image_tag, ports, volumes, backend=True):
        if not self.exsit_image(image_tag):
            self.pull_images([image_tag])

        if self.exsit_container(image_tag):
            return self.get_container(image_tag)

        if backend:
            container = self.client.containers.run(image_tag, ports=ports,
                    volumes=volumes, detach=True)
            LOG.info("container: {} running in backend".format(image_tag))
            return container

    def stop(self, image_tag, stop_all = False):
        for container in self.list_containers():
            if stop_all:
                container.stop()
                LOG.info("stop all of containers")
            elif image_tag in container.image.tags:
                container.stop()
                LOG.info("stop {image_tag} success".format(image_tag))

docker_client = DockerClient()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    s = docker_client.run("mysql:5.7.19", ports={"3306/tcp": 3306},volumes=["mysqldata:/var/lib/mysql"])
    print(s.short_id)

    #print(docker_client.list_containers()[0].status)

    docker_client.stop("mysql:5.7.19")

