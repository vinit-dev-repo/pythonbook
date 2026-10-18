# lifecycle_model.py
print("module starts")

def mark(cls):
    print("decorate", cls.__name__)
    cls.kind = "decorated"
    return cls

class TraceMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print("prepare", name)
        return {}

    def __new__(mcs, name, bases, namespace, **kwargs):
        print("new begins", name)
        cls = super().__new__(mcs, name, bases, namespace, **kwargs)
        cls.declared_fields = tuple(
            key for key, value in namespace.items() if isinstance(value, NamedField)
        )
        print("new returns", name)
        return cls

    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace)
        cls.kind = "meta " + name
        print("meta init", name)

    def __call__(cls, *args, **kwargs):
        print("instance call", cls.__name__)
        return super().__call__(*args, **kwargs)

class Parent:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print("parent hook", cls.__name__)

class NamedField:
    def __set_name__(self, owner, name):
        self.name = name
        print("name field", owner.__name__, name)

    def __get__(self, instance, owner=None):
        return self if instance is None else self.name

@mark
class Parcel(Parent, metaclass=TraceMeta):
    print("body Parcel")
    code = NamedField()
    region = NamedField()

    class Note:
        print("nested body Note")

    def __init__(self):
        print("instance init", type(self).__name__)

    def report(self):
        return self.kind

class Child(Parcel):
    print("body Child")
    kind = "child body value"

print("module ready")
if __name__ == "__main__":
    print("main guard")
    print(Parcel().report())
    print(Child().report())
