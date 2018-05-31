import util.builder


def pre(task, *args):
    if task == 'build':
        util.builder.pre_build_task(*args)
