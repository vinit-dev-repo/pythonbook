# test_hook_insertion.py
import unittest

from hook_insertion import insert_private
from record_fixture import make_record_class


class HookInsertionTests(unittest.TestCase):
    def fixture(self):
        Record = make_record_class()
        existing = Record('Ada', 'rose')
        return Record, existing

    def test_fixtures_are_isolated_fresh_classes(self):
        first, first_record = self.fixture()
        second, second_record = self.fixture()
        self.assertIsNot(first, second)
        self.assertIsNot(first_record, second_record)
        self.assertEqual(first_record.label, 'ADA')
        self.assertEqual(second_record.label, 'ADA')
        insert_private('secret')(first)
        self.assertEqual(first_record.label, 'Ada')
        self.assertEqual(second_record.label, 'ADA')
        self.assertEqual(second_record.reveal(), 'rose')
        with self.assertRaisesRegex(ValueError, '^label must not be empty$'):
            second_record.label = ''
        self.assertEqual(second('Mina', 'violet').label, 'MINA')

    def test_same_class_and_existing_instance_survive_hook_replacement(self):
        Record, existing = self.fixture()
        original_get = Record.__getattribute__
        original_set = Record.__setattr__
        Original = Record
        original_instance = existing
        self.assertEqual(existing.label, 'ADA')
        with self.assertRaisesRegex(ValueError, '^label must not be empty$'):
            existing.label = ''
        self.assertIs(insert_private('secret', '__str__')(Record), Original)
        self.assertIs(type(existing), Original)
        self.assertIs(existing, original_instance)
        self.assertIsNot(Record.__getattribute__, original_get)
        self.assertIsNot(Record.__setattr__, original_set)
        self.assertEqual(existing.label, 'Ada')
        existing.label = ''
        self.assertEqual(existing.label, '')
        existing.label = 'Noor'
        self.assertEqual(existing.label, 'Noor')

    def test_denied_external_reads_and_writes_leave_state_unchanged(self):
        Record, existing = self.fixture()
        insert_private('secret', '__str__')(Record)
        with self.assertRaisesRegex(TypeError, '^private read: secret$'):
            existing.secret
        with self.assertRaisesRegex(TypeError, '^private write: secret$'):
            existing.secret = 'jade'
        self.assertEqual(object.__getattribute__(existing, 'secret'), 'rose')

    def test_internal_read_and_new_construction_fail(self):
        Record, existing = self.fixture()
        insert_private('secret', '__str__')(Record)
        with self.assertRaisesRegex(TypeError, '^private read: secret$'):
            existing.reveal()
        with self.assertRaisesRegex(TypeError, '^private write: secret$'):
            Record('Mina', 'violet')
        self.assertEqual(object.__getattribute__(existing, 'secret'), 'rose')

    def test_explicit_str_is_denied_but_implicit_str_uses_existing_type_method(self):
        Record, existing = self.fixture()
        insert_private('secret', '__str__')(Record)
        existing.label = 'Noor'
        with self.assertRaisesRegex(TypeError, '^private read: __str__$'):
            existing.__str__()
        self.assertEqual(str(existing), 'Record(Noor)')

    def test_implicit_str_can_still_fail_on_an_internal_denied_read(self):
        Record, existing = self.fixture()
        insert_private('label', '__str__')(Record)
        with self.assertRaisesRegex(TypeError, '^private read: __str__$'):
            existing.__str__()
        with self.assertRaisesRegex(TypeError, '^private read: label$'):
            str(existing)


if __name__ == '__main__':
    unittest.main()
