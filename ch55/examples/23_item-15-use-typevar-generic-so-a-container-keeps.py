class Stack[T]:               # Python 3.12+ generic class syntax — same idea, less boilerplate
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

names: Stack[str] = Stack()
names.push("Ana")
print(names.pop())
