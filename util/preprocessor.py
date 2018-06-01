import re
import build


def _txt_process(lang, inp, out):
    with open(inp) as f:
        txt = f.read()
    if lang.line_comment is not None:
        txt = re.sub('((?<=[\n\r])|^)(\s*)' + re.escape(lang.line_comment + '&') + '(.*?)((?=[\n\r])|$)', _smpl_txt_repl, txt)
    with open(out, 'w') as f:
        f.write(txt)


def _smpl_txt_repl(m):
    globals()['indent'] = m.group(2)
    s = eval('str(' + m.group(3) + ')\n', {
        'cfg': build.cfg,
        'indent': m.group(2),
        'include': include
    })
    globals().pop('indent')
    return s


def process(lang, inp, out):
    # print(inp, '=>', out)
    if lang.is_text:
        _txt_process(lang, inp, out)
    else:
        with open(inp, 'rb') as inp:
            with open(out, 'wb') as out:
                out.write(inp.read())


def include(file, indent_aware=True):
    i = globals().get('indent', None)
    with open(file) as f:
        if not indent_aware or i is None or i == '':
            return f.read()
        ls = f.read()
    out = ''
    ls = ls.splitlines(True)
    for l in ls:
        out += i + l
    return out
