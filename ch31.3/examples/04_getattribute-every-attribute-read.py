class Watched:
    def __init__(self, value):
        self.value = value

    def __getattribute__(self, name):
        print(f"reading '{name}'")
        return object.__getattribute__(self, name)

w = Watched(42)
result = w.value
print(result)
