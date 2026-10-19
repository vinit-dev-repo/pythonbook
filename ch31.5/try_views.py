# try_views.py
import importlib
from inspection_tools import DefaultView, FieldsView, InheritedView


def build(kind, *args, **kwargs):
    return kind(*args, **kwargs)


class Device:
    region = "west"

    def __init__(self, label, *, count=1):
        self.label = label
        self.count = count

    def ping(self):
        return self.label

    @property
    def caption(self):
        return self.label.upper()

    @property
    def offline(self):
        raise RuntimeError("no connection")


def demonstrate(view):
    class Screen(Device, view):
        pass

    value = build(Screen, "dock", count=2)
    print(value)
    return value


if __name__ == "__main__":
    for policy in (FieldsView, InheritedView):
        demonstrate(policy)

    module = importlib.import_module("inspection_tools")
    chosen = getattr(module, "DefaultView")
    print("default alias:", chosen is DefaultView)
    item = demonstrate(chosen)
    before = vars(item).copy()
    print("repeat stable:", str(item) == str(item))
    print("state unchanged:", vars(item) == before)
    print("special names included:", "__str__ = <function __str__>" in item.class_report(True))
    print("bound:", item.ping.__self__ is item)
    print("function:", Device.ping.__name__)
