class OrderBad:
    def __init__(self):
        self._db = []          # creates its own in-memory storage

    def place(self, item):
        self._db.append(item)
        return len(self._db)

o = OrderBad()
print(o.place("book"))
