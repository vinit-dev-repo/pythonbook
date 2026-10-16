from typing import NamedTuple
# 1
class BookHint(NamedTuple):
    title: str
    author: str
    year: int

b3 = BookHint("Dune", "Frank Herbert", 1965)
print(b3)
