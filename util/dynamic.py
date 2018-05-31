import importlib.util


def load(f, i):
    spec = importlib.util.spec_from_file_location('module', f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    t = type(i)

    if hasattr(mod, t.__name__) and issubclass(getattr(mod, t.__name__), t):
        mod = getattr(mod, t.__name__)  # could return getattr(mod, t.__name__) but setting attrs in i is for the IDEs

    for attr in dir(mod):
        if not attr.startswith('_'):
            setattr(i, attr, getattr(mod, attr))


def iscallable(o, k):
    f = getattr(o, k, None)
    if f is None:
        return False
    if not hasattr(f, '__call__'):
        return False
    return True
