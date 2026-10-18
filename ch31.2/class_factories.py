# class_factories.py
events = []

def make_class(name, bases, namespace):
    events.append("function: " + name)
    return type(name, bases, namespace)

class ClassFactory:
    def __call__(self, name, bases, namespace):
        events.append("object: " + name)
        return type(name, bases, namespace)

class Note(metaclass=make_class):
    label = "note"

class Tag(metaclass=ClassFactory()):
    label = "tag"

class Child(Note):
    pass

print(events)
print(type(Note) is type, type(Tag) is type, type(Child) is type)
print(Note().label, Tag().label, Child().label)

class LegacySpelling:
    __metaclass__ = make_class

print(type(LegacySpelling) is type)

def return_name(name, bases, namespace):
    return name.lower()

class Summary(metaclass=return_name):
    ignored = 10

print(Summary, type(Summary).__name__)
