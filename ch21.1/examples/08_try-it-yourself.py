# 1
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

b1 = Book("Dune", 412)
b2 = Book("Emma", 250)
print(b1.title, b2.title)          # Dune Emma

# 2
class Dog:
    pass

first = Dog()
second = Dog()
print(first is second)             # False
print(type(first) is Dog)          # True

# 3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Point(1, 2)
b = Point(3, 4)
a.x = 10
print(a.x, b.x)                    # 10 3
