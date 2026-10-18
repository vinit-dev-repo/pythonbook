class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

print(callable(BankAccount))
acc2 = BankAccount("Rahul", 0)
print(type(acc2))
