from collections.abc import MutableSequence

class FibonacciABC(MutableSequence):
    def __init__(self, values):
        self._values = list(values)
    def __len__(self):
        return len(self._values)
    def __getitem__(self, index):
        return self._values[index]
    def __setitem__(self, index, value):
        self._values[index] = value
    def __delitem__(self, index):
        del self._values[index]
    def insert(self, index, value):     # the ONE extra method MutableSequence needs
        self._values.insert(index, value)

fib = FibonacciABC([0, 1, 1, 2, 3, 5])
fib.append(8)              # free -- built from insert()
fib.extend([13, 21])       # free -- built from insert()
fib.remove(1)               # free -- removes the FIRST matching value
print(fib._values)
print(2 in fib)              # free -- __contains__
print(list(reversed(fib)))  # free -- __reversed__
