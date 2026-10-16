import sys
import threading

previous_interval = sys.getswitchinterval()
sys.setswitchinterval(1e-6)     # request frequent switches, without promising timing

balance = 0
lock = threading.Lock()

def read_balance():
    return balance

def write_balance(new_value):
    global balance
    balance = new_value

def deposit_many():
    for _ in range(200_000):
        with lock:              # protect all three steps with the same lock
            current = read_balance()
            write_balance(current + 1)

t1 = threading.Thread(target=deposit_many)
t2 = threading.Thread(target=deposit_many)
try:
    t1.start(); t2.start()
    t1.join(); t2.join()
finally:
    sys.setswitchinterval(previous_interval)

print(balance)
