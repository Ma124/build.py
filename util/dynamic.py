import importlib.util


def load(f, i):
    spec = importlib.util.spec_from_file_location('module', f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    t = type(i)

    if hasattr(mod, t.__name__) and issubclass(getattr(mod, t.__name__), t):
        mod = mod.Config

    for attr in dir(mod):
        if not attr.startswith('_'):
            setattr(i, attr, getattr(mod, attr))
