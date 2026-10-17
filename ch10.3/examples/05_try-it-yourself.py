# 1
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Not enough balance")
    return balance - amount

print(withdraw(100, 40))    # 60

# 2
def risky():
    try:
        return 1 / 0
    except ZeroDivisionError:
        print("logging the problem")
        raise            # re-raises the same ZeroDivisionError

# 3
import traceback

try:
    1 / 0
except ZeroDivisionError:
    print(traceback.format_exc().strip())

print("still running")
