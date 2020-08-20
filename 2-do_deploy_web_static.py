#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
from fabric.api import put, run, env
import os


env.hosts = ["34.75.57.54", "34.74.149.81"]
#env.hosts=['localhost']


def do_deploy(archive_path):
    """deploy"""
    out = os.path.isfile(archive_path)

    if out is not False:
        try:
            put(archive_path, "/tmp/{}".format(archive_path[9:]))

            run("mkdir -p /data/web_static/releases/{}/"
                .format(archive_path[9:-4]))

            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
                .format(archive_path[9:], archive_path[9:-4]))

            run("rm /tmp/{}".format(archive_path[9:]))

            run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/"""
                .format(archive_path[9:-4], archive_path[9:-4]))

            run("rm -rf /data/web_static/releases/{}/web_static"
                .format(archive_path[9:-4]))
            run("rm -rf /data/web_static/current")
            run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
                .format(archive_path[9:-4]))

            print("New version deployed!")

            return True

        except Exception as e:
            return False
    else:
        return False
