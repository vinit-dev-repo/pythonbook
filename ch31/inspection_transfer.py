# inspection_transfer.py
from collections import UserDict
from namespace_views import FieldsView, InheritedView, TreeView


class Root:
    category = "record"


class Left(Root):
    pass


class Right(Root):
    pass


class Diamond(TreeView, Left, Right):
    pass


item = Diamond()
item.note = "one object"
report = str(item)
assert report.count("Root [seen]") == 1
assert report.count("category = 'record'") == 1
assert vars(item) == {"note": "one object"}
assert str(item) == report
print("shared class shown once:", True)


class OwnSlots(FieldsView):
    __slots__ = ("label",)


class VisibleSlots(InheritedView):
    __slots__ = ("label",)


own = OwnSlots()
visible = VisibleSlots()
own.label = visible.label = "port"
assert not hasattr(own, "__dict__") and not hasattr(visible, "__dict__")
assert "<no instance dictionary>" in str(own)
assert "label = 'port'" in str(visible)
print("slots need a different view:", True)


class LoggedMap(TreeView, UserDict):
    pass


mapping = LoggedMap({"a": 1})
mapping["b"] = 2
large = str(mapping)
assert "UserDict" in large and "MutableMapping" in large
assert dict(mapping) == {"a": 1, "b": 2}
assert str(mapping) == large
print("library mixin keeps mapping behavior:", True)


class ChangingView(InheritedView):
    def __init__(self):
        self.reads = 0

    @property
    def signal(self):
        self.reads += 1
        return self.reads


changing = ChangingView()
str(changing)
assert changing.reads == 1
str(changing)
assert changing.reads == 2
print("property reads can change state:", changing.reads)
