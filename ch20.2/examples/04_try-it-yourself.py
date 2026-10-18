# 1
import sys
print(sys.path[0])
# On most setups this is the folder containing the script you ran:
# it normally comes first in sys.path, unless -P or -I omits it.
# Built-in and frozen modules are handled before the path-based finder.

# 2
# plain.py
PUBLIC = "public"
_internal = "internal"

# check.py
from plain import *
print("PUBLIC" in globals(), "_internal" in globals())   # True False
from plain import _internal
print(_internal)                                          # internal

# 3
import importlib

name = "math"                                  # could come from a configuration file
module = importlib.import_module(name)
print(module.pi)                               # 3.141592653589793

# 4
# store.py
items = ["start"]

# client.py
import store
from store import items

items.append("shared")
print(store.items)                             # ['start', 'shared']
items = ["caller"]
print(store.items)                             # ['start', 'shared']
