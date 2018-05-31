import build


class Language(build.Language):
    extensions = ['py']
    out_extension = 'pyc'
    is_text = True
    line_comment = '#'
