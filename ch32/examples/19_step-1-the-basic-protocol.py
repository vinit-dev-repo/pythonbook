class Fibonacci:
    """A sequence of the first `count` Fibonacci numbers."""

    def __init__(self, count):
        self._count = count
        self._values = self._build(count)

    @staticmethod
    def _build(count):
        if type(count) is not int:
            raise TypeError("count must be a built-in int")
        if count < 0:
            raise ValueError("count must be nonnegative")
        values = []
        a, b = 0, 1
        for _ in range(count):
            values.append(a)
            a, b = b, a + b
        return values

    def __len__(self):
        return self._count

    def __getitem__(self, index):
        return self._values[index]

fib = Fibonacci(8)
print(len(fib))
print(fib[5])
for n in fib:
    print(n, end=" ")
