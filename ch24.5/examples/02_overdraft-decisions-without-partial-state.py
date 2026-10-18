from datetime import datetime, timezone
from math import isfinite


def _number_text(value):
    # Internal callers supply a validated built-in int or float.
    try:
        return str(value)
    except ValueError:
        return "<integer exceeds decimal display limit>"


class OverdraftNotAllowedError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {_number_text(amount)}: "
                         f"only {_number_text(balance)} available")
        self.balance = balance
        self.amount = amount


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

    def deposit(self, amount):
        self._change(amount, withdrawing=False)

    def withdraw(self, amount):
        self._change(amount, withdrawing=True)

    def _change(self, amount, withdrawing):
        if not finite_number(amount) or amount <= 0:
            raise ValueError("Amount must be a positive finite int or float")
        signed_amount = -amount if withdrawing else amount
        # Arithmetic may raise OverflowError. Nothing has changed yet.
        candidate = self.balance + signed_amount
        if not finite_number(candidate):
            raise ValueError("Resulting balance must be finite")
        if candidate < 0 and not self.is_overdraft_allowed:
            raise OverdraftNotAllowedError(self.balance, amount)
        entry = (datetime.now(timezone.utc), signed_amount, candidate)
        self._ledger.append(entry)
        self._balance = candidate

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
