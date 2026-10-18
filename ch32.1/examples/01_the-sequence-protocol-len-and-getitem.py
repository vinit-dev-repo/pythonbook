class Shelf:
    def __init__(self, books):
        self._books = books

    def __len__(self):
        return len(self._books)

    def __getitem__(self, index):
        return self._books[index]

shelf = Shelf(["Dune", "Emma", "It"])

print(len(shelf))          # len() works
print(shelf[0])            # indexing works
for book in shelf:         # for-loop works!
    print(book)
print("Emma" in shelf)     # in works!
print(list(shelf))         # list() works!
