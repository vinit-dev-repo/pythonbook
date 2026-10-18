class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

print(type(5))
print(type(int))
print((5).bit_length())
print(isinstance(5, int))

acc = BankAccount("Asha", 100)
print(type(acc))
print(isinstance(acc, BankAccount))
