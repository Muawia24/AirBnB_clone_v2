#!/usr/bin/python3
# Fabric script that deletes out-of-date archives, using the function do_clean
from fabric.api import *
import os


env.hosts = ['54.172.71.51', '18.204.5.46']


def do_clean(number=0):
    """
    Delete all unnecessary archives except the recent one
    """

    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))

    for archive in range(number):
        archives.pop()

    with lcd("versions"):
        for archive in archives:
            local("rm ./{}".format(archive))
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [archive for archive in archives if "web_static" in archive]

        for archive in range(number):
            archives.pop()
        for arc in archives:
            run("rm -rf ./{}".format(arc))
