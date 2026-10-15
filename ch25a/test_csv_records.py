# test_csv_records.py
import csv
import unittest
from datetime import date
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
from tempfile import TemporaryDirectory

from csv_records import Observation, ObservationSeries, RecordParseError, read_observations


class ClearFirstSeries(ObservationSeries):
    # Deliberately faulty: a later parse error leaves the old publication lost.
    def load(self, path):
        self._data = ()
        super().load(path)


class CSVRecordTests(unittest.TestCase):
    def setUp(self):
        folder = TemporaryDirectory(prefix='csv-record-tests-')
        self.addCleanup(folder.cleanup)
        self.folder = Path(folder.name)

    def fixture(self, text, name='case.csv'):
        path = self.folder / name
        path.write_text(text, encoding='utf-8', newline='')
        return path

    def snapshot(self, records):
        return tuple((record.observed_on, record.value) for record in records)

    def test_literal_fixture_types_precision_order_and_skipped_dot(self):
        records = read_observations('observations.csv')
        self.assertIs(type(records), tuple)
        self.assertEqual(self.snapshot(records), (
            (date(2026, 1, 2), Decimal('0.1000000000000000000000000001')),
            (date(2026, 1, 4), Decimal('-2.50')),
            (date(2026, 1, 4), Decimal('0'))))
        for record in records:
            self.assertIs(type(record), Observation)
            self.assertIs(type(record.observed_on), date)
            self.assertIs(type(record.value), Decimal)

    def test_header_must_match_exact_names_and_order(self):
        for text in ('', 'value,date\n', ' date,value\n', 'date,value \n',
                     'date,date\n', 'date,value,extra\n', '\n'):
            with self.subTest(text=text), self.assertRaises(RecordParseError) as caught:
                read_observations(self.fixture(text))
            self.assertEqual((caught.exception.record_number, caught.exception.field), (1, 'header'))

    def test_header_only_clears_but_zero_byte_failure_does_not(self):
        series = ObservationSeries()
        series.load('observations.csv')
        before = series.data
        with self.assertRaises(RecordParseError):
            series.load(self.fixture(''))
        self.assertIs(series.data, before)
        self.assertIsNone(series.load(self.fixture('date,value\n')))
        self.assertEqual(series.data, ())
        self.assertEqual(len(before), 3)
        series.load(self.fixture('date,value\n2026-01-01,.\n'))
        self.assertEqual(series.data, ())

    def test_blank_short_and_long_data_records_are_rejected(self):
        for row in ('\n', '2026-01-01\n', '2026-01-01,1,extra\n', '2026-01-01,.,extra\n'):
            with self.subTest(row=row), self.assertRaises(RecordParseError) as caught:
                read_observations(self.fixture('date,value\n' + row))
            self.assertEqual((caught.exception.record_number, caught.exception.field), (2, 'row'))

    def test_invalid_dates_are_errors_even_when_value_is_dot(self):
        for text in ('', '.', 'bad-date', '2026-02-30'):
            for value in ('1', '.'):
                with self.subTest(text=text, value=value), self.assertRaises(RecordParseError) as caught:
                    read_observations(self.fixture(f'date,value\n{text},{value}\n'))
                self.assertEqual((caught.exception.record_number, caught.exception.field), (2, 'date'))
                self.assertIsInstance(caught.exception.__cause__, ValueError)

    def test_nonmissing_invalid_values_are_not_silently_skipped(self):
        for text in ('', '  ', '..', 'oops', 'NaN', 'sNaN', 'Infinity', '-Infinity'):
            with self.subTest(text=text), self.assertRaises(RecordParseError) as caught:
                read_observations(self.fixture(f'date,value\n2026-01-01,{text}\n'))
            self.assertEqual((caught.exception.record_number, caught.exception.field), (2, 'value'))
            if text.strip() in ('', '..', 'oops'):
                self.assertIsInstance(caught.exception.__cause__, InvalidOperation)
            else:
                self.assertIsNone(caught.exception.__cause__)

    def test_disabled_decimal_trap_still_rejects_nonfinite_result(self):
        path = self.fixture('date,value\n2026-01-01,oops\n')
        with localcontext() as context:
            context.traps[InvalidOperation] = False
            with self.assertRaises(RecordParseError) as caught:
                read_observations(path)
            self.assertEqual(caught.exception.field, 'value')
            self.assertIn('finite', caught.exception.reason)

    def test_whitespace_quotes_parser_dates_zero_sign_and_exponents(self):
        path = self.fixture('date,value\n" 2026-1-2 "," . "\n'
                            '"2026-01-03"," 0 "\n2026-01-01,-2.50\n'
                            '2026-01-01,+1.2E+3\n2026-01-01,+1.2E+3\n')
        records = read_observations(path)
        self.assertEqual(self.snapshot(records), (
            (date(2026, 1, 3), Decimal('0')),
            (date(2026, 1, 1), Decimal('-2.50')),
            (date(2026, 1, 1), Decimal('1.2E+3')),
            (date(2026, 1, 1), Decimal('1.2E+3'))))
        self.assertEqual(str(records[2].value), '1.2E+3')
        self.assertIsNot(records[2], records[3])

    def assert_replacement_preserved(self, series_type):
        series = series_type()
        series.load('observations.csv')
        before = series.data
        records = tuple(before)
        values = self.snapshot(before)
        with self.assertRaises(RecordParseError) as caught:
            series.load('malformed.csv')
        self.assertEqual((caught.exception.record_number, caught.exception.field), (3, 'value'))
        self.assertIs(series.data, before, 'failed replacement changed tuple identity')
        self.assertEqual(self.snapshot(series.data), values)
        for current, previous in zip(series.data, records):
            self.assertIs(current, previous)
        series.load('replacement.csv')
        self.assertIsNot(series.data, before)
        self.assertEqual(self.snapshot(series.data), ((date(2026, 2, 1), Decimal('4.25')),))
        self.assertEqual(self.snapshot(before), values)
        return series

    def test_full_replacement_regression_detects_clear_first_stage(self):
        self.assert_replacement_preserved(ObservationSeries)
        with self.assertRaisesRegex(AssertionError, 'failed replacement changed tuple identity'):
            self.assert_replacement_preserved(ClearFirstSeries)

    def test_new_failure_and_external_errors_preserve_previous_data(self):
        new = ObservationSeries()
        with self.assertRaises(RecordParseError):
            new.load('malformed.csv')
        self.assertEqual(new.data, ())
        series = ObservationSeries()
        series.load('observations.csv')
        before = series.data
        malformed_quotes = self.fixture('date,value\n"2026-01-01,1\n', 'syntax.csv')
        bad_encoding = self.folder / 'encoding.csv'
        bad_encoding.write_bytes(b'date,value\n\xff')
        for path, error in ((self.folder / 'absent.csv', FileNotFoundError),
                            (malformed_quotes, csv.Error), (bad_encoding, UnicodeDecodeError)):
            with self.subTest(path=path), self.assertRaises(error):
                series.load(path)
            self.assertIs(series.data, before)
            self.assertEqual(len(series.data), 3)

    def test_logical_record_number_is_not_physical_line_number(self):
        path = self.fixture('date,value\n"2026-01-01\n",1\n2026-01-02,oops\n')
        with self.assertRaises(RecordParseError) as caught:
            read_observations(path)
        self.assertEqual(caught.exception.record_number, 3)
        self.assertEqual(caught.exception.field, 'value')

    def test_tuple_is_read_only_outer_storage_not_immutable_records(self):
        series = ObservationSeries()
        series.load('replacement.csv')
        saved = series.data
        with self.assertRaises(AttributeError):
            series.data = ()
        with self.assertRaises(TypeError):
            series.data[0] = Observation(date(2026, 1, 1), Decimal('2'))
        saved[0].value = Decimal('7')
        self.assertIs(series.data, saved)
        self.assertEqual(series.data[0].value, Decimal('7'))


if __name__ == '__main__':
    unittest.main()
