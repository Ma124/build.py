#!/usr/bin/python3

import argparse
import util.dynamic


class Config:
    out = 'out'


cfg = None


def main(n=__name__):
    if n != '__main__':
        return
    global cfg
    par = argparse.ArgumentParser()
    par.add_argument('-f', '--file',   action='store', default='build',           help='The build configuration')
    par.add_argument('-o', '--out',    action='store',                            help='The output directory')
    par.add_argument('task',           action='store',                 nargs='?', help='The task that should be called')
    par.add_argument('args',           action='store',                 nargs='*', help='The arguments for TASK')
    args = par.parse_args()

    cfg = Config()
    util.dynamic.load(args.file, cfg)

    if args.out is not None:
        cfg.out = args.out


main()
