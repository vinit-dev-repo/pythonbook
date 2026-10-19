# shape_result_lab.py
def location(path):
    return "root" + "".join(f"[{key!r}]" for key in path)

def check_shape(data, template, path=()):
    if type(template) is dict:
        if type(data) is not dict:
            return False, f"{location(path)}: expected dict, found {type(data).__name__}"
        missing = sorted(template.keys() - data.keys(), key=repr)
        extra = sorted(data.keys() - template.keys(), key=repr)
        if missing or extra:
            return False, f"{location(path)}: missing={missing!r}; extra={extra!r}"
        for key, child_template in template.items():
            ok, message = check_shape(data[key], child_template, path + (key,))
            if not ok:
                return False, message
        return True, ""
    if type(data) is not template:
        return False, f"{location(path)}: expected {template.__name__}, found {type(data).__name__}"
    return True, ""

template = {"batch": int, "station": {"name": str, "enabled": bool}}
good = {"station": {"enabled": True, "name": "north"}, "batch": 8}
missing = {"batch": 8, "station": {"name": "north", "note": "check"}}
wrong_type = {"batch": True, "station": {"name": "north", "enabled": True}}
for candidate in (good, missing, wrong_type):
    ok, message = check_shape(candidate, template)
    print("valid:", ok)
    if not ok:
        print(message)
