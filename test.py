#!/usr/bin/python3

import build

build.main(__name__, __file__)


class Config(build.Config):
    languages = ['python']
    preserve_paths = True
