class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

acc = BankAccount("Asha", 100)
acc.balance = -500   # nothing stops this!
print(acc.balance)
