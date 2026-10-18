# type_links.py
print(type(object) is type)
print(type(type) is type)
print(type.__bases__ == (object,))
print(object.__bases__)
print(isinstance(object, type), issubclass(object, type))
