class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

m1 = Money(50)
m2 = Money(50)
print(m1 == m2)
print(hash(m1) == hash(m2))
print(len({m1, m2}))
