class StackUntyped:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

s = StackUntyped()
s.push(1)
s.push("oops")   # a type checker has no way to know this shouldn't be allowed
print(s.pop())
