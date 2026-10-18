# slot_boundaries.py
class SlotParent:
    __slots__ = ("label",)

class SlotChild(SlotParent):
    __slots__ = ("count", "__dict__")

item = SlotChild()
print(item.__slots__)
print("label" in dir(item), hasattr(item, "label"))
setattr(item, "label", "draft")
item.count = 4
item.note = "extra"
print(getattr(item, "label"), item.count, vars(item))
try:
    class SlotConflict:
        __slots__ = ("label",)
        label = "default"
except ValueError:
    print("slot default rejected")
