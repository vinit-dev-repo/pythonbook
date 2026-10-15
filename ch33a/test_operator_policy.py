# test_operator_policy.py
import unittest

from attribute_policy import Public
from operator_policy import (
    CheckedReadingList,
    DeniedAddReadingList,
    DeniedIterReadingList,
    DirectAdd,
)
from reading_list import ReadingList


POLICY_ADD_ERROR = 'access denied: __add__'
POLICY_ITER_ERROR = 'access denied: __iter__'


class OperatorPolicyTests(unittest.TestCase):
    def target_of(self, wrapper):
        return object.__getattribute__(wrapper, '_Controlled__target')

    def test_plain_direct_lookup_and_implicit_lookup_differ(self):
        plain = Public('summary', '__str__', '__repr__', '__add__', '__getitem__', '__call__', '__iter__')(ReadingList)(['A', 'B'])
        self.assertEqual(plain.__add__(['C']).summary(), 'A, B, C')
        self.assertEqual(plain.__getitem__(0), 'A')
        self.assertEqual(plain.__call__(prefix='> '), '> A, B')
        self.assertEqual(list(plain.__iter__()), ['A', 'B'])
        self.assertIs(type(plain).__repr__, object.__repr__)
        self.assertIs(type(plain).__str__, object.__str__)
        self.assertEqual(repr(self.target_of(plain)), "ReadingList(['A', 'B'])")
        for operation in (lambda: plain + ['B'], lambda: plain[0], lambda: plain('> '), lambda: iter(plain)):
            with self.assertRaises(TypeError):
                operation()

    def test_target_validation_copy_and_raw_not_implemented(self):
        supplied = ['A']
        reading = ReadingList(supplied)
        supplied.append('B')
        self.assertEqual(reading.summary(), 'A')
        self.assertEqual(ReadingList([]).summary(), '')
        self.assertEqual(ReadingList(['']).summary(), '')
        self.assertEqual(list(ReadingList([])), [])
        self.assertEqual(list(reading + []), ['A'])

        class ListSubclass(list):
            pass

        class StringSubclass(str):
            pass

        for invalid in (None, 'A', ('A',), ListSubclass(['A']), [1], [StringSubclass('A')]):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(TypeError, '^titles must be an exact list of strings$'):
                    ReadingList(invalid)
        for unsupported in (1, ('B',), 'B', ListSubclass(['B']), CheckedReadingList(['B'])):
            self.assertIs(reading.__add__(unsupported), NotImplemented)
            with self.assertRaises(TypeError):
                reading + unsupported
        self.assertIs(ReadingList(['A']).__add__(1), NotImplemented)
        with self.assertRaises(TypeError):
            ReadingList(('A',))
        with self.assertRaises(TypeError):
            ReadingList(['A', 1])
        with self.assertRaises(TypeError):
            ReadingList(['A']) + ['B', 1]

    def test_checked_operations_keep_exact_raw_result_types(self):
        checked = CheckedReadingList(['A', 'B'])
        target = self.target_of(checked)
        right = ['C']
        result = checked + right
        self.assertIs(type(result), ReadingList)
        self.assertIsNot(result, target)
        self.assertIs(type(checked[:]), list)
        self.assertIs(type(checked(prefix='> ')), str)
        self.assertEqual(str(checked), 'ReadingList: A, B')
        self.assertIs(type(checked).__repr__, object.__repr__)
        self.assertEqual(checked(), 'A, B')
        self.assertEqual(checked[-1], 'B')
        self.assertEqual(checked[::-1], ['B', 'A'])
        sliced = checked[:]
        sliced.append('D')
        self.assertEqual(checked[:], ['A', 'B'])
        self.assertEqual(checked[:], ['A', 'B'])
        self.assertEqual(checked[1], 'B')
        self.assertEqual(checked('> '), '> A, B')
        self.assertEqual(checked(prefix='> '), '> A, B')
        self.assertEqual(result.summary(), 'A, B, C')
        self.assertEqual(target.summary(), 'A, B')
        self.assertEqual(right, ['C'])
        with self.assertRaises(IndexError):
            checked[4]
        with self.assertRaises(TypeError):
            checked['first']
        with self.assertRaises(TypeError):
            checked('one', 'two')
        with self.assertRaises(TypeError):
            checked(prefix=1)
        with self.assertRaises(TypeError):
            checked(unexpected='value')
        with self.assertRaises(ValueError):
            checked[::0]
        with self.assertRaises(TypeError):
            checked[1.5]
        right.append('D')
        self.assertEqual(result.summary(), 'A, B, C')

    def test_not_implemented_and_target_validation_propagate_through_forwarder(self):
        checked = CheckedReadingList(['A'])
        self.assertIs(checked.__add__(1), NotImplemented)
        with self.assertRaises(TypeError):
            checked + 1
        malformed = ['B', 1]
        for operation in (lambda: checked.__add__(malformed), lambda: checked + malformed):
            with self.assertRaisesRegex(TypeError, '^titles must be an exact list of strings$'):
                operation()
        self.assertEqual(malformed, ['B', 1])
        self.assertEqual(self.target_of(checked).summary(), 'A')

    def test_denied_add_stops_before_target_invocation(self):
        denied = DeniedAddReadingList(['A'])
        target = self.target_of(denied)
        calls = []

        def guard(titles):
            calls.append(titles)
            raise AssertionError('target __add__ should not run')

        right = ['B']
        target.__add__ = guard
        try:
            for operation in (lambda: denied.__add__(right), lambda: denied + right):
                with self.assertRaisesRegex(TypeError, f'^{POLICY_ADD_ERROR}$'):
                    operation()
        finally:
            del target.__add__
        self.assertEqual(calls, [])
        self.assertEqual(right, ['B'])
        self.assertEqual(target.summary(), 'A')

    def test_direct_add_bypasses_the_same_denial_explicitly_and_implicitly(self):
        direct = DirectAdd(['A'])
        target = self.target_of(direct)
        self.assertEqual(direct.__add__(['B']).summary(), 'A, B')
        self.assertEqual((direct + ['B']).summary(), 'A, B')
        self.assertIsInstance(direct, DeniedAddReadingList)
        self.assertEqual(str(direct), 'ReadingList: A')
        self.assertEqual(direct[0], 'A')
        self.assertEqual(direct(prefix='> '), '> A')
        self.assertEqual(list(direct), ['A'])
        self.assertEqual(target.summary(), 'A')

    def test_denied_iter_stops_before_target_invocation_even_with_getitem(self):
        denied = DeniedIterReadingList(['A', 'B'])
        target = self.target_of(denied)
        calls = []

        def guard():
            calls.append('iter')
            raise AssertionError('target __iter__ should not run')

        target.__iter__ = guard
        try:
            self.assertEqual(denied[0], 'A')
            for operation in (lambda: denied.__iter__(), lambda: iter(denied)):
                with self.assertRaisesRegex(TypeError, f'^{POLICY_ITER_ERROR}$'):
                    operation()
        finally:
            del target.__iter__
        self.assertEqual(calls, [])

    def test_iterators_are_raw_fresh_and_keep_their_own_exhaustion(self):
        checked = CheckedReadingList(['A', 'B'])
        first = iter(checked)
        second = iter(checked)
        self.assertIs(type(first), type(iter(['A'])))
        self.assertIsNot(first, second)
        self.assertIs(iter(first), first)
        self.assertEqual((next(first), next(second), next(first)), ('A', 'A', 'B'))
        with self.assertRaises(StopIteration):
            next(first)
        with self.assertRaises(StopIteration):
            next(first)
        self.assertEqual(list(second), ['B'])
        self.assertEqual(list(iter(checked)), ['A', 'B'])
        self.assertEqual([(outer, inner) for outer in checked for inner in checked], [
            ('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B'),
        ])


if __name__ == '__main__':
    unittest.main()
