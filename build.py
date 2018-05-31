#!/usr/bin/python3

import argparse
import util.dynamic


class Config:
    pass


args = None
cfg = None


def main(n=__name__):
    if n != '__main__':
        return
    global args, cfg
    par = argparse.ArgumentParser()
    par.add_argument('-f', '--file',     action='store',      default='build',            help='The build configuration')
    par.add_argument('-o', '--out',      action='store',      default='out',              help='The output directory')
    par.add_argument('-p', '--preserve', action='store_true', default=True,               help='Whether the directory structure should be preserved')
    par.add_argument('task',             action='store',      default='build', nargs='?', help='The task that should be called')
    par.add_argument('args',             action='store',                       nargs='*', help='The arguments for TASK')
    args = par.parse_args()

    cfg = Config()
    util.dynamic.load(args.file, cfg)


main()
