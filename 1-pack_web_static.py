#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """pack"""
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    ruta = "web_static_{}.tgz".format(time)
    local('mkdir -p versions')
    local('tar -czvf versions/{:s} web_static/'.format(ruta))
