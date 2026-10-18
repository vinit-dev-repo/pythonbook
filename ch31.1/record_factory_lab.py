# record_factory_lab.py
import keyword

def record_class(class_name, field_names):
    def valid_name(name):
        return (
            type(name) is str and name.isidentifier()
            and not keyword.iskeyword(name) and not name.startswith("_")
        )

    if not valid_name(class_name):
        raise ValueError("invalid class name")
    if isinstance(field_names, str):
        field_names = field_names.replace(",", " ").split()
    names = tuple(field_names)
    if not names or not all(valid_name(name) for name in names):
        raise ValueError("fields need public identifier names")
    if len(set(names)) != len(names):
        raise ValueError("field names must be unique")

    def initialize(self, *args, **kwargs):
        if len(args) > len(names):
            raise TypeError("too many positional values")
        values = dict(zip(names, args))
        if values.keys() & kwargs.keys():
            raise TypeError("field supplied twice")
        if kwargs.keys() - set(names):
            raise TypeError("unknown field")
        values.update(kwargs)
        if len(values) != len(names):
            raise TypeError("missing field")
        for name in names:
            setattr(self, name, values[name])

    def iterate(self):
        for name in names:
            yield getattr(self, name)

    def represent(self):
        parts = [f"{name}={getattr(self, name)!r}" for name in names]
        return type(self).__name__ + "(" + ", ".join(parts) + ")"

    namespace = {
        "__module__": __name__, "__slots__": names,
        "__init__": initialize, "__iter__": iterate, "__repr__": represent,
    }
    return type(class_name, (object,), namespace)

ShelfRecord = record_class("ShelfRecord", "aisle, quantity")
item = ShelfRecord("east", quantity=4)
print(item)
aisle, quantity = item
print(aisle, quantity)
item.quantity = 6
print(tuple(item))
print(ShelfRecord is record_class("ShelfRecord", ("aisle", "quantity")))
for args, kwargs in [(("east",), {}), (("east", 4), {"quantity": 5}),
                     (("east", 4, 5), {}), ((), {"aisle": "east", "other": 4})]:
    try:
        ShelfRecord(*args, **kwargs)
    except TypeError as error:
        print(error)
