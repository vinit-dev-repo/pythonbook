from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

m1 = Money(50)
m2 = Money(100)
print(m1 < m2)
print(m1 <= m2)
print(m1 > m2)
print(m1 >= m2)
