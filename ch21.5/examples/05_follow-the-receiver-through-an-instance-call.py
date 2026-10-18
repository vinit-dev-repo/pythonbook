import math

class BankAccount:
    bank_name = "Community Bank"

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

    def deposit(self, amount):
        if type(amount) not in (int, float):
            raise TypeError("Amount must be an int or float, not bool")
        if isinstance(amount, float) and not math.isfinite(amount):
            raise ValueError("Amount must be finite")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        proposed_balance = self.balance + amount
        self.balance = proposed_balance

    def withdraw(self, amount):
        if type(amount) not in (int, float):
            raise TypeError("Amount must be an int or float, not bool")
        if isinstance(amount, float) and not math.isfinite(amount):
            raise ValueError("Amount must be finite")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        proposed_balance = self.balance - amount
        self.balance = proposed_balance

    @classmethod
    def from_string(cls, text):
        # text looks like "Asha,250"
        owner, balance = text.split(",")
        return cls(owner, float(balance))

    @staticmethod
    def is_valid_amount(amount):
        return (type(amount) in (int, float)
                and amount > 0
                and (type(amount) is int or math.isfinite(amount)))

    @classmethod
    def rename_bank(cls, name):
        cls.bank_name = name

first = BankAccount.from_string("Asha,250")
second = BankAccount("Rahul", 100)
print(first.rename_bank("Local Bank"))
print(BankAccount.bank_name, first.bank_name, second.bank_name)
print(first.rename_bank.__self__ is BankAccount)
print(first.deposit.__self__ is first)
print(first.is_valid_amount is BankAccount.is_valid_amount)
try:
    first.deposit(True)
except TypeError as error:
    print(type(error).__name__)
print(first.balance)
