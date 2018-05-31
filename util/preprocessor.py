import re


def _txt_process(lang, inp, out):
    with open(inp) as f:
        txt = f.read()
    if lang.line_comment is not None:
        txt = re.sub('(?<=[\n\r])' + re.escape(lang.line_comment + '&') + '(.*?)' + '(?=[\n\r])', lambda m: "# " + m.group(1), txt) # TODO fix (?<=[\n\r]) at start of file
    with open(out, 'w') as f:
        f.write(txt)


def process(lang, inp, out):
    print(inp, '=>', out)
    if lang.is_text:
        _txt_process(lang, inp, out)
    else:
        with open(inp, 'rb') as inp:
            with open(out, 'wb') as out:
                out.write(inp.read())
