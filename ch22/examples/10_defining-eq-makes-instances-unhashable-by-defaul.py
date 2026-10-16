class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

m = Money(50)
try:
    print({m})
except TypeError as e:
    print(f"TypeError: {e}")
