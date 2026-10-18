class SlottedBase:
    __slots__ = ("x",)

class OpenChild(SlottedBase):
    pass

class ClosedChild(SlottedBase):
    __slots__ = ()

class ExtraSlottedChild(SlottedBase):
    __slots__ = ("y",)

class HybridChild(SlottedBase):
    __slots__ = ("__dict__",)

class OpenBase:
    pass

class SlottedChildOfOpen(OpenBase):
    __slots__ = ("y",)

for kind in (SlottedBase, OpenChild, ClosedChild, ExtraSlottedChild, SlottedChildOfOpen, HybridChild):
    print(kind.__name__, hasattr(kind(), "__dict__"))
slotted = ClosedChild()
slotted.x = 1
del slotted.x
print(hasattr(slotted, "x"))
slotted.x = 2
SlottedBase.label = "base setting"
print(slotted.x, ClosedChild.label)
open_child = OpenChild()
open_child.x = 1
open_child.note = "extra"
print(open_child.x, vars(open_child))
