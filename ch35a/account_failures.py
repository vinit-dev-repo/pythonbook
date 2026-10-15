# account_failures.py
import unittest

from account import Account


class CoercingNamesAccount(Account):
    @staticmethod
    def _validate_name(name, value):
        return str(value)


class UntrimmedNamesAccount(Account):
    @staticmethod
    def _validate_name(name, value):
        if type(value) is not str:
            raise TypeError('name must be a string')
        if not value.strip():
            raise ValueError('name must not be blank')
        return value


class MissingBalanceValidation(Account):
    def __init__(self, account_id, first_name, last_name, initial_balance):
        super().__init__(account_id, first_name, last_name, 0)
        self._balance = initial_balance


def assert_name_rule(cls):
    rejected = False
    try:
        cls('A100', None, 'Lovelace')
    except TypeError:
        rejected = True
    assert rejected, 'None name was accepted'
    value = cls('A100', ' Ada ', 'Lovelace')
    assert value.first_name == 'Ada', 'name was not stripped'


def assert_initial_balance_rule(cls):
    rejected = False
    try:
        cls('A100', 'Ada', 'Lovelace', -1)
    except ValueError:
        rejected = True
    assert rejected, 'negative initial balance was accepted'


if __name__ == '__main__':
    assert_name_rule(Account)
    assert_initial_balance_rule(Account)
    for label, check, cls, expected in [
        ('coercion', assert_name_rule, CoercingNamesAccount, 'None name was accepted'),
        ('whitespace', assert_name_rule, UntrimmedNamesAccount, 'name was not stripped'),
        ('balance', assert_initial_balance_rule, MissingBalanceValidation, 'negative initial balance was accepted'),
    ]:
        try:
            check(cls)
        except AssertionError as error:
            assert str(error) == expected
            print(label + ' detected:', error)
        else:
            raise AssertionError('fault was not detected')
    test = unittest.TestCase()
    actual = 'BROKEN'
    test.assertTrue('A100', actual)
    try:
        test.assertEqual('A100', actual)
    except AssertionError:
        print('truth assertion passed; equality assertion detected the wrong value')
    else:
        raise AssertionError('equality check failed to detect the wrong value')
