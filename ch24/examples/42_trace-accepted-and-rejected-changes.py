account = Account("Mira", "Das", "A-17", 100)
old = account.ledger
account.deposit(25)
print("After deposit:", account.balance)
before = (account.balance, account.ledger)
try:
    account.withdraw(200)
except OverdraftNotAllowedError as error:
    print(type(error).__name__, error.balance, error.amount)
print("Rejected withdrawal unchanged:", before == (account.balance, account.ledger))
account.is_overdraft_allowed = True
account.withdraw(150)
print("Allowed overdraft:", account.balance)
before = (account.balance, account.ledger, account.is_overdraft_allowed)
try:
    account.is_overdraft_allowed = False
except ValueError:
    print("Cannot disable overdraft while negative")
print("Rejected policy change unchanged:", before == (account.balance, account.ledger, account.is_overdraft_allowed))
account.deposit(25)
account.is_overdraft_allowed = False
print("Recovered:", account.balance, account.is_overdraft_allowed)
print("Signed entries:", [entry[1:] for entry in account.ledger])
