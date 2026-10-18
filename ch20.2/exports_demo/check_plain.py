# exports_demo/check_plain.py
from plain import *
print(PUBLIC)
print("_internal" in globals())
from plain import _internal
print(_internal)
