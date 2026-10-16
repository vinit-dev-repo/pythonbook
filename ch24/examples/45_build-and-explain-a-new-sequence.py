account = Account("Asha", "Rao", "B-42", 20)
old = account.ledger
account.is_overdraft_allowed = True
account.withdraw(35)
print("After withdrawal:", account.balance)
before = (account.balance, account.ledger, account.is_overdraft_allowed)
try:
    account.is_overdraft_allowed = False
except ValueError:
    print("Disable rejected:", before == (account.balance, account.ledger, account.is_overdraft_allowed))
account.deposit(15)
account.is_overdraft_allowed = False
print("Final balance and flag:", account.balance, account.is_overdraft_allowed)
print("Signed entries:", [entry[1:] for entry in account.ledger])
print("Snapshot lengths:", len(old), len(account.ledger))
print("Shared opening entry:", old[0] is account.ledger[0])
