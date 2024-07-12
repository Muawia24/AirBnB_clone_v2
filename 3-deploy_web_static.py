#!/usr/bin/python3
"""
Scripts creates and distributes an archive to your web
servers, using the function deploy
"""


from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['54.172.71.51', '18.204.5.46']


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


def do_deploy(archive_path):
    """
    Deploy archive!
    Returns False if the file at the path archive_path does't exist
    """

    if exists(archive_path) is False:
        return False

    file_name = archive_path.split('/')[-1]
    rm_extension = "/data/web_static/releases/" + '{}'\
        .format(file_name.split('.')[0])
    tmp = "/tmp/" + file_name

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(rm_extension))
        run("tar -xzf {} -C {}/".format(tmp, rm_extension))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(rm_extension, rm_extension))
        run("rm -rf {}/web_static".format(rm_extension))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(rm_extension))

        return True
    except:
        return False


def deploy():
    """
    call do_pack(), do_deploy(archive_path)
    """

    arch_path = do_pack()
    if exists(arch_path) is False:
        return False
    full_deploy = do_deploy(arch_path)
    return full_deploy
