settings = {"theme": None}
for name in ("theme", "missing"):
    try:
        value = settings[name]
    except KeyError:
        print(name, "is absent")
    else:
        print(name, "has value", repr(value))
