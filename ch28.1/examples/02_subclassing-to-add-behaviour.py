from collections import namedtuple

class OpenPoint(namedtuple("OpenPoint", "x y")):
    pass

class ClosedPoint(namedtuple("ClosedPoint", "x y")):
    __slots__ = ()

open_point = OpenPoint(3, 4)
try:
    open_point.x = 9
except AttributeError as error:
    print("field replacement:", type(error).__name__)

open_point.label = "origin"
print("open extra:", open_point.label)

closed_point = ClosedPoint(3, 4)
try:
    closed_point.label = "origin"
except AttributeError as error:
    print("closed extra:", type(error).__name__)
