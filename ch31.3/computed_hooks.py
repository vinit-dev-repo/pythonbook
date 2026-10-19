# computed_hooks.py
class Reading:
    def __init__(self, label, millivolts):
        self.label = label
        self.millivolts = millivolts

    def __setattr__(self, name, value):
        if name == "label":
            if type(value) is not str:
                raise TypeError("label must be text")
            value = value.strip()
            if not value:
                raise ValueError("label cannot be blank")
        elif name == "millivolts":
            if type(value) is not int:
                raise TypeError("millivolts must be a built-in integer")
            if not 0 <= value <= 5000:
                raise ValueError("millivolts must be between 0 and 5000")
        elif name == "volts":
            raise AttributeError("volts is computed")
        object.__setattr__(self, name, value)


class MissingReading(Reading):
    def __getattr__(self, name):
        print("missing:", name)
        if name == "volts":
            return self.millivolts / 1000
        raise AttributeError(name)


class EveryReading(Reading):
    def __getattribute__(self, name):
        print("ordinary read:", name)
        if name == "volts":
            return object.__getattribute__(self, "millivolts") / 1000
        return object.__getattribute__(self, name)


for kind in (MissingReading, EveryReading):
    print(kind.__name__)
    first = kind("  north  ", 1250)
    second = kind("south", 2000)
    print(first.label, first.volts, second.volts)
    try:
        first.millivolts = -1
    except ValueError:
        print("Rejected before storage")
    print(first.volts)
    try:
        first.volts = 9
    except AttributeError:
        print("Computed write rejected")
