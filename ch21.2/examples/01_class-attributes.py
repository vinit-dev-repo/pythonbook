class BankAccount:
    bank_name = "Community Bank"   # class attribute - shared by everyone

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

acc1 = BankAccount("Asha", 100)
acc2 = BankAccount("Rahul", 50)
print(acc1.bank_name)
print(acc2.bank_name)
print(BankAccount.bank_name)
