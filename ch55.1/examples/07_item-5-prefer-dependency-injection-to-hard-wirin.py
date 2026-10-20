class OrderGood:
    def __init__(self, db):
        self._db = db          # injected — the caller decides what "db" actually is

    def place(self, item):
        self._db.append(item)
        return len(self._db)

fake_db = []                    # a test passes in exactly this — no real database needed
o2 = OrderGood(fake_db)
print(o2.place("book"))
print(fake_db)
