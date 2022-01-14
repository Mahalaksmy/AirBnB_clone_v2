#!/usr/bin/python3

from fabric.api import local
import os.path

env.user = "ubuntu"
env.hosts = ['35.185.98.24', '54.158.48.32']


def do_deploy(archive_path):
    """
    This is a Method that distributes
    an archive to your web servers.
    """
    if os.path.exists(archive_path) is False:
        return False

    basename = path = os.path.basename(archive_path)
    root, ext = os.path.splitext(basename)
    target = '/data/web_static/releases/{}'.format(root)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(target))
        run("sudo tar -xzf /tmp/{} -C {}/".format(path, target))
        run("sudo rm /tmp/{}".format(path))
        run("sudo mv {}/web_static/* {}/".format(target, target))
        run("sudo rm -rf {}/web_static".format(target))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(target))
     
    except Exception as error:
        print(error)
    else:
        return True
