import math

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if type(new_balance) not in (int, float):
            raise TypeError("Balance must be an int or float, not bool")
        if isinstance(new_balance, float) and not math.isfinite(new_balance):
            raise ValueError("Balance must be finite")
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = new_balance

    @balance.deleter
    def balance(self):
        print(f"Closing out {self.owner}'s balance and resetting to 0")
        self._balance = 0

acc = BankAccount("Asha", 500)
del acc.balance
print(acc.balance)
