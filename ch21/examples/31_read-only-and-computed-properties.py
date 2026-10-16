import math

class BankAccount:
    interest_rate = 0.02   # 2% per year - shared by every account

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

    @property
    def interest_earned(self):
        candidate = self.balance * self.interest_rate
        if not math.isfinite(candidate):
            raise ValueError("Interest must be finite")
        return round(candidate, 2)

acc = BankAccount("Asha", 1000)
print(acc.interest_earned)
acc.balance = 2000
print(acc.interest_earned)
