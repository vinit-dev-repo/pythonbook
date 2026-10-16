class BadMoney:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return id(self)   # BROKEN: ignores amount, uses identity instead

a = BadMoney(50)
b = BadMoney(50)
print(a == b)
prices = {a: "fifty"}
print(b in prices)
