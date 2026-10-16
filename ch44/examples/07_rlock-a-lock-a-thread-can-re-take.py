import threading

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.RLock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def transfer_in_twice(self, amount):
        with self.lock:          # acquired once here...
            self.deposit(amount) # ...and again inside deposit — fine with RLock
            self.deposit(amount)

acc = BankAccount(0)
acc.transfer_in_twice(50)
print(acc.balance)
