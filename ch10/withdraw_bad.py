# withdraw_bad.py
def withdraw(balance, amount):
    assert amount > 0, f"amount must be positive, got {amount}"
    return balance - amount

print(withdraw(100, 30))

try:
    withdraw(100, -5)
except AssertionError as e:
    print("AssertionError:", e)
