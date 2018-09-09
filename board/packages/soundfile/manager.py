import os
from subprocess import call
import os.path
import random

from . import build_path, FILES_PATH


def get_files_names():
    res = []
    for file in os.listdir(FILES_PATH):
        res.append(file)
    return res


def upload(f):
    path = build_path(f.name)
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def play(name):
    path = build_path(name)
    if os.path.exists(path):
        call(["omxplayer", path])


def play_random():
    files = get_files_names()
    name = random.choice(files)
    play(name)


def delete(name):
    path = build_path(name)
    if os.path.exists(path):
        os.remove(path)
