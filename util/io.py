import os


def walk(r):
    for root, dirs, files in os.walk(r):
        for dir in dirs:
            walk(os.path.join(root, dir))
        for file in files:
            yield os.path.join(root, file)
