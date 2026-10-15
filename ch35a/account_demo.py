# account_demo.py
from datetime import datetime, timezone
from itertools import count

from account import Account
from account_timezone import TimeZone
from confirmations import parse_confirmation


def fixed_now():
    return datetime(2026, 1, 1, 23, 45, 0, 987654, tzinfo=timezone.utc)


if __name__ == '__main__':
    saved_rate, saved_counter = Account._interest_rate, Account._counter
    try:
        Account.set_interest_rate(0.5)
        Account._counter = count(100)
        a = Account('A100', ' Ada ', ' Lovelace ', 1000, TimeZone('East', 5, 30), clock=fixed_now)
        b = Account('B200', 'Grace', 'Hopper', 20, TimeZone('West', -2, 15), clock=fixed_now)
        print('names:', a.full_name, '/', b.full_name)
        print('equivalent west:', b.preferred_timezone == TimeZone('West', -1, -45))
        for owner, confirmation in [(a, a.pay_interest()), (b, b.deposit(5)), (a, a.withdraw(2000))]:
            parsed = parse_confirmation(confirmation, owner.preferred_timezone)
            assert parsed.utc_time == parsed.local_time
            print(confirmation, 'balance:', owner.balance)
            print('times:', parsed.utc_time.isoformat(), '->', parsed.local_time.isoformat())
        assert (a.balance, b.balance) == (1005.0, 25.0)
    finally:
        Account._interest_rate, Account._counter = saved_rate, saved_counter
