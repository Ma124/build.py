============
  build.py
============

build.py is a simple build system written in python.

Just create a ``build.py`` with the following content::

  #!/usr/bin/python3
  import build

  build.main(__name__)


  class Config(build.Config):
    # Put your options here

  # Or remove the class above and put your options here

Then you can call ``./build.py``

usage: ``build.py [-h] [-f FILE] [-o OUT] [task] [args [args ...]]``

***positional arguments***:
+------+--------------------------------+
| task | The task that should be called |
+------+--------------------------------+
| args | The arguments for TASK         |
+------+--------------------------------+

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  The build configuration
  -o OUT, --out OUT     The output directory
