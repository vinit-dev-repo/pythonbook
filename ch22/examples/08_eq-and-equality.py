class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

m1 = Money(50)
m2 = Money(50)
m3 = Money(100)
print(m1 == m2)
print(m1 == m3)
