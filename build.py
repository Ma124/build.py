#!/usr/bin/python3

import argparse
import os.path
import util.dynamic
import util.builtins
import util.io


class Language:
    extensions = None
    out_extension = None
    is_text = None
    line_comment = None

    def build(self, inp, out):
        # print(inp, '->', out)
        with open(inp, 'rb') as inp:
            with open(out, 'wb') as out:
                out.write(inp.read())


class Config:
    default = 'build'
    out = 'out'
    languages = []
    builtins = True
    preserve_paths = True

    def build(self):
        pass


cfg = Config()
langs = dict()


def main(n, f=None):
    global cfg, langs
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

    util.dynamic.load(args.file, cfg)

    if args.out is not None:
        cfg.out = args.out

    if args.task is None:
        args.task = cfg.default

    for lang in cfg.languages:
        l = Language()
        util.dynamic.load(os.path.join('lang', lang + '.py'), l)
        for ext in l.extensions:
            langs[util.fmt_ext(ext)] = l

    util.io.mkdir(cfg.out)

    if util.dynamic.iscallable(cfg, args.task):
        util.builtins.pre(args.task, *args.args)
        getattr(cfg, args.task).__call__(cfg, *args.args)
    else:
        print("No task named " + args.task + "available.")


main(__name__)
