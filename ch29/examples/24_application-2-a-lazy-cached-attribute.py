class LazyProperty:
    """Computes a value once, on first read, then caches it."""
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"  (computing {self.name} ...)")
        value = self.func(instance)
        instance.__dict__[self.name] = value   # shadow the class descriptor for this instance
        return value

    def __call__(self, func):
        self.func = func
        return self


class Report:
    def __init__(self, numbers):
        self.numbers = numbers

    @LazyProperty()
    def total(self):
        return sum(self.numbers)


r = Report([10, 20, 30, 40])
print("First read:")
print(r.total)
print("Second read:")
print(r.total)
