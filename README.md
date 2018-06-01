# build.py

build.py is a simple build system written in python.

Just create a `build.py` with the following content:

```python
#!/usr/bin/python3
import build

build.main(__name__)


class Config(build.Config):
  # Put your options here
  # Defaults:
  # Default task
  default = 'build'
  # Languages to build (lang/<lang>.py)
  languages = []
  # Default output directory
  out = 'out'
  # Whether to preserve output paths (src/dir/file.py -> out/dir/file.py or out/file.py)
  preserve_paths = True
  # Enable builtin tasks (build etc.)
  builtins = True

# Or remove the class above and put your options here
```

Then call `./build.py -h`  
usage: `build.py [-h] [-f FILE] [-o OUT] [task] [args [args ...]]`

***positional arguments***:

| Option | Description                    |
|--------|--------------------------------|
| task   | The task that should be called |
| args   | The arguments for TASK         |

***optional arguments***:

| Short   | Long        | Description                     |
|-----------|---------------|---------------------------------|
| `-h`      | `--help`      | Show this help message and exit |
| `-f FILE` | `--file FILE` | The build configuration         |
| `-o OUT`  | `--out OUT`   | The output directory            |
