# manual_namespace/check.py
import sys
from loader import prepare, run_registered

name = "lesson_memory"
source = '''
"""A module whose body is supplied as source text."""
import sys
print("registered during execution:", sys.modules[__name__].__dict__ is globals())
base = 20
def total(value):
    return base + value
'''
code = prepare(source, name)
print("cached after compile:", name in sys.modules)
module = run_registered(name, code)
caller = {}
caller["lesson"] = module
print(caller["lesson"].total(22))
print(module.total.__globals__ is module.__dict__)
print(module.__doc__)
module.base = 30
print(module.total(22))
del caller["lesson"]
print("caller/cache:", "lesson" in caller, name in sys.modules)
del sys.modules[name]
print("retained reference:", module.total(22))
