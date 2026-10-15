# class_lookup.py
class CatalogMeta(type):
    label = "metaclass label"

    @property
    def status(cls):
        return cls.__dict__.get("_status", "new")

    @status.setter
    def status(cls, value):
        if type(value) is not str:
            raise TypeError("status must be text")
        cls._status = value

    def describe(cls):
        return "class " + cls.__name__

    def __getitem__(cls, index):
        return cls.entries[index]

class CatalogBase:
    label = "base label"
    status = "instance default"

class Catalog(CatalogBase, metaclass=CatalogMeta):
    entries = ("east", "west")

    @classmethod
    def class_name(cls):
        return cls.__name__

item = Catalog()
print(Catalog.label, item.label)
print(Catalog.status, item.status)
Catalog.status = "ready"
print(Catalog.status, item.status, "status" in vars(Catalog))
print(Catalog.describe(), item.class_name())
try:
    item.describe()
except AttributeError:
    print("metaclass method absent on instance")
print(Catalog[1])
try:
    item[1]
except TypeError:
    print("instance has no indexing protocol")
