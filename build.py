#!/usr/bin/python3

import argparse
import util.dynamic


class Config:
    default = 'build'

    out = 'out'

    def build(self):
        pass


cfg = None


def main(n, f=None):
    """
    build.main(__name__, __file__)

    :param n: __name__
    :param f: __file__
    """

    if n != '__main__':
        return
    global cfg
    par = argparse.ArgumentParser()
    par.add_argument('-f', '--file',   action='store', default='build',           help='The build configuration')
    par.add_argument('-o', '--out',    action='store',                            help='The output directory')
    par.add_argument('task',           action='store',                 nargs='?', help='The task that should be called')
    par.add_argument('args',           action='store',                 nargs='*', help='The arguments for TASK')
    args = par.parse_args()

    if f is not None:
        args.file = f

    cfg = Config()
    util.dynamic.load(args.file, cfg)

    if args.out is not None:
        cfg.out = args.out

    if args.task is None:
        args.task = cfg.default

    if util.dynamic.iscallable(cfg, args.task):
        getattr(cfg, args.task).__call__(cfg, *args.args)
    else:
        print("No task " + args.task)


main(__name__)
