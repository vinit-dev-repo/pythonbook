# account.py
from datetime import datetime, timezone
from itertools import count
from math import isfinite

from account_timezone import TimeZone
from confirmations import format_confirmation, validate_account_id


def utc_now():
    return datetime.now(timezone.utc)


class Account:
    _interest_rate = 0.5
    _counter = count(100)

    def __init__(
        self,
        account_id,
        first_name,
        last_name,
        initial_balance=0,
        preferred_timezone=None,
        *,
        clock=utc_now,
    ):
        self._account_id = validate_account_id(account_id)
        self._first_name = self._validate_name("first_name", first_name)
        self._last_name = self._validate_name("last_name", last_name)
        self._balance = self._validate_nonnegative("initial_balance", initial_balance)
        self._preferred_timezone = TimeZone("UTC") if preferred_timezone is None else self._validate_timezone(preferred_timezone)
        if not callable(clock):
            raise TypeError("clock must be callable")
        self._clock = clock

    @staticmethod
    def _validate_name(name, value):
        if type(value) is not str:
            raise TypeError(f"{name} must be a string")
        value = value.strip()
        if not value:
            raise ValueError(f"{name} must not be blank")
        return value

    @staticmethod
    def _validate_number(name, value):
        if type(value) not in (int, float):
            raise TypeError(f"{name} must be an int or float")
        try:
            number = float(value)
        except OverflowError as error:
            raise ValueError(f"{name} must be representable") from error
        if not isfinite(number):
            raise ValueError(f"{name} must be finite")
        return number

    @classmethod
    def _validate_nonnegative(cls, name, value):
        number = cls._validate_number(name, value)
        if number < 0:
            raise ValueError(f"{name} must not be negative")
        return number

    @staticmethod
    def _validate_timezone(value):
        if type(value) is not TimeZone:
            raise TypeError("preferred_timezone must be a TimeZone")
        return value

    @property
    def account_id(self):
        return self._account_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = self._validate_name("first_name", value)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = self._validate_name("last_name", value)

    @property
    def preferred_timezone(self):
        return self._preferred_timezone

    @preferred_timezone.setter
    def preferred_timezone(self, value):
        self._preferred_timezone = self._validate_timezone(value)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def balance(self):
        return self._balance

    @classmethod
    def get_interest_rate(cls):
        return Account._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        Account._interest_rate = cls._validate_nonnegative("interest_rate", value)

    def _complete(self, code, candidate):
        instant = self._clock()
        if not isinstance(instant, datetime) or instant.tzinfo is None or instant.utcoffset() is None:
            raise TypeError("clock must return an aware datetime")
        utc_instant = instant.astimezone(timezone.utc)
        counter = next(Account._counter)
        if type(counter) is not int:
            raise TypeError("counter must be an int")
        if counter <= 0:
            raise ValueError("counter must be positive")
        confirmation = format_confirmation(code, self.account_id, utc_instant, counter)
        if code != "X":
            self._balance = candidate
        return confirmation

    def deposit(self, amount):
        amount = self._validate_number("amount", amount)
        if amount < 0.01:
            raise ValueError("amount must be at least 0.01")
        candidate = self.balance + amount
        if not isfinite(candidate):
            raise ValueError("candidate balance must be finite")
        return self._complete("D", candidate)

    def withdraw(self, amount):
        amount = self._validate_number("amount", amount)
        if amount < 0.01:
            raise ValueError("amount must be at least 0.01")
        candidate = self.balance - amount
        if candidate < 0:
            return self._complete("X", self.balance)
        if not isfinite(candidate):
            raise ValueError("candidate balance must be finite")
        return self._complete("W", candidate)

    def pay_interest(self):
        interest = self.balance * Account._interest_rate / 100
        candidate = self.balance + interest
        if not isfinite(candidate):
            raise ValueError("candidate balance must be finite")
        return self._complete("I", candidate)
