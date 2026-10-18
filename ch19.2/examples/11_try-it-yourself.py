from collections import namedtuple

# 1
Book = namedtuple("Book", "title author year")
b = Book("Dune", "Frank Herbert", 1965)
print(b)
print(b.author)                       # Frank Herbert

# 2
b2 = b._replace(year=2021)            # e.g. a reprint edition
print(b2)                             # year=2021
print(b)                              # original still year=1965

# 3
emma = Book._make(["Emma", "Jane Austen", 1815])
print(Book._fields)                   # ('title', 'author', 'year')
print(emma._asdict())                 # {'title': 'Emma', 'author': 'Jane Austen', 'year': 1815}

# 4
Record = namedtuple("Record", "name scores")
first = Record("Ana", [85])
second = first._replace(name="Bea")
second.scores.append(90)
print(first)                          # Record(name='Ana', scores=[85, 90])
print(second)                         # Record(name='Bea', scores=[85, 90])
print(first.scores is second.scores)  # True
