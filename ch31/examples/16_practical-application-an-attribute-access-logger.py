class Logged:
    def __init__(self, **fields):
        for key, value in fields.items():
            setattr(self, key, value)   # goes THROUGH __setattr__ below, on purpose

    def __getattribute__(self, name):
        value = object.__getattribute__(self, name)
        if not name.startswith("__"):
            print(f"GET {name} -> {value!r}")
        return value

    def __setattr__(self, name, value):
        print(f"SET {name} = {value!r}")
        object.__setattr__(self, name, value)

user = Logged(name="Vinit", age=30)
print(user.name)
user.age = 31
