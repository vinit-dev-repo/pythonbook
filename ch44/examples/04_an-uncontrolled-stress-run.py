import sys
import threading

# Request a shorter switching interval; this cannot guarantee a lost update.
previous_interval = sys.getswitchinterval()
sys.setswitchinterval(1e-6)

balance = 0

def read_balance():
    return balance

def write_balance(new_value):
    global balance
    balance = new_value

def deposit_many():
    for _ in range(200_000):
        current = read_balance()      # step 1: READ  the balance
        new_value = current + 1       # step 2: ADD   one pound
        write_balance(new_value)      # step 3: WRITE it back

t1 = threading.Thread(target=deposit_many)
t2 = threading.Thread(target=deposit_many)
try:
    t1.start(); t2.start()
    t1.join(); t2.join()
finally:
    sys.setswitchinterval(previous_interval)

print(f"expected: {2 * 200_000}")
print(f"lost some deposits: {balance < 2 * 200_000}")
