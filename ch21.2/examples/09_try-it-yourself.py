# 1
class Book:
    library_name = "City Library"

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

b1 = Book("Dune", 412)
b2 = Book("Emma", 250)
print(b1.library_name, b2.library_name)                      # City Library City Library

# 2
b1.library_name = "Home"
print(Book.library_name, b1.library_name, b2.library_name)   # City Library Home City Library
del b1.library_name
print(b1.library_name)                                       # City Library

# 3 and 4
class Basket:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def count(self):
        return len(self.items)

first = Basket("first")
second = Basket("second")
first.add("tea")
print(first.items, second.items)                             # ['tea'] []
print(first.count(), Basket.count(first))                    # 1 1

# 5
bound = first.add

def shout_add(self, item):
    self.items.append(item.upper())

Basket.add = shout_add
bound("x")
first.add("y")
print(first.items)                                           # ['tea', 'x', 'Y']
