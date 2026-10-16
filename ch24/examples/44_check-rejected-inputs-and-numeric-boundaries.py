for opening in (True, -1, float("nan"), float("inf"), "10"):
    try:
        Account("Mira", "Das", "Rejected", opening)
    except ValueError:
        print("Opening rejected:", repr(opening))
try:
    Account("Mira", "Das", "")
except ValueError:
    print("Empty identifier rejected")
for method_name in ("deposit", "withdraw"):
    for amount in (True, 0, -1, float("nan"), float("inf"), "1"):
        trial = Account("Mira", "Das", "Trial", 10)
        before = (trial.balance, trial.ledger)
        try:
            getattr(trial, method_name)(amount)
        except ValueError:
            print(method_name, repr(amount), "unchanged:", before == (trial.balance, trial.ledger))
trial = Account("Mira", "Das", "Flag", 10)
before = (trial.balance, trial.ledger, trial.is_overdraft_allowed)
try:
    trial.is_overdraft_allowed = 1
except ValueError:
    print("Non-Boolean flag rejected:", before == (trial.balance, trial.ledger, trial.is_overdraft_allowed))
large = Account("Mira", "Das", "Large", 1e308)
before = (large.balance, large.ledger)
try:
    large.deposit(1e308)
except ValueError:
    print("Infinite candidate rejected:", before == (large.balance, large.ledger))
huge = Account("Mira", "Das", "Huge", 10 ** 400)
before = (huge.balance, huge.ledger)
try:
    huge.deposit(0.5)
except OverflowError:
    print("Mixed arithmetic rejected:", before == (huge.balance, huge.ledger))
rounded = Account("Mira", "Das", "Rounded", 1e20)
rounded.deposit(1.0)
print("Float rounding:", rounded.balance == 1e20, rounded.ledger[-1][1])
