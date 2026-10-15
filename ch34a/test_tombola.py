# test_tombola.py
import unittest

from bingo import BingoCage
from lotto import LotteryBlower
from tombola import Tombola
from tombolist import TomboList


IMPLEMENTATIONS = (BingoCage, LotteryBlower, TomboList)


class TombolaContractTests(unittest.TestCase):
    def assert_contents(self, device, expected):
        snapshot = device.inspect()
        self.assertIs(type(snapshot), tuple)
        self.assertEqual(snapshot, tuple(sorted(expected)))
        self.assertIs(device.loaded(), bool(expected))

    def assert_complete_draw(self, device, values):
        remaining = list(values)
        while remaining:
            picked = device.pick()
            self.assertIn(picked, remaining)
            remaining.remove(picked)  # Remove one occurrence, not every equal value.
        for _ in range(2):
            with self.assertRaises(LookupError):
                device.pick()
        self.assert_contents(device, [])

    def test_common_contract_and_caller_list_independence(self):
        for implementation in IMPLEMENTATIONS:
            with self.subTest(implementation=implementation.__name__):
                supplied = [3, 1, 3]
                device = implementation(supplied)
                self.assertEqual(supplied, [3, 1, 3])
                supplied.append(9)
                self.assert_contents(device, [1, 3, 3])
                extra = [2, 0, 2]
                device.load(extra)
                self.assertEqual(extra, [2, 0, 2])
                extra.append(8)
                self.assert_contents(device, [0, 1, 2, 2, 3, 3])
                self.assert_complete_draw(device, [0, 1, 2, 2, 3, 3])
                self.assertEqual(supplied, [3, 1, 3, 9])
                self.assertEqual(extra, [2, 0, 2, 8])

    def test_empty_load_exhaustion_and_reload(self):
        for implementation in IMPLEMENTATIONS:
            with self.subTest(implementation=implementation.__name__):
                device = implementation()
                self.assert_contents(device, [])
                self.assert_complete_draw(device, [])
                device.load([])
                self.assert_contents(device, [])
                device.load([4, 4])
                self.assert_contents(device, [4, 4])
                device.load(())
                self.assert_contents(device, [4, 4])
                self.assert_complete_draw(device, [4, 4])
                device.load([7, 1, 7])
                self.assert_contents(device, [1, 7, 7])
                self.assert_complete_draw(device, [1, 7, 7])

    def test_tuple_range_fresh_generators_and_separate_strings(self):
        for implementation in IMPLEMENTATIONS:
            with self.subTest(implementation=implementation.__name__):
                device = implementation((2, 1))
                device.load(range(3, 5))
                addition = (number for number in (5, 5))
                device.load(addition)
                self.assertEqual(tuple(addition), ())
                self.assert_contents(device, [1, 2, 3, 4, 5, 5])
                self.assert_complete_draw(device, [1, 2, 3, 4, 5, 5])

                initial = (number for number in (8, 2, 8))
                generated = implementation(initial)
                self.assertEqual(tuple(initial), ())
                self.assert_contents(generated, [2, 8, 8])
                self.assert_complete_draw(generated, [2, 8, 8])

                words = implementation(['blue', 'amber', 'blue'])
                words.load(('amber',))
                self.assert_contents(words, ['amber', 'amber', 'blue', 'blue'])
                self.assert_complete_draw(words, ['amber', 'amber', 'blue', 'blue'])

    def test_repeated_observations_preserve_duplicate_contents(self):
        for implementation in IMPLEMENTATIONS:
            with self.subTest(implementation=implementation.__name__):
                device = implementation([2, 1, 2])
                self.assert_contents(device, [1, 2, 2])
                self.assert_contents(device, [1, 2, 2])
                self.assert_complete_draw(device, [1, 2, 2])

    def test_instances_have_separate_outer_storage(self):
        for implementation in IMPLEMENTATIONS:
            with self.subTest(implementation=implementation.__name__):
                first, second = implementation([1]), implementation([2])
                first.load([3])
                self.assert_contents(first, [1, 3])
                self.assert_contents(second, [2])
                self.assert_complete_draw(first, [1, 3])
                self.assert_contents(second, [2])

    def test_input_and_snapshot_share_contained_objects(self):
        for implementation in IMPLEMENTATIONS:
            with self.subTest(implementation=implementation.__name__):
                inner = [1]
                supplied = [inner]
                device = implementation(supplied)
                snapshot = device.inspect()
                self.assertIs(type(snapshot), tuple)
                self.assertIs(snapshot[0], inner)
                supplied.clear()
                inner.append(2)
                self.assertEqual(snapshot, ([1, 2],))
                self.assertIs(device.inspect()[0], inner)
                self.assertIs(device.pick(), inner)
                self.assertIs(device.loaded(), False)

    def test_base_helpers_call_pick_then_load(self):
        class Counted(Tombola):
            def __init__(self):
                self.items = [2, 1]
                self.pick_calls = 0
                self.load_calls = 0

            def load(self, values):
                self.load_calls += 1
                self.items.extend(values)

            def pick(self):
                self.pick_calls += 1
                if not self.items:
                    raise LookupError
                return self.items.pop()

        counted = Counted()
        self.assertEqual(counted.inspect(), (1, 2))
        self.assertEqual(counted.pick_calls, 3)
        self.assertEqual(counted.load_calls, 1)
        counted.pick_calls = 0
        self.assertIs(counted.loaded(), True)
        self.assertEqual(counted.pick_calls, 3)
        self.assertEqual(counted.load_calls, 2)

    def test_optimized_helpers_do_not_call_pick(self):
        class GuardedLottery(LotteryBlower):
            def pick(self):
                raise AssertionError('optimized helper used pick')

        guarded = GuardedLottery([2, 1])
        self.assertEqual(guarded.inspect(), (1, 2))
        self.assertIs(guarded.loaded(), True)
        empty = GuardedLottery()
        self.assertEqual(empty.inspect(), ())
        self.assertIs(empty.loaded(), False)

    def test_registration_recognizes_without_inheriting_helpers(self):
        self.assertTrue(issubclass(TomboList, Tombola))
        self.assertTrue(isinstance(TomboList(), Tombola))
        self.assertNotIn(Tombola, TomboList.__mro__)
        for name in ('load', 'pick', 'loaded', 'inspect'):
            self.assertIn(name, TomboList.__dict__)

        @Tombola.register
        class BadRegistered:
            def pick(self):
                raise LookupError

        bad = BadRegistered()
        self.assertTrue(isinstance(bad, Tombola))
        with self.assertRaises(AttributeError):
            bad.inspect()

    def test_abstract_subclass_and_bingo_inherited_helpers(self):
        class MissingLoad(Tombola):
            def pick(self):
                raise LookupError

        with self.assertRaises(TypeError):
            Tombola()
        with self.assertRaises(TypeError):
            MissingLoad()
        self.assertIs(BingoCage.inspect, Tombola.inspect)
        self.assertIs(BingoCage.loaded, Tombola.loaded)


if __name__ == '__main__':
    unittest.main()
