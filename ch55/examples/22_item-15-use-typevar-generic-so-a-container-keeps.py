from typing import Generic, TypeVar

T = TypeVar("T")

class StackTyped(Generic[T]):
    def __init__(self):
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

ints: StackTyped[int] = StackTyped()
ints.push(1)
ints.push(2)
print(ints.pop())
