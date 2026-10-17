# withdraw_checked.py
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    return balance - amount

print(withdraw(100, 30))
try:
    withdraw(100, -5)
except ValueError as error:
    print("ValueError:", error)
