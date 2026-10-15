# test_tombola_ops.py
import unittest

import test_tombola as baseline_tests
from bingo import BingoCage
from bingoaddable import AddableBingoCage
from callable_cages import CallableBingoCage, DiscardingBingoCage
from lotto import LotteryBlower
from tombola import Tombola
from tombolist import TomboList


IMPLEMENTATIONS = (BingoCage, LotteryBlower, TomboList)


def drain_calls(cage):
    values = []
    while True:
        try:
            values.append(cage())
        except LookupError:
            return values


class TombolaOpsTests(unittest.TestCase):
    def test_copied_common_suite_on_callable_extensions(self):
        original = baseline_tests.IMPLEMENTATIONS
        nested = unittest.TestResult()
        try:
            baseline_tests.IMPLEMENTATIONS = (CallableBingoCage, AddableBingoCage)
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(baseline_tests.TombolaContractTests)
            suite.run(nested)
        finally:
            baseline_tests.IMPLEMENTATIONS = original
        self.assertGreater(nested.testsRun, 0)
        self.assertTrue(nested.wasSuccessful(), (nested.errors, nested.failures))
        self.assertIs(baseline_tests.IMPLEMENTATIONS, original)
        print('nested contract tests:', nested.testsRun)

    def test_discarded_and_returned_singletons_and_empty_propagation(self):
        discarded = DiscardingBingoCage([7])
        returned = CallableBingoCage([7])
        self.assertIsNone(discarded())
        self.assertEqual(returned(), 7)
        self.assertEqual(discarded.inspect(), ())
        self.assertEqual(returned.inspect(), ())
        for cage in (discarded, returned):
            with self.assertRaises(LookupError):
                cage()

    def test_callable_preserves_duplicate_occurrences(self):
        cage = CallableBingoCage([2, 1, 1])
        self.assertEqual(tuple(sorted(drain_calls(cage))), (1, 1, 2))
        with self.assertRaises(LookupError):
            cage()

    def test_add_accepts_all_declared_tombola_operands(self):
        for kind in (BingoCage, LotteryBlower, TomboList, CallableBingoCage, AddableBingoCage):
            with self.subTest(other=kind.__name__):
                left = AddableBingoCage([2, 1, 2])
                other = kind([3, 3])
                result = left + other
                self.assertIs(type(result), AddableBingoCage)
                self.assertIsNot(result, left)
                self.assertIsNot(result, other)
                self.assertEqual(result.inspect(), (1, 2, 2, 3, 3))
                result.load([9])
                self.assertEqual(left.inspect(), (1, 2, 2))
                self.assertEqual(other.inspect(), (3, 3))
                left.load([0])
                other.load([8])
                self.assertEqual(result.inspect(), (1, 2, 2, 3, 3, 9))

    def test_add_refusal_and_no_reflected_support(self):
        left = AddableBingoCage([1])
        self.assertIs(left.__add__([2]), NotImplemented)
        self.assertFalse(hasattr(AddableBingoCage, '__radd__'))
        with self.assertRaises(TypeError):
            left + [2]
        with self.assertRaises(TypeError):
            [2] + left
        registered = TomboList([2])
        ordinary_list_result = registered + [3]
        self.assertIs(type(ordinary_list_result), list)
        self.assertEqual(ordinary_list_result, [2, 3])
        with self.assertRaises(TypeError):
            registered + left
        with self.assertRaises(TypeError):
            BingoCage([2]) + left
        self.assertEqual(left.inspect(), (1,))
        self.assertEqual(registered.inspect(), (2,))

    def test_iadd_accepts_finite_iterables_and_preserves_alias(self):
        cases = (
            ('list', lambda: [2, 2], [5], (2, 2, 5)),
            ('tuple', lambda: (0, 0), [1], (0, 0, 1)),
            ('string', lambda: 'ba', ['c'], ('a', 'b', 'c')),
            ('range', lambda: range(2), [7], (0, 1, 7)),
            ('generator', lambda: (value for value in (4, 4)), [9], (4, 4, 9)),
        )
        for label, factory, start, expected in cases:
            with self.subTest(incoming=label):
                incoming = factory()
                left = AddableBingoCage(start)
                alias = left
                before = left.inspect()
                left += incoming
                self.assertIs(left, alias)
                self.assertEqual(left.inspect(), expected)
                self.assertEqual(before, tuple(sorted(start)))
                self.assertIs(left.loaded(), True)
                if label == 'generator':
                    self.assertEqual(tuple(incoming), ())
                if label == 'list':
                    self.assertEqual(incoming, [2, 2])

    def test_iadd_tombola_self_alias_and_empty_inputs(self):
        for kind in (BingoCage, LotteryBlower, TomboList, CallableBingoCage, AddableBingoCage):
            with self.subTest(other=kind.__name__):
                left = AddableBingoCage([1, 2])
                alias = left
                before = left.inspect()
                other = kind([3, 3])
                left += other
                self.assertIs(left, alias)
                self.assertEqual(left.inspect(), (1, 2, 3, 3))
                self.assertEqual(other.inspect(), (3, 3))
                self.assertEqual(before, (1, 2))

        left = AddableBingoCage([1, 2, 2])
        alias = left
        left += left
        self.assertIs(left, alias)
        self.assertEqual(left.inspect(), (1, 1, 2, 2, 2, 2))
        left += []
        left += AddableBingoCage()
        self.assertIs(left, alias)
        self.assertEqual(left.inspect(), (1, 1, 2, 2, 2, 2))
        empty = AddableBingoCage()
        empty_alias = empty
        empty += []
        empty += AddableBingoCage()
        self.assertIs(empty, empty_alias)
        self.assertEqual(empty.inspect(), ())

    def test_noniterable_rejection_keeps_identity_and_contents(self):
        left = AddableBingoCage([1])
        alias = left
        before = left.inspect()
        with self.assertRaises(TypeError):
            left += 9
        self.assertIs(left, alias)
        self.assertEqual(left.inspect(), before)

    def test_partial_generator_failure_keeps_prior_loaded_value(self):
        for error_type in (RuntimeError, TypeError):
            with self.subTest(error=error_type.__name__):
                def broken():
                    yield 2
                    raise error_type('internal batch failure')

                left = AddableBingoCage([1])
                alias = left
                before = left.inspect()
                with self.assertRaisesRegex(error_type, '^internal batch failure$'):
                    left += broken()
                self.assertIs(left, alias)
                self.assertEqual(left.inspect(), (1, 2))
                self.assertEqual(before, (1,))

    def test_add_self_and_empty_operands_returns_fresh_contents(self):
        left = AddableBingoCage([1, 2, 2])
        doubled = left + left
        self.assertIsNot(doubled, left)
        self.assertEqual(doubled.inspect(), (1, 1, 2, 2, 2, 2))
        self.assertEqual(left.inspect(), (1, 2, 2))
        for a, b in (([], []), ([1, 1], []), ([], [1, 1])):
            with self.subTest(left=a, right=b):
                first, second = AddableBingoCage(a), TomboList(b)
                result = first + second
                self.assertIsNot(result, first)
                self.assertIsNot(result, second)
                self.assertEqual(result.inspect(), tuple(sorted(a + b)))
                self.assertEqual(first.inspect(), tuple(sorted(a)))
                self.assertEqual(second.inspect(), tuple(sorted(b)))

    def test_combined_outer_storage_still_shares_inner_objects(self):
        first_inner, second_inner = [1], [2]
        left = AddableBingoCage([first_inner])
        right = TomboList([second_inner])
        result = left + right
        snapshot = result.inspect()
        self.assertIs(snapshot[0], first_inner)
        self.assertIs(snapshot[1], second_inner)
        first_inner.append(3)
        self.assertEqual(snapshot, ([1, 3], [2]))
        self.assertIs(left.inspect()[0], result.inspect()[0])
        self.assertIs(right.inspect()[0], result.inspect()[1])


if __name__ == '__main__':
    unittest.main()
