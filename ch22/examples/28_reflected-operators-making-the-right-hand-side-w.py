class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"

    def __add__(self, other):
        if type(self) is not Money or type(other) is not Money:
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("currencies must match")
        return Money(self.amount + other.amount, self.currency)

wallet = [Money(10), Money(20), Money(30)]
try:
    print(sum(wallet))
except TypeError as e:
    print(f"TypeError: {e}")
