class Money:
    def __init__(self, amount):
        self.amount = amount

    def __format__(self, spec):
        return f"${self.amount:{spec}}"

price = Money(19.5)
print(f"{price:.2f}")
