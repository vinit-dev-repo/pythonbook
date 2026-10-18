book_tuple = ("Dune", 412)
book_dict = {"title": "Dune", "pages": 412}

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_thick(self):
        return self.pages > 400

book = Book("Dune", 412)
print(book_tuple[0], book_dict["title"], book.title)
print(book.is_thick())
