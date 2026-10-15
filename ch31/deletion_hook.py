# deletion_hook.py
class DeletionProbe:
    __slots__ = ("label",)

    def __init__(self):
        self.label = "draft"

    def __delattr__(self, name):
        print("delete", name)
        object.__delattr__(self, name)


sample = DeletionProbe()
del sample.label
print("still present:", hasattr(sample, "label"))
try:
    delattr(sample, "label")
except AttributeError:
    print("already absent")
