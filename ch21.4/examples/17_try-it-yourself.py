# 1
class Book:
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

    @pages.deleter                     # 4
    def pages(self):
        print("Resetting pages to 0")
        self._pages = 0

    @property                          # 3
    def reading_hours(self):
        return self.pages / 40

# 2
book = Book("Dune", 412)
try:
    book.pages = -10
except ValueError as error:
    print(error)                       # Pages cannot be negative
print(book.pages)                      # 412

# 3
print(book.reading_hours)              # 10.3
try:
    book.reading_hours = 5
except AttributeError as error:
    print(type(error).__name__)        # AttributeError

# 4
del book.pages                         # Resetting pages to 0
print(book.pages)                      # 0

# 5
class CachedSquare:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print("calculating")
            self._area = self._side ** 2
        return self._area

square = CachedSquare(3)
print(square.area)                     # calculating, then 9
print(square.area)                     # 9, from the cache
square.side = 4
print(square.area)                     # calculating, then 16
