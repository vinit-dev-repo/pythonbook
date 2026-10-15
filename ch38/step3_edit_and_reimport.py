# step3_edit_and_reimport.py
import importlib.util
import os
import pathlib

# Never hard-code the .pyc name: it carries the interpreter version, so
# "greeter.cpython-312.pyc" is wrong the moment you run a different Python.
# cache_from_source() asks the running interpreter where it would put the file.
pyc_path = importlib.util.cache_from_source("greeter.py")
before = pathlib.Path(pyc_path).read_bytes()

pathlib.Path("greeter.py").write_text(
    'print("greeter.py is running its top-level code")\n'
    '\n'
    'def greet(name):\n'
    '    return f"Hello, {name}"\n'
    '\n'
    'def farewell(name):\n'
    '    return f"Goodbye, {name}"\n'
)

import greeter
print(greeter.farewell("Amir"))

after = pathlib.Path(pyc_path).read_bytes()
print("pyc content changed:", after != before)
