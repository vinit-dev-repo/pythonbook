# account_transfer.py
from datetime import datetime, timezone
from itertools import count

from account import Account
from account_timezone import TimeZone
from confirmations import parse_confirmation


def first_clock():
    return datetime(2026, 3, 31, 23, 50, tzinfo=timezone.utc)


def second_clock():
    return datetime(2026, 4, 1, 0, 10, tzinfo=timezone.utc)


if __name__ == '__main__':
    saved_rate, saved_counter = Account._interest_rate, Account._counter
    try:
        Account.set_interest_rate(0.5)
        Account._counter = count(700)
        maya = Account('M7', 'Maya', 'Rao', 40, TimeZone('East', 5, 30), clock=first_clock)
        noah = Account('N8', 'Noah', 'Lee', 10, TimeZone('West', -4), clock=second_clock)
        first = maya.deposit(5)
        assert (maya.balance, noah.balance) == (45.0, 10.0)
        declined = noah.withdraw(20)
        assert (maya.balance, noah.balance) == (45.0, 10.0)
        accepted = maya.withdraw(12)
        assert (maya.balance, noah.balance) == (33.0, 10.0)
        for text, owner, expected_code, expected_counter, expected_local in [
            (first, maya, 'D', 700, '2026-04-01T05:20:00+05:30'),
            (declined, noah, 'X', 701, '2026-03-31T20:10:00-04:00'),
            (accepted, maya, 'W', 702, '2026-04-01T05:20:00+05:30'),
        ]:
            result = parse_confirmation(text, owner.preferred_timezone)
            assert (result.code, result.account_id, result.counter) == (expected_code, owner.account_id, expected_counter)
            assert result.local_time.isoformat() == expected_local
            assert result.local_time.astimezone(timezone.utc) == result.utc_time
            print(text, result.local_time.isoformat())
        maya_before, noah_before = vars(maya).copy(), vars(noah).copy()
        Account.set_interest_rate(1e308)
        try:
            maya.pay_interest()
        except ValueError:
            assert vars(maya) == maya_before and vars(noah) == noah_before
            print('failed candidate; balances:', maya.balance, noah.balance)
        else:
            raise AssertionError('overflowing candidate was accepted')
        Account.set_interest_rate(0.5)
        last = noah.pay_interest()
        assert last == 'I-N8-20260401001000-703'
        assert (maya.balance, noah.balance) == (33.0, 10.05)
        print(last, 'balances:', maya.balance, noah.balance)
    finally:
        Account._interest_rate, Account._counter = saved_rate, saved_counter
