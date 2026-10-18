# 1
class Swimmer:
    def move(self):
        return "swims"

class Walker:
    def move(self):
        return "walks"

class Beaver(Swimmer, Walker):
    pass

class Otter(Walker, Swimmer):
    pass

print(Beaver().move(), Otter().move())           # swims walks
print([cls.__name__ for cls in Beaver.__mro__])  # ['Beaver', 'Swimmer', 'Walker', 'object']

# 2
class NameTagMixin:
    def name_tag(self):
        return f"[{self.name}]"

class Worker(NameTagMixin):
    def __init__(self, name):
        self.name = name

print(Worker("Asha").name_tag())                 # [Asha]

# 3
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)
print(hasattr(point, "__dict__"))                # False
try:
    point.z = 3
except AttributeError as error:
    print(type(error).__name__)                  # AttributeError
