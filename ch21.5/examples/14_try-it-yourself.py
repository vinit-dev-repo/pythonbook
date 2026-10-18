# 1, 2 and 3
class Book:
    library_name = "City Library"

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    @classmethod
    def from_line(cls, text):
        title, pages = text.split(",")
        return cls(title, int(pages))

    @staticmethod
    def is_thick(pages):
        return pages > 400

    @classmethod
    def rename_library(cls, name):
        cls.library_name = name

b3 = Book.from_line("1984,328")
print(b3.title, b3.pages)                      # 1984 328
print(Book.is_thick(412), Book.is_thick(250))  # True False
b3.rename_library("Town Library")
print(Book.library_name)                       # Town Library

# 4
class Config:
    factor = 10

    def scale(self, n):
        return n * self.factor

print(Config().scale(5))                       # 50

# 5
made = []
for number in (1, 2):
    class Stamp:
        print("class body", number)
    made.append(Stamp)

first = made[0]()
second = made[0]()
third = made[1]()
print(len(made), made[0] is made[1])           # 2 False
