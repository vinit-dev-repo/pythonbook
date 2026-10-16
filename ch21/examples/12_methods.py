class BankAccount:
    bank_name = "Community Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

acc = BankAccount("Asha", 100)
acc.deposit(50)
acc.withdraw(20)
print(acc.balance)
