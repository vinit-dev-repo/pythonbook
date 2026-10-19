# shape_exception_lab.py
class ShapeError(Exception):
    pass

class ShapeKeys(ShapeError):
    pass

class ShapeType(ShapeError, TypeError):
    pass

def location(path):
    return "root" + "".join(f"[{key!r}]" for key in path)

def validate_shape(data, template, path=()):
    if type(template) is dict:
        if type(data) is not dict:
            raise ShapeType(f"{location(path)}: expected dict, found {type(data).__name__}")
        missing = sorted(template.keys() - data.keys(), key=repr)
        extra = sorted(data.keys() - template.keys(), key=repr)
        if missing or extra:
            raise ShapeKeys(f"{location(path)}: missing={missing!r}; extra={extra!r}")
        for key, child_template in template.items():
            validate_shape(data[key], child_template, path + (key,))
        return
    if type(data) is not template:
        raise ShapeType(f"{location(path)}: expected {template.__name__}, found {type(data).__name__}")

template = {"batch": int, "station": {"name": str, "enabled": bool}}
good = {"station": {"enabled": True, "name": "north"}, "batch": 8}
missing = {"batch": 8, "station": {"name": "north", "note": "check"}}
wrong_type = {"batch": True, "station": {"name": "north", "enabled": True}}
print(validate_shape(good, template))
for candidate in (missing, wrong_type):
    try:
        validate_shape(candidate, template)
    except ShapeKeys as error:
        print("keys:", error)
    except ShapeType as error:
        print("type:", error)
    except ShapeError as error:
        print("other shape problem:", error)
try:
    validate_shape(wrong_type, template)
except TypeError:
    print("also caught by TypeError")
