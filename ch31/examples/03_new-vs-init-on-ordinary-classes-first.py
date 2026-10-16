class Traceable:
    def __new__(cls, *args, **kwargs):
        print(f"__new__: building a {cls.__name__}")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print(f"__init__: setting up {name}")
        self.name = name

t = Traceable("Widget")
