class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        message = f"Cannot withdraw {amount}: only {balance} available"
        super().__init__(message)
        self.balance = balance
        self.amount = amount

try:
    raise InsufficientFundsError(balance=100, amount=500)
except InsufficientFundsError as e:
    print(e)
    print(e.balance, e.amount)
