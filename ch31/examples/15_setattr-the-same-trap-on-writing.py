class ReadOnly:
    def __init__(self, value):
        object.__setattr__(self, "value", value)   # bypass our own guard, just this once

    def __setattr__(self, name, value):
        raise AttributeError(f"{name} is read-only, cannot be changed")

r = ReadOnly(10)
print(r.value)

try:
    r.value = 99
except AttributeError as e:
    print(e)
