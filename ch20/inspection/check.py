# inspection/check.py
import sys
from types import ModuleType
import labels

name = "shout"
cached = sys.modules["labels"]
print(labels.shout is labels.__dict__[name] is getattr(cached, name))
print(getattr(labels, name)("hello"))
print(labels.__doc__)
print(sorted(key for key in labels.__dict__ if not key.startswith("__")))
print(hasattr(labels, "__file__"), hasattr(ModuleType("memory"), "__file__"))
try:
    getattr(labels, "missing")
except AttributeError:
    print("missing attribute")
