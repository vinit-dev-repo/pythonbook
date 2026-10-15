# rebuild_class.py
class Origin:
    def label(self):
        return "origin"

class Named(Origin):
    def label(self):
        return super().label() + ":named"

namespace = {key: value for key, value in vars(Named).items()
             if key not in {"__dict__", "__weakref__"}}
Copied = type("Copied", Named.__bases__, namespace)
print(Copied is Named, issubclass(Copied, Named))
print(Named().label())
try:
    Copied().label()
except TypeError:
    print("copied method retains the old defining class")

def add_kind(cls):
    cls.kind = "kept"
    return cls

saved = Named
Named = add_kind(Named)
print(Named is saved, Named().label(), Named.kind)
