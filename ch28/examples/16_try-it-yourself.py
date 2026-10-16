# 2
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int

b = Book("Dune", "Frank Herbert", 1965)
b.year = 2021
print(b)
