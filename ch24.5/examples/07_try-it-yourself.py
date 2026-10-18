class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"balance {balance}, requested {amount}")
        self.balance = balance
        self.amount = amount

class Wallet:
    def __init__(self, opening):
        self._balance = opening
        self._ledger = [opening]

    @property
    def balance(self):
        return self._balance

    @property
    def ledger(self):
        return tuple(self._ledger)

    @staticmethod
    def _check(amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError(f"invalid amount: {amount!r}")

    def deposit(self, amount):
        self._check(amount)
        self._balance += amount
        self._ledger.append(amount)

    def withdraw(self, amount):
        self._check(amount)
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        self._ledger.append(-amount)

# 1
wallet = Wallet(100)
try:
    wallet.withdraw(250)
except InsufficientFundsError as error:
    print(error.balance, error.amount)         # 100 250
print(wallet.balance, wallet.ledger)           # 100 (100,)

# 2
old = wallet.ledger
wallet.deposit(25)
print(len(old), len(wallet.ledger))            # 1 2

# 3
try:
    wallet.deposit(True)
except ValueError as error:
    print(error)                               # invalid amount: True
print(wallet.balance, len(wallet.ledger))      # 125 2
