class Fibonacci:
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
        return self._values[index]     # index can be an int OR a slice — list handles both

    def __repr__(self):
        return f"Fibonacci({self._count})"

fib = Fibonacci(10)
print(fib[2:6])
print(fib)
