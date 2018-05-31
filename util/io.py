import os
import uuid
import atexit
import shutil


def walk(r):
    for root, dirs, files in os.walk(r):
        for dir in dirs:
            walk(os.path.join(root, dir))
        for file in files:
            yield os.path.join(root, file)


def mkdir(f, autodel=False):
    if not os.path.exists(f):
        os.mkdir(f, mode=0o770)
    if autodel:
        atexit.register(shutil.rmtree, f)


def tmp():
    return os.path.join('.tmp', uuid.uuid4().hex)


mkdir('.tmp', autodel=True)
