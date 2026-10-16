class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

acc = BankAccount("Asha", 100)
print(acc.owner)
print(acc.balance)
