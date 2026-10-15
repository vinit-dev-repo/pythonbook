# test_processor.py
import unittest

from processor import END, processor, ListReader, CountdownReader, ListWriter, TextWriter, describe


class IntChild(int):
    pass


class StrChild(str):
    pass


class ListChild(list):
    pass


class ProcessorTests(unittest.TestCase):
    def test_two_reader_two_writer_substitution_matrix_uses_unchanged_client(self):
        expected = ['int:2', 'int:1', 'int:0']
        for make_reader in (lambda: ListReader([2, 1, 0]), lambda: CountdownReader(2)):
            for writer_type in (ListWriter, TextWriter):
                with self.subTest(writer=writer_type.__name__, reader=make_reader):
                    reader, writer = make_reader(), writer_type()
                    self.assertIsNone(processor(reader, describe, writer))
                    if writer_type is ListWriter:
                        self.assertEqual(writer.items, expected)
                    else:
                        self.assertEqual(writer.text, 'int:2\nint:1\nint:0\n')
                    self.assertIs(reader.read(), END)
                    self.assertIs(reader.read(), END)

    def test_empty_input_never_converts_or_writes(self):
        calls = []
        def converter(value):
            calls.append(value)
            return 'unexpected'
        for writer in (ListWriter(), TextWriter()):
            reader = ListReader([])
            self.assertIsNone(processor(reader, converter, writer))
            self.assertIs(reader.read(), END)
            self.assertIs(reader.read(), END)
            self.assertEqual(writer.items if isinstance(writer, ListWriter) else writer.text,
                             [] if isinstance(writer, ListWriter) else '')
        self.assertEqual(calls, [])

    def test_false_values_and_empty_converted_strings_are_data(self):
        writer = ListWriter()
        processor(ListReader([0, '', False, None, 'ok']), describe, writer)
        self.assertEqual(writer.items, ['int:0', "str:''", 'bool:False', 'NoneType:None', "str:'ok'"])
        for writer in (ListWriter(), TextWriter()):
            processor(ListReader([1, 2]), lambda value: '', writer)
            if isinstance(writer, ListWriter):
                self.assertEqual(writer.items, ['', ''])
            else:
                self.assertEqual(writer.text, '\n\n')

    def test_outer_copy_shared_record_reference_and_independent_readers(self):
        record = ['original']
        source = [record, 'second']
        first, second = ListReader(source), ListReader(source)
        source[1] = 'replacement'
        source.append('extra')
        record.append('changed inside')
        self.assertIs(first.read(), record)
        self.assertEqual(first.read(), 'second')
        self.assertIs(first.read(), END)
        self.assertIs(second.read(), record)
        self.assertEqual(record, ['original', 'changed inside'])
        self.assertEqual(second.read(), 'second')
        self.assertIs(second.read(), END)
        self.assertEqual(ListReader(('tuple record',)).read(), 'tuple record')

    def test_reserved_marker_and_container_domain_use_identity(self):
        for bad in ('abc', {}, None, 3, ListChild([1])):
            with self.assertRaises(TypeError):
                ListReader(bad)
        for records in ([END], [0, END], (END,)):
            with self.assertRaises(ValueError):
                ListReader(records)
        class EqualityTrap:
            def __eq__(self, other):
                raise AssertionError('sentinel checks must not call equality')
        item = EqualityTrap()
        writer = ListWriter()
        processor(ListReader([item]), lambda value: 'accepted', writer)
        self.assertEqual(writer.items, ['accepted'])

    def test_countdown_domain_inclusive_zero_and_independent_state(self):
        for bad in (True, 2.0, '2', IntChild(2), None):
            with self.assertRaises(TypeError):
                CountdownReader(bad)
        with self.assertRaises(ValueError):
            CountdownReader(-1)
        first, second = CountdownReader(0), CountdownReader(1)
        self.assertEqual(first.read(), 0)
        self.assertIs(first.read(), END)
        self.assertIs(first.read(), END)
        self.assertEqual([second.read(), second.read()], [1, 0])
        self.assertIs(second.read(), END)

    def test_writer_domain_rejection_before_mutation_and_independent_state(self):
        for writer_type in (ListWriter, TextWriter):
            first, second = writer_type(), writer_type()
            self.assertIsNone(first.write('kept'))
            before = first.items[:] if writer_type is ListWriter else first.text
            for bad in (None, 0, False, b'bytes', StrChild('child')):
                with self.assertRaises(TypeError):
                    first.write(bad)
                self.assertEqual(first.items if writer_type is ListWriter else first.text, before)
            self.assertEqual(second.items if writer_type is ListWriter else second.text,
                             [] if writer_type is ListWriter else '')
            first.write('')
            first.write('a\nb')
            self.assertEqual(first.items if writer_type is ListWriter else first.text,
                             ['kept', '', 'a\nb'] if writer_type is ListWriter else 'kept\n\na\nb\n')
        reader, writer = ListReader([1, 2]), ListWriter()
        with self.assertRaises(TypeError):
            processor(reader, lambda value: value, writer)
        self.assertEqual(writer.items, [])
        self.assertEqual(reader.read(), 2)

    def test_actual_call_order_terminal_read_and_ignored_writer_return(self):
        events = []
        class Reader:
            def __init__(self):
                self.source = ListReader([0, ''])
            def read(self):
                value = self.source.read()
                events.append(('read', 'END' if value is END else describe(value)))
                return value
        def convert(value):
            result = describe(value)
            events.append(('convert', result))
            return result
        class Writer:
            def write(self, value):
                events.append(('write', value))
                return 'ignored'
        self.assertIsNone(processor(Reader(), convert, Writer()))
        self.assertEqual(events, [('read', 'int:0'), ('convert', 'int:0'), ('write', 'int:0'),
                                  ('read', "str:''"), ('convert', "str:''"), ('write', "str:''"),
                                  ('read', 'END')])

    def test_each_failure_preserves_prior_writes_and_consumed_boundary(self):
        for stage in ('read', 'convert', 'write'):
            with self.subTest(stage=stage):
                fault = RuntimeError(stage + ' failed')
                source = ListReader([1, 2, 3])
                target = ListWriter()
                events = []
                class Reader:
                    calls = 0
                    def read(self):
                        self.calls += 1
                        events.append(('read', self.calls))
                        if stage == 'read' and self.calls == 2:
                            raise fault
                        return source.read()
                def convert(value):
                    events.append(('convert', value))
                    if stage == 'convert' and value == 2:
                        raise fault
                    return str(value)
                class Writer:
                    def write(self, value):
                        events.append(('write', value))
                        if stage == 'write' and value == '2':
                            raise fault
                        target.write(value)
                with self.assertRaises(RuntimeError) as caught:
                    processor(Reader(), convert, Writer())
                self.assertIs(caught.exception, fault)
                self.assertEqual(target.items, ['1'])
                self.assertEqual(source.read(), 2 if stage == 'read' else 3)
                expected = [('read', 1), ('convert', 1), ('write', '1'), ('read', 2)]
                if stage != 'read':
                    expected.append(('convert', 2))
                if stage == 'write':
                    expected.append(('write', '2'))
                self.assertEqual(events, expected)

    def test_same_complete_result_check_detects_truthiness_bug(self):
        def faulty_processor(reader, converter, writer):
            while True:
                data = reader.read()
                if not data:
                    return None
                writer.write(converter(data))
        def check_all_records(client, writer):
            client(ListReader([0, '', False, None, 'ok']), describe, writer)
            self.assertEqual(writer.items, ['int:0', "str:''", 'bool:False', 'NoneType:None', "str:'ok'"],
                             'false-valued records were lost')
        check_all_records(processor, ListWriter())
        bad_result = ListWriter()
        with self.assertRaisesRegex(AssertionError, 'false-valued records were lost'):
            check_all_records(faulty_processor, bad_result)
        self.assertEqual(bad_result.items, [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
