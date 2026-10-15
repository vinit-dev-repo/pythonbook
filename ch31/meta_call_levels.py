# meta_call_levels.py
events = []

class CreationGate(type):
    def __call__(mcs, name, bases, namespace):
        events.append("gate " + name)
        return super().__call__(name, bases, namespace)

class TrackedType(type, metaclass=CreationGate):
    def __new__(mcs, name, bases, namespace):
        events.append("new " + name)
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        events.append("class init " + name)

    def __call__(cls, *args, **kwargs):
        events.append("instance call " + cls.__name__)
        return super().__call__(*args, **kwargs)

class Part(metaclass=TrackedType):
    def __init__(self, label):
        events.append("object init " + label)

print(events)
events.clear()
Part("blue")
print(events)
print(type(Part) is TrackedType, type(TrackedType) is CreationGate)
