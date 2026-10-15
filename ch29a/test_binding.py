# test_binding.py
import unittest
from counted import ClosureCountedCalls, CountedCalls
from inventory import format_stock, make_inventory

class BindingTests(unittest.TestCase):
    def check_strategy(self, decorator_type):
        Inventory = make_inventory(decorator_type)
        east = Inventory('east', 10)
        west = Inventory('west', 20)
        add = vars(Inventory)['add']
        quantity_now = vars(Inventory)['quantity_now']

        self.assertEqual(add.__name__, 'add')
        self.assertIn('positive built-in integer', add.__doc__)
        self.assertIs(add.__wrapped__, add.func)
        self.assertEqual(quantity_now.__name__, 'quantity_now')
        self.assertEqual(add.total_calls, 0)
        self.assertEqual(quantity_now.total_calls, 0)
        self.assertIsInstance(Inventory.add.decorator, decorator_type)
        self.assertEqual((add.calls_for(east), add.calls_for(west)), (0, 0))

        first = east.add
        second = east.add
        self.assertIsNot(first, second)
        self.assertIs(first.decorator, add)
        self.assertIs(first.subject, east)
        self.assertEqual(first.__name__, 'add')
        self.assertEqual(first.__doc__, add.__doc__)
        self.assertIs(first.__wrapped__, add.func)
        self.assertEqual((add.calls_for(east), add.total_calls), (0, 0))

        with self.assertRaises(TypeError):
            Inventory.add()
        with self.assertRaises(TypeError):
            Inventory.add(subject=east, amount=1)
        self.assertEqual((add.calls_for(east), add.total_calls), (0, 0))

        with self.assertRaises(TypeError):
            east.add()
        with self.assertRaises(TypeError):
            east.add(1, unexpected=True)
        self.assertEqual((east.quantity, add.calls_for(east), add.total_calls), (10, 2, 2))

        for invalid in (0, -1, True, 1.0, '1'):
            with self.subTest(invalid=invalid):
                before = east.quantity
                with self.assertRaises(ValueError):
                    east.add(invalid)
                self.assertEqual(east.quantity, before)
        self.assertEqual((add.calls_for(east), add.total_calls), (7, 7))

        self.assertEqual(first(2), 'east:12:stock')
        self.assertEqual(west.add(3, reason='delivery'), 'west:23:delivery')
        self.assertEqual(Inventory.add(east, 4, reason='audit'), 'east:16:audit')
        self.assertEqual((east.quantity, west.quantity), (16, 23))
        self.assertEqual((add.calls_for(east), add.calls_for(west), add.total_calls), (9, 1, 10))

        self.assertEqual(east.quantity_now(), 16)
        self.assertEqual((quantity_now.calls_for(east), quantity_now.total_calls), (1, 1))
        self.assertEqual((add.calls_for(east), add.total_calls), (9, 10))

        west.saved = first
        self.assertEqual(west.saved(1), 'east:17:stock')
        self.assertEqual((east.quantity, west.quantity), (17, 23))
        self.assertEqual((add.calls_for(east), add.calls_for(west), add.total_calls), (10, 1, 11))
        self.assertIsNot(east._call_counts, west._call_counts)

    def test_object_wrapper_contract(self):
        self.check_strategy(CountedCalls)

    def test_closure_wrapper_contract(self):
        self.check_strategy(ClosureCountedCalls)

    def test_standalone_decorations_are_independent(self):
        for decorator_type in (CountedCalls, ClosureCountedCalls):
            with self.subTest(decorator_type=decorator_type.__name__):
                first = decorator_type(format_stock)
                second = decorator_type(format_stock)
                self.assertIsNot(first, second)
                self.assertEqual(first('x', width=3), '  x')
                with self.assertRaises(TypeError):
                    first()
                self.assertEqual(first.total_calls, 2)
                self.assertEqual(second.total_calls, 0)

if __name__ == '__main__':
    unittest.main()
