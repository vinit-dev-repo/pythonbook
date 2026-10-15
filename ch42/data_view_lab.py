# data_view_lab.py
import json
import keyword

class DataView:
    __slots__ = ("_data",)

    def __new__(cls, value):
        if type(value) is dict:
            return super().__new__(cls)
        if type(value) is list:
            return tuple(cls(item) for item in value)
        if value is None or type(value) in (str, int, float, bool):
            return value
        raise TypeError("expected a built-in JSON value")

    def __init__(self, mapping):
        if any(type(key) is not str for key in mapping):
            raise TypeError("object keys must be strings")
        object.__setattr__(self, "_data", dict(mapping))

    def __getitem__(self, key):
        return type(self)(self._data[key])

    def __getattr__(self, name):
        if not name.isidentifier() or keyword.iskeyword(name) or name.startswith("_"):
            raise AttributeError(name)
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name) from None

    def keys(self):
        return tuple(self._data)

    def __dir__(self):
        public = [name for name in self._data if name.isidentifier()
                  and not keyword.iskeyword(name) and not name.startswith("_")]
        return sorted(set(object.__dir__(self)) | set(public))

    def __setattr__(self, name, value):
        raise AttributeError("view attributes are read-only")

    def __delattr__(self, name):
        raise AttributeError("view attributes are read-only")

raw = json.loads('{"records": [{"label": "draft"}], "keys": "stored text", '
                 '"class": 5, "class_": 6, "2nd": "second"}')
view = DataView(raw)
saved_record = view.records[0]
print(saved_record.label)
print(callable(view.keys), view["keys"])
print(view["class"], view.class_, view["2nd"])
print("records" in dir(view), hasattr(view, "missing"))
raw["records"][0]["label"] = "revised"
print(saved_record.label, view.records[0].label)
try:
    view.records = ()
except AttributeError:
    print("ordinary write refused")
print(DataView([1, None, True]))
