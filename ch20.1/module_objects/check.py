# module_objects/check.py
from types import ModuleType
from collections import namedtuple
import sys

def double(value):
    return value * 2

Point = namedtuple("Point", "x y")
demo = ModuleType("demo", "A module made in memory.")
demo.answer = 21
demo.double = double
demo.Point = Point
print(demo.__name__, demo.answer)
print(demo.double(demo.answer))
print(demo.Point(2, 3))
print(demo.double.__globals__ is globals())
print(demo.double.__globals__ is demo.__dict__)
print(hasattr(demo, "__file__"))
print("demo" in sys.modules)
