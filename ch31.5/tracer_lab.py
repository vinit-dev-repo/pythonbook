# tracer_lab.py
def Tracer(target_class):
    class Wrapped:
        def __init__(self, *args, **kwargs):
            self._target = target_class(*args, **kwargs)
            self.lookups = 0

        def __getattr__(self, name):
            self.lookups += 1
            return getattr(self._target, name)
    return Wrapped

class Counter:
    def __init__(self, value):
        self.value = value

    def add(self, amount):
        self.value += amount       # internal target read/write bypass Wrapped
        return self.value

    def fail(self):
        raise ValueError("target failed")

TracedCounter = Tracer(Counter)
if __name__ == "__main__":
    first = TracedCounter(1)
    second = TracedCounter(value=10)
    print(first.add(2))
    print(second.add(5))
    saved = first.add
    print("before saved calls:", first.lookups)
    print(saved(0))
    print(saved(0))
    print("after saved calls:", first.lookups)
    try:
        first.fail()
    except ValueError as error:
        print("target error:", error)
    print("independent:", first._target.value, second._target.value)
    print("lookups:", first.lookups, second.lookups)
    print("wrapper type:", isinstance(first, Counter))
    print("target type:", isinstance(first._target, Counter))
