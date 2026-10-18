class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # stored with a leading underscore

    @property
    def balance(self):
        return self._balance

acc = BankAccount("Asha", 100)
print(acc.balance)   # looks like an attribute, but a method ran
