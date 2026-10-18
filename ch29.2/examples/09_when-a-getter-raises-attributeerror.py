class Missing:
    def __get__(self, instance, owner):
        raise AttributeError("not ready")

class Demo:
    value = Missing()

    def __getattr__(self, name):
        return f"fallback for {name}"

d = Demo()
print(d.value)
print(getattr(d, "value"))
try:
    print(object.__getattribute__(d, "value"))
except AttributeError as error:
    print(type(error).__name__ + ":", error)
