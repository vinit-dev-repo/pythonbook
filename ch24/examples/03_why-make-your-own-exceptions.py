def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Not enough funds")
    if amount < 0:
        raise ArithmeticError("Amount cannot be negative")
    return balance - amount

# the caller has to know BOTH exact exception types used inside
try:
    withdraw(100, 500)
except (ValueError, ArithmeticError):
    print("Withdrawal failed")
