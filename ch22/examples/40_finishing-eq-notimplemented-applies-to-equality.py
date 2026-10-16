from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.amount < other.amount
        return NotImplemented

m = Money(50)
try:
    print(m < 100)
except TypeError as e:
    print(f"TypeError: {e}")
