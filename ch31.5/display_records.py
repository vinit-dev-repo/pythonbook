# display_records.py
def auto_repr(cls):
    def __repr__(self):
        fields = ", ".join(f"{key}={value!r}" for key, value in self.__dict__.items())
        return f"{cls.__name__}({fields})"
    cls.__repr__ = __repr__
    return cls

class AttrDisplay:
    def gathered_fields(self):
        return sorted(self.__dict__.items())

    def __repr__(self):
        fields = ", ".join(f"{key}={value!r}" for key, value in self.gathered_fields())
        return f"{type(self).__name__}({fields})"

class HardcodedClient:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"HardcodedClient(name={self.name!r}, level={self.level!r})"

@auto_repr
class DecoratedClient:
    def __init__(self, name):
        self.name = name

class PremiumDecorated(DecoratedClient):
    pass

class Client(AttrDisplay):
    def __init__(self, name, level):
        self.name = name
        self.level = level

class PriorityClient(Client):
    def __init__(self, name, level, priority):
        super().__init__(name, level)
        self.priority = priority

    def gathered_fields(self):
        own_fields = super().gathered_fields()
        return [("kind", "priority")] + own_fields

class InheritedClient(Client):
    region = "north"

    @property
    def label(self):
        return self.name.upper()

class SlottedClient:
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    hardcoded = HardcodedClient("Ada", 2)
    decorated = PremiumDecorated("Lin")
    priority = PriorityClient("Mina", 3, "high")
    print(hardcoded)
    print(decorated)
    print(priority)
    inherited = InheritedClient("Noor", 1)
    print("own fields:", inherited.gathered_fields())
    print("property/inherited in own fields:", "label" in inherited.__dict__, "region" in inherited.__dict__)
    print("slots has dictionary:", hasattr(SlottedClient("Kai"), "__dict__"))
    priority.gathered_fields = "shadowed helper"
    try:
        print(repr(priority))
    except TypeError as error:
        print("helper collision:", type(error).__name__)
