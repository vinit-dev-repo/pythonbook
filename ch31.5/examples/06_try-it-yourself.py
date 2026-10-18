from inspect import getattr_static

# 1
class Show:
    def gathered_fields(self):
        return sorted(self.__dict__.items())

    def __repr__(self):
        fields = ", ".join(f"{key}={value!r}" for key, value in self.gathered_fields())
        return f"{type(self).__name__}({fields})"

class Big(Show):
    def __init__(self, size):
        self.size = size

print(Big(3))

# 2
class Box:
    size = 1

    def grow(self):
        self.size += 1

class Wrap:
    def __init__(self, target):
        self.target = target

    def __getattr__(self, name):
        return getattr(self.target, name)

box = Box()
wrap = Wrap(box)
wrap.size = 0
wrap.grow()
print(wrap.size, box.size)

# 3
class Sensor:
    @property
    def reading(self):
        print("getter runs")
        return 42

sensor = Sensor()
print(type(getattr_static(sensor, "reading")).__name__)
print(sensor.reading)
