# property_factory_lab.py
def bounded_int(storage_name, low, high):
    if type(storage_name) is not str or not storage_name.startswith("_"):
        raise ValueError("use a private backing name")
    if type(low) is not int or type(high) is not int or low > high:
        raise ValueError("expected ordered integer bounds")

    def get_value(instance):
        try:
            return instance.__dict__[storage_name]
        except KeyError:
            raise AttributeError(storage_name) from None

    def set_value(instance, value):
        if type(value) is not int:
            raise TypeError("expected a built-in integer")
        if not low <= value <= high:
            raise ValueError("outside the allowed range")
        instance.__dict__[storage_name] = value

    return property(get_value, set_value,
                    doc=f"Integer from {low} through {high}, inclusive.")

class Batch:
    count = bounded_int("_count", 1, 12)
    priority = bounded_int("_priority", 0, 3)

    def __init__(self, count, priority):
        self.count = count
        self.priority = priority

first = Batch(4, 1)
second = Batch(8, 3)
first.count = 6
print(first.count, first.priority, second.count, second.priority)
try:
    first.priority = 4
except ValueError:
    print("rejected; previous value:", first.priority)
try:
    first.count = True
except TypeError:
    print("Boolean refused")
print(Batch.count.__doc__)
