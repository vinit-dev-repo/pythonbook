# test_accounts.py
import math
import unittest
from datetime import datetime, timezone
from itertools import count
from unittest.mock import patch

import account as account_module
from account import Account
from account_timezone import TimeZone


class IntChild(int):
    pass


class FloatChild(float):
    pass


class StrChild(str):
    pass


def scripted(values):
    pending = iter(values)
    calls = []

    def read():
        calls.append(None)
        value = next(pending)
        if isinstance(value, Exception):
            raise value
        return value

    read.calls = calls
    return read


def utc():
    return datetime(2026, 1, 1, 23, 45, 0, 987654, tzinfo=timezone.utc)


class IsolatedAccountTest(unittest.TestCase):
    def setUp(self):
        old_rate = Account._interest_rate
        old_counter = Account._counter
        self.addCleanup(setattr, Account, '_interest_rate', old_rate)
        self.addCleanup(setattr, Account, '_counter', old_counter)
        Account.set_interest_rate(0.5)
        Account._counter = count(100)


class IdentityTests(IsolatedAccountTest):
    def test_normalized_names_read_only_identity_balance_and_default_zone(self):
        a = Account('A100', ' Ada ', ' Lovelace ', 1000)
        self.assertEqual((a.account_id, a.first_name, a.last_name, a.full_name, a.balance),
                         ('A100', 'Ada', 'Lovelace', 'Ada Lovelace', 1000.0))
        self.assertIs(type(a.balance), float)
        self.assertEqual(a.preferred_timezone, TimeZone('UTC'))
        for field in ('account_id', 'balance', 'full_name'):
            with self.subTest(field=field):
                before = vars(a).copy()
                with self.assertRaises(AttributeError):
                    setattr(a, field, 'changed')
                with self.assertRaises(AttributeError):
                    delattr(a, field)
                self.assertEqual(vars(a), before)

    def test_name_constructor_and_setter_rules_match_and_fail_without_mutation(self):
        a = Account('A100', 'Ada', 'Lovelace')
        for field in ('first_name', 'last_name'):
            for bad, error in ((None, TypeError), (42, TypeError), (StrChild('A'), TypeError),
                               ('', ValueError), (' \t ', ValueError)):
                with self.subTest(field=field, bad=repr(bad)):
                    args = dict(account_id='A100', first_name='Ada', last_name='Lovelace')
                    args[field] = bad
                    with self.assertRaises(error):
                        Account(**args)
                    before = vars(a).copy()
                    with self.assertRaises(error):
                        setattr(a, field, bad)
                    self.assertEqual(vars(a), before)
            setattr(a, field, '  Grace  ')
            self.assertEqual(getattr(a, field), 'Grace')
        self.assertEqual(a.full_name, 'Grace Grace')

    def test_account_id_grammar_is_not_silent_trimming(self):
        for valid in ('A100', 'z9', '123'):
            self.assertEqual(Account(valid, 'A', 'B').account_id, valid)
        for bad in ('', ' A100', 'A100 ', 'A-100', 'A_100', 'é100', 'A\n100', None, 100):
            with self.subTest(bad=repr(bad)):
                with self.assertRaises((TypeError, ValueError)):
                    Account(bad, 'A', 'B')

    def test_initial_balance_and_rate_domains(self):
        for value in (0, 0.0, 1, 1.5):
            a = Account('A', 'A', 'B', value)
            self.assertEqual(a.balance, float(value))
            Account.set_interest_rate(value)
            self.assertEqual(Account.get_interest_rate(), float(value))
        for bad, error in ((True, TypeError), ('1', TypeError), (IntChild(1), TypeError),
                           (FloatChild(1), TypeError), (-1, ValueError), (math.inf, ValueError),
                           (-math.inf, ValueError), (math.nan, ValueError), (10**400, ValueError)):
            with self.subTest(bad=repr(bad)):
                with self.assertRaises(error):
                    Account('A', 'A', 'B', bad)
                before = Account.get_interest_rate()
                with self.assertRaises(error):
                    Account.set_interest_rate(bad)
                self.assertEqual(Account.get_interest_rate(), before)

    def test_signed_components_equivalence_limits_and_unsupported_equality(self):
        west = TimeZone(' West ', -2, 15)
        equivalent = TimeZone('West', -1, -45)
        self.assertEqual(west, equivalent)
        self.assertEqual(west.offset.total_seconds(), -6300)
        self.assertNotEqual(west, TimeZone('Other', -1, -45))
        self.assertIs(west.__eq__(object()), NotImplemented)
        self.assertFalse(west == 0)
        for hours, minutes, seconds in ((-12, 0, -43200), (14, 0, 50400), (5, 30, 19800),
                                        (0, -59, -3540), (0, 59, 3540)):
            with self.subTest(hours=hours, minutes=minutes):
                self.assertEqual(TimeZone('Z', hours, minutes).offset.total_seconds(), seconds)
        for hours, minutes in ((-12, -1), (14, 1), (0, -60), (0, 60)):
            with self.assertRaises(ValueError):
                TimeZone('Z', hours, minutes)
        for hours, minutes in ((True, 0), (0, True), (1.0, 0), (0, IntChild(1))):
            with self.assertRaises(TypeError):
                TimeZone('Z', hours, minutes)
        for name, error in ((None, TypeError), (StrChild('Z'), TypeError), ('', ValueError), ('  ', ValueError)):
            with self.assertRaises(error):
                TimeZone(name)

    def test_timezone_assignment_and_public_value_fields(self):
        a = Account('A', 'A', 'B')
        zone = TimeZone('East', 5, 30)
        a.preferred_timezone = zone
        self.assertIs(a.preferred_timezone, zone)
        for bad in ('UTC', None, 0):
            before = vars(a).copy()
            with self.assertRaises(TypeError):
                a.preferred_timezone = bad
            self.assertEqual(vars(a), before)
            if bad is not None:
                with self.assertRaises(TypeError):
                    Account('A', 'A', 'B', preferred_timezone=bad)
        for field in ('name', 'offset', 'tzinfo'):
            before = vars(zone).copy()
            with self.assertRaises(AttributeError):
                setattr(zone, field, 'changed')
            with self.assertRaises(AttributeError):
                delattr(zone, field)
            self.assertEqual(vars(zone), before)


class TransactionTests(IsolatedAccountTest):
    def test_shared_ids_rate_independent_balances_and_half_percent(self):
        a = Account('A100', 'Ada', 'Lovelace', 1000, clock=utc)
        b = Account('B200', 'Grace', 'Hopper', 20, clock=utc)
        self.assertEqual(a.pay_interest(), 'I-A100-20260101234500-100')
        self.assertEqual(a.balance, 1005.0)
        self.assertEqual(b.balance, 20.0)
        Account.set_interest_rate(1)
        self.assertEqual(b.pay_interest(), 'I-B200-20260101234500-101')
        self.assertEqual(b.balance, 20.2)
        self.assertEqual(a.balance, 1005.0)
        self.assertEqual(a.withdraw(2000), 'X-A100-20260101234500-102')
        self.assertEqual(a.balance, 1005.0)
        self.assertEqual(a.withdraw(5), 'W-A100-20260101234500-103')
        self.assertEqual(a.balance, 1000.0)
        self.assertEqual(a.deposit(10), 'D-A100-20260101234500-104')
        self.assertEqual(a.balance, 1010.0)

    def test_minimum_amount_is_not_cent_quantization(self):
        a = Account('A', 'A', 'B', 1, clock=utc)
        a.deposit(0.01)
        self.assertEqual(a.balance, 1.01)
        b = Account('B', 'C', 'D', 1, clock=utc)
        b.deposit(0.011)
        self.assertEqual(b.balance, 1.011)
        c = Account('C', 'E', 'F', 0.01, clock=utc)
        c.withdraw(0.01)
        self.assertEqual(c.balance, 0.0)

    def test_invalid_amounts_leave_state_clock_and_counter_untouched(self):
        clock = scripted([utc()])
        a = Account('A', 'A', 'B', 10, clock=clock)
        before = vars(a).copy()
        cases = [(True, TypeError), ('1', TypeError), (IntChild(1), TypeError),
                 (FloatChild(1), TypeError), (0, ValueError), (-1, ValueError),
                 (0.009, ValueError), (math.inf, ValueError), (math.nan, ValueError),
                 (10**400, ValueError)]
        for method in (a.deposit, a.withdraw):
            for value, error in cases:
                with self.subTest(method=method.__name__, value=repr(value)):
                    with self.assertRaises(error):
                        method(value)
                    self.assertEqual(vars(a), before)
        self.assertEqual(clock.calls, [])
        self.assertEqual(next(Account._counter), 100)

    def test_finite_inputs_can_overflow_before_clock_or_counter(self):
        clock = scripted([utc()])
        a = Account('A', 'A', 'B', 1e308, clock=clock)
        for action in ('deposit', 'interest'):
            with self.subTest(action=action):
                before = vars(a).copy()
                with self.assertRaises(ValueError):
                    if action == 'deposit':
                        a.deposit(1e308)
                    else:
                        Account.set_interest_rate(1e308)
                        a.pay_interest()
                self.assertEqual(vars(a), before)
        self.assertEqual(clock.calls, [])
        self.assertEqual(next(Account._counter), 100)

    def test_clock_failures_happen_before_counter(self):
        for sample, error in ((RuntimeError('offline'), RuntimeError),
                               (datetime(2026, 1, 1), TypeError), ('now', TypeError)):
            with self.subTest(sample=repr(sample)):
                Account._counter = count(100)
                clock = scripted([sample])
                a = Account('A', 'A', 'B', 10, clock=clock)
                before = vars(a).copy()
                with self.assertRaises(error):
                    a.deposit(1)
                self.assertEqual(vars(a), before)
                self.assertEqual(len(clock.calls), 1)
                self.assertEqual(next(Account._counter), 100)

    def test_counter_failure_or_invalid_sample_preserves_balance(self):
        for counter, error in ((iter([]), StopIteration), (iter([True]), TypeError),
                               (iter([0]), ValueError), (iter([-1]), ValueError),
                               (iter([1.5]), TypeError), (iter([IntChild(1)]), TypeError)):
            with self.subTest(error=error):
                Account._counter = counter
                clock = scripted([utc()])
                a = Account('A', 'A', 'B', 10, clock=clock)
                before = vars(a).copy()
                with self.assertRaises(error):
                    a.deposit(1)
                self.assertEqual(vars(a), before)
                self.assertEqual(len(clock.calls), 1)

    def test_encoding_failure_consumes_counter_but_does_not_commit(self):
        a = Account('A', 'A', 'B', 10, clock=utc)
        before = vars(a).copy()
        with patch.object(account_module, 'format_confirmation', side_effect=RuntimeError('encoder failed')):
            with self.assertRaisesRegex(RuntimeError, 'encoder failed'):
                a.deposit(1)
        self.assertEqual(vars(a), before)
        self.assertEqual(a.deposit(1), 'D-A-20260101234500-101')
        self.assertEqual(a.balance, 11.0)

    def test_config_cleanup_restores_the_actual_shared_objects(self):
        old_rate, old_counter = Account._interest_rate, Account._counter

        class TemporaryChange(unittest.TestCase):
            def runTest(self):
                self.addCleanup(setattr, Account, '_interest_rate', old_rate)
                self.addCleanup(setattr, Account, '_counter', old_counter)
                Account.set_interest_rate(9)
                Account._counter = count(900)
                self.assertEqual(next(Account._counter), 900)

        result = unittest.TestResult()
        TemporaryChange().run(result)
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(Account._interest_rate, old_rate)
        self.assertIs(Account._counter, old_counter)


class ConfirmationTests(IsolatedAccountTest):
    def test_known_confirmation_fields_rollover_and_precision(self):
        from confirmations import Confirmation, format_confirmation, parse_confirmation

        instant = utc()
        text = format_confirmation('D', 'A100', instant, 100)
        self.assertEqual(text, 'D-A100-20260101234500-100')
        result = parse_confirmation(text, TimeZone('East', 5, 30))
        self.assertIs(type(result), Confirmation)
        self.assertEqual((result.code, result.account_id, result.counter), ('D', 'A100', 100))
        self.assertEqual(result.utc_time.isoformat(), '2026-01-01T23:45:00+00:00')
        self.assertEqual(result.local_time.isoformat(), '2026-01-02T05:15:00+05:30')
        self.assertEqual(result.local_time.astimezone(timezone.utc), result.utc_time)
        self.assertEqual(result.utc_time.microsecond, 0)
        west = parse_confirmation('W-B200-20260101003000-101', TimeZone('West', -2, 15))
        self.assertEqual(west.local_time.isoformat(), '2025-12-31T22:45:00-01:45')
        self.assertEqual(west.local_time, west.utc_time)
        self.assertEqual(parse_confirmation(text).local_time, result.utc_time)
        self.assertEqual(format_confirmation('I', 'A', datetime(1, 1, 1, tzinfo=timezone.utc), 1),
                         'I-A-00010101000000-1')
        for code in ('D', 'W', 'I', 'X'):
            with self.subTest(code=code):
                self.assertEqual(parse_confirmation(format_confirmation(code, 'A', instant, 1)).code, code)

    def test_parser_rejects_malformed_fields_with_explicit_causes(self):
        from confirmations import ConfirmationError, parse_confirmation

        texts = [None, 'D-A-20260101234500', 'D-A-20260101234500-1-extra',
                 'Z-A-20260101234500-1', 'D--20260101234500-1',
                 'D-A-100-20260101234500-1', 'D-A_1-20260101234500-1',
                 'D-é-20260101234500-1', 'D- A-20260101234500-1',
                 'D-A-2026010123450-1', 'D-A-202601012345000-1',
                 'D-A-２０２６0101234500-1', 'D-A-20260230000000-1',
                 'D-A-20261301000000-1', 'D-A-20260101240000-1',
                 'D-A-00000101000000-1', 'D-A-20260101234500-0',
                 'D-A-20260101234500--1', 'D-A-20260101234500-+1',
                 'D-A-20260101234500-1.0', 'D-A-20260101234500- 1',
                 'D-A-20260101234500-１', 'D-A-20260101234500-']
        for text in texts:
            with self.subTest(text=text):
                with self.assertRaises(ConfirmationError) as caught:
                    parse_confirmation(text)
                self.assertIsInstance(caught.exception.__cause__, (TypeError, ValueError, OverflowError))
                self.assertIsNot(caught.exception.__cause__, caught.exception)
        with self.assertRaises(ConfirmationError) as caught:
            parse_confirmation('D-A-20260230000000-1')
        self.assertIs(type(caught.exception.__cause__), ValueError)
        with self.assertRaises(ConfirmationError) as caught:
            parse_confirmation('D-A-20260101234500-1', 'UTC')
        self.assertIs(type(caught.exception.__cause__), TypeError)
        with self.assertRaises(ConfirmationError) as caught:
            parse_confirmation('D-A-00010101000000-1', TimeZone('West', -1))
        self.assertIs(type(caught.exception.__cause__), OverflowError)

    def test_formatter_rejects_collisions_and_bad_inputs(self):
        from confirmations import ConfirmationError, format_confirmation

        for code, account_id, instant, counter in [
            ('?', 'A', utc(), 1), ([], 'A', utc(), 1), ('D', 'A-B', utc(), 1),
            ('D', ' A', utc(), 1), ('D', 'é', utc(), 1),
            ('D', 'A', datetime(2026, 1, 1), 1), ('D', 'A', 'now', 1),
            ('D', 'A', utc(), True), ('D', 'A', utc(), 0), ('D', 'A', utc(), -1),
            ('D', 'A', utc(), 1.0),
        ]:
            with self.subTest(code=code, account_id=account_id, counter=counter):
                with self.assertRaises(ConfirmationError):
                    format_confirmation(code, account_id, instant, counter)


class FaultDetectionTests(IsolatedAccountTest):
    def test_real_name_and_initial_balance_failures_share_repaired_assertions(self):
        from account_failures import (CoercingNamesAccount, UntrimmedNamesAccount,
                                      MissingBalanceValidation, assert_name_rule,
                                      assert_initial_balance_rule)

        assert_name_rule(Account)
        assert_initial_balance_rule(Account)
        for cls, check, message in [
            (CoercingNamesAccount, assert_name_rule, 'None name was accepted'),
            (UntrimmedNamesAccount, assert_name_rule, 'name was not stripped'),
            (MissingBalanceValidation, assert_initial_balance_rule, 'negative initial balance was accepted'),
        ]:
            with self.subTest(cls=cls.__name__):
                with self.assertRaisesRegex(AssertionError, message):
                    check(cls)
        self.assertEqual(MissingBalanceValidation('A', 'A', 'B', -1).balance, -1)

    def test_truth_assertion_does_not_compare_the_second_argument(self):
        actual = 'BROKEN'
        self.assertTrue('A100', actual)
        with self.assertRaises(AssertionError):
            self.assertEqual('A100', actual)
        self.assertEqual('A100', Account('A100', 'A', 'B').account_id)


if __name__ == '__main__':
    unittest.main(verbosity=2)
