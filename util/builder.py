import os.path
import util.io
import util.preprocessor
# import util.postprocessor
import build as main


def out_name(inp, lang):
    n, ext = os.path.splitext(inp)
    if main.cfg.preserve_paths:
        return os.path.join(main.cfg.out, os.path.relpath(n) + util.fmt_ext(lang.out_extension))
    else:
        return os.path.join(main.cfg.out, os.path.basename(n) + util.fmt_ext(lang.out_extension))


def build(inp, out=None):
    n, ext = os.path.splitext(inp)
    if ext not in main.langs:
        return
    lang = main.langs[ext]
    if out is None:
        out = out_name(inp, lang)

    util.io.mkdir(os.path.dirname(out))

    tmp = util.io.tmp()
    util.preprocessor.process(lang, inp, tmp)
    # tmp2 = util.io.tmp()
    lang.build(lang, tmp, out)
    # lang.build(lang, tmp, tmp2)
    # util.postprocessor.process(lang, tmp2, out)


def pre_build_task(*args):
    for file in util.io.walk(os.getcwd()):
        build(file)

