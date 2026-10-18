# import_practice_package/myapp/utils/library.py
from .formatting import shout

__all__ = ["label_pair"]

def label_pair(first, second):
    return shout(first) + " / " + shout(second)
