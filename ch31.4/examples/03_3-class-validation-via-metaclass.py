class InterfaceMeta(type):
    required_methods = {"save", "load"}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:
            missing = mcs.required_methods - namespace.keys()
            if missing:
                raise TypeError(f"{name} is missing required methods: {missing}")
        return cls

class Storage(metaclass=InterfaceMeta):
    pass

class FileStorage(Storage):
    def save(self): pass
    def load(self): pass

try:
    class BrokenStorage(Storage):
        def save(self): pass
        # forgot load!
except TypeError as e:
    print(e)
