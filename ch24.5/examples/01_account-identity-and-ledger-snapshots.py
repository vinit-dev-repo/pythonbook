from datetime import datetime, timezone
from math import isfinite

def _number_text(value):
    # Internal callers supply a validated built-in int or float.
    try:
        return str(value)
    except ValueError:
        return "<integer exceeds decimal display limit>"

def finite_number(value):
    # bool and numeric subclasses are outside this exercise's input domain.
    return type(value) is int or (type(value) is float and isfinite(value))

class Account:
    def __init__(self, first_name, last_name, account_number,
                 initial_balance=0, is_overdraft_allowed=False):
        for label, value in (("first_name", first_name),
                             ("last_name", last_name),
                             ("account_number", account_number)):
            if type(value) is not str or not value:
                raise ValueError(f"{label} must be a nonempty string")
        if not finite_number(initial_balance) or initial_balance < 0:
            raise ValueError("Opening balance must be finite and nonnegative")
        self._first_name = first_name
        self._last_name = last_name
        self._account_number = account_number
        self._balance = initial_balance
        self.is_overdraft_allowed = is_overdraft_allowed
        self._ledger = [(datetime.now(timezone.utc), 0, initial_balance)]

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def ledger(self):
        return tuple(self._ledger)

    @property
    def is_overdraft_allowed(self):
        return self._is_overdraft_allowed

    @is_overdraft_allowed.setter
    def is_overdraft_allowed(self, value):
        if type(value) is not bool:
            raise ValueError("Overdraft flag must be True or False")
        if not value and self.balance < 0:
            raise ValueError("Restore a nonnegative balance before disabling overdraft")
        self._is_overdraft_allowed = value

    def __str__(self):
        return f"{self.account_number}: {_number_text(self.balance)}"

    def __repr__(self):
        return (f"Account({self.account_number!r}, "
                f"owner={(self.first_name, self.last_name)!r}, balance={_number_text(self.balance)}, "
                f"overdraft={self.is_overdraft_allowed!r}, "
                f"entries={len(self._ledger)})")

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.account_number == other.account_number

    __hash__ = None

account = Account("Mira", "Das", "A-17", 100)
same_number = Account("Other", "Person", "A-17", 500)
print(account.first_name, account.last_name)
print(str(account))
print(repr(account))
print("Equal identifiers:", account == same_number)
print("Same object:", account is same_number)
print("Compared with a string:", account == "A-17")
print("Ledger length:", len(account.ledger))
print("Opening amount and balance:", account.ledger[0][1:])
timestamp = account.ledger[0][0]
print("Aware UTC:", timestamp.tzinfo is not None and timestamp.utcoffset().total_seconds() == 0)
try:
    account.balance = 999
except AttributeError:
    print("Balance has no public setter")
try:
    hash(account)
except TypeError:
    print("Account is unhashable")
