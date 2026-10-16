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

    def __radd__(self, other):
        # sum() starts with 0, so the very first call is really 0 + Money(...)
        if type(self) is not Money:
            return NotImplemented
        if type(other) is int and other == 0:
            return self
        return self.__add__(other)

wallet = [Money(10), Money(20), Money(30)]
print(sum(wallet))
