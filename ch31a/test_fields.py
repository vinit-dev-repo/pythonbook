# test_fields.py
import unittest
from fields import CharField, IntegerField


def record_with(descriptor):
    class Record:
        value = descriptor
    return Record


class ConstructorDefaultsTests(unittest.TestCase):
    def test_integer_no_arguments(self):
        Record = record_with(IntegerField())
        item = Record()
        item.value = 10**400
        self.assertEqual(item.value, 10**400)

    def test_integer_one_argument(self):
        Record = record_with(IntegerField(0))
        item = Record()
        item.value = 0
        self.assertEqual(item.value, 0)

    def test_char_no_arguments(self):
        Record = record_with(CharField())
        item = Record()
        item.value = ""
        self.assertEqual(item.value, "")

    def test_char_one_argument(self):
        Record = record_with(CharField(0))
        item = Record()
        item.value = ""
        self.assertEqual(item.value, "")


class FieldTests(unittest.TestCase):
    def test_integer_bound_forms(self):
        cases = [
            ("omitted", lambda: IntegerField(), (-10**400, 10**400), ()),
            ("None", lambda: IntegerField(None, None), (-2, 2), ()),
            ("lower positional", lambda: IntegerField(0), (0, 1), (-1,)),
            ("lower keyword", lambda: IntegerField(min_value=-2), (-2, 0), (-3,)),
            ("upper keyword", lambda: IntegerField(max_value=0), (-1, 0), (1,)),
            ("upper positional", lambda: IntegerField(None, 0), (-1, 0), (1,)),
            ("two positional", lambda: IntegerField(-2, 2), (-2, 2), (-3, 3)),
            ("two keywords", lambda: IntegerField(min_value=-2, max_value=2), (-2, 2), (-3, 3)),
            ("zero width", lambda: IntegerField(0, 0), (0,), (-1, 1)),
            ("negative interval", lambda: IntegerField(-3, -1), (-3, -1), (-4, 0)),
            ("huge bounds", lambda: IntegerField(10**400, 10**400 + 1), (10**400, 10**400 + 1), (10**400 - 1, 10**400 + 2)),
        ]
        self.check_bound_cases(cases)

    def test_char_bound_forms(self):
        cases = [
            ("omitted", lambda: CharField(), ("", " a "), ()),
            ("None", lambda: CharField(None, None), ("", "abc"), ()),
            ("lower positional", lambda: CharField(1), ("a", "ab"), ("",)),
            ("lower keyword", lambda: CharField(min_length=1), ("a", "ab"), ("",)),
            ("upper keyword", lambda: CharField(max_length=1), ("", "a"), ("ab",)),
            ("upper positional", lambda: CharField(None, 1), ("", "a"), ("ab",)),
            ("two positional", lambda: CharField(1, 2), ("a", "ab"), ("", "abc")),
            ("two keywords", lambda: CharField(min_length=1, max_length=2), ("a", "ab"), ("", "abc")),
            ("zero width", lambda: CharField(0, 0), ("",), ("a",)),
        ]
        self.check_bound_cases(cases)

    def check_bound_cases(self, cases):
        for label, make_field, valid, invalid in cases:
            with self.subTest(case=label):
                Record = record_with(make_field())
                item = Record()
                for value in valid:
                    item.value = value
                    self.assertEqual(item.value, value)
                previous = item.value
                for value in invalid:
                    with self.assertRaises(ValueError):
                        item.value = value
                    self.assertEqual(item.value, previous)
                    unset = Record()
                    with self.assertRaises(ValueError):
                        unset.value = value
                    self.assertNotIn("_value", unset.__dict__)

    def test_configuration_errors(self):
        class IntSubclass(int):
            pass

        for field, names in [
            (IntegerField, ("min_value", "max_value")),
            (CharField, ("min_length", "max_length")),
        ]:
            for name in names:
                for bad in (True, False, 1.5, "1", IntSubclass(1)):
                    with self.subTest(field=field.__name__, bound=name, bad=repr(bad)):
                        with self.assertRaises(TypeError):
                            field(**{name: bad})
            with self.assertRaises(ValueError):
                field(2, 1)
        for name in ("min_length", "max_length"):
            with self.subTest(bound=name):
                with self.assertRaises(ValueError):
                    CharField(**{name: -1})

    def test_assignment_types_preserve_state(self):
        class IntSubclass(int):
            pass

        class StrSubclass(str):
            pass

        cases = [
            (IntegerField, 1, (True, False, None, 1.0, "1", IntSubclass(1))),
            (CharField, "a", (True, False, None, 1, b"a", StrSubclass("a"))),
        ]
        for field, good, invalid in cases:
            for bad in invalid:
                with self.subTest(field=field.__name__, bad=repr(bad)):
                    Record = record_with(field())
                    item = Record()
                    item.value = good
                    with self.assertRaises(TypeError):
                        item.value = bad
                    self.assertEqual(item.value, good)
                    unset = Record()
                    with self.assertRaises(TypeError):
                        unset.value = bad
                    self.assertNotIn("_value", unset.__dict__)

    def test_fields_instances_and_metadata(self):
        class Record:
            left = IntegerField()
            right = IntegerField()
            label = CharField()

        for name in ("left", "right", "label"):
            descriptor = Record.__dict__[name]
            self.assertIs(getattr(Record, name), descriptor)
            self.assertIs(descriptor.owner, Record)
            self.assertEqual(descriptor.name, name)
            self.assertEqual(descriptor.storage_name, "_" + name)
            with self.assertRaisesRegex(AttributeError, name):
                getattr(Record(), name)
        self.assertIsNot(Record.left, Record.right)
        first, second = Record(), Record()
        first.left, first.right, first.label = 1, 2, "A"
        second.left, second.right, second.label = 3, 4, "B"
        self.assertEqual((first.left, first.right, first.label), (1, 2, "A"))
        self.assertEqual((second.left, second.right, second.label), (3, 4, "B"))
        self.assertIsNot(first.__dict__, second.__dict__)

    def test_code_points_without_normalization(self):
        Record = record_with(CharField(max_length=1))
        item = Record()
        item.value = "é"
        self.assertEqual(len(item.value), 1)
        combining = "e\u0301"
        self.assertEqual(len(combining), 2)
        with self.assertRaises(ValueError):
            item.value = combining
        self.assertEqual(item.value, "é")
        Wider = record_with(CharField(0, 2))
        other = Wider()
        other.value = combining
        self.assertEqual(other.value, combining)


if __name__ == "__main__":
    unittest.main()
