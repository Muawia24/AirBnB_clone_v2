#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function
do_pack.
"""
from fabric.api import *
from datetime import datetime

def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    local("sudo mkdir -p versions")

    time = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = "versions/web_static_{}.tgz".format(time)
    gen_files = local("sudo tar -cvzf {} web_static".format(archive_path))

    if gen_files.succeeded:
        return archive_path
    else:
        return None
