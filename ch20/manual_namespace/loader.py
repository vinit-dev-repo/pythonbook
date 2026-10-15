# manual_namespace/loader.py
from types import ModuleType
import sys

def prepare(source, name):
    return compile(source, "<" + name + ">", "exec")

def run_registered(name, code):
    if name in sys.modules:
        raise ValueError("choose a fresh module name")
    module = ModuleType(name)
    sys.modules[name] = module
    try:
        exec(code, module.__dict__)
    except BaseException:
        del sys.modules[name]
        raise
    return module
