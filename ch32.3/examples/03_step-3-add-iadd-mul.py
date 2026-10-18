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

fib = Fibonacci.first(5)
print(fib)
print(fib + [8, 13])       # __add__: makes a NEW Fibonacci
print(fib * 2)              # __mul__: repeats the values

fib += [8, 13]               # __iadd__: grows IN PLACE
print(fib)
