class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

m = Money(50)
try:
    print(m == 5)
except AttributeError as e:
    print(f"AttributeError: {e}")
