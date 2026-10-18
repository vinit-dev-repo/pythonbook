from dataclasses import dataclass, field
from typing import NamedTuple


# 1
class BookHint(NamedTuple):
    title: str
    author: str
    year: int


b3 = BookHint("Dune", "Frank Herbert", 1965)
print(b3)


# 2
@dataclass
class Book:
    title: str
    author: str
    year: int


b = Book("Dune", "Frank Herbert", 1965)
b.year = 2021
print(b)


# 3
@dataclass
class Cart:
    title: str
    items: list[str] = field(default_factory=list)


first = Cart("Monday")
second = Cart("Tuesday")
first.items.append("pen")
print(first.items, second.items, first.items is second.items)
