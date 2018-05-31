def process(lang, inp, out):
    print(inp, '=>', out)
    with open(inp, 'rb') as inp:
        with open(out, 'wb') as out:
            out.write(inp.read())
