class Book:
    library_name = "City Library"

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value < 0:
            raise ValueError("Pages cannot be negative")
        self._pages = value

    @classmethod
    def from_line(cls, text):
        title, pages = text.split(",")
        return cls(title, int(pages))

    @staticmethod
    def is_thick(pages):
        return pages > 400

# 1 and 2
b1 = Book("Dune", 412)
b2 = Book("Emma", 250)
print(b1.title, b2.title)
print(b1.library_name, b2.library_name)

# 3 - reject the assignment and keep the old value
try:
    b1.pages = -10
except ValueError as error:
    print(error)
print(b1.pages)

# 4
b3 = Book.from_line("1984,328")
print(b3.title, b3.pages)

# 5
print(Book.is_thick(412))
print(Book.is_thick(250))
