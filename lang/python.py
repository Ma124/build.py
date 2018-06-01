import build
import py_compile


class Language(build.Language):
    extensions = ['py']
    out_extension = 'pyc'
    is_text = True
    line_comment = '#'

    def build(self, inp, out):
        py_compile.compile(inp, out)
