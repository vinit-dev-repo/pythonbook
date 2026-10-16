class Fibonacci:
    def __init__(self, values):
        self._values = list(values)

    @classmethod
    def first(cls, count):
        if type(count) is not int:
            raise TypeError("count must be a built-in int")
        if count < 0:
            raise ValueError("count must be nonnegative")
        values = []
        a, b = 0, 1
        for _ in range(count):
            values.append(a)
            a, b = b, a + b
        return cls(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Fibonacci(self._values[index])
        return self._values[index]

    def __repr__(self):
        return f"Fibonacci({self._values})"

    def __add__(self, other):
        return Fibonacci(self._values + list(other))

    def __iadd__(self, other):
        self._values += list(other)
        return self

    def __mul__(self, times):
        return Fibonacci(self._values * times)

    # --- mutable sequence methods ---

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            self._values[index] = list(value)   # slice assignment needs an iterable
        else:
            self._values[index] = value

    def __delitem__(self, index):
        del self._values[index]

    def append(self, value):
        self._values.append(value)

    def insert(self, index, value):
        self._values.insert(index, value)


fib = Fibonacci.first(6)
print("before:", fib)

fib[0] = 99              # __setitem__ with a single index
print("after fib[0] = 99:", fib)

fib[1:3] = [100, 200, 300]   # __setitem__ with a slice -- can change length!
print("after fib[1:3] = [100, 200, 300]:", fib)

del fib[0]                # __delitem__
print("after del fib[0]:", fib)

fib.append(777)
print("after append(777):", fib)

fib.insert(0, -1)
print("after insert(0, -1):", fib)
