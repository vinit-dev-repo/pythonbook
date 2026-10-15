# csv_transfer.py
import csv
from datetime import date
from decimal import Decimal
from io import StringIO

from csv_records import RecordParseError, parse_date, parse_value


class LabelledObservation:
    def __init__(self, observed_on, label, value):
        self.observed_on = observed_on
        self.label = label
        self.value = value


def read_labelled(text):
    candidate = []
    reader = csv.reader(StringIO(text), strict=True)
    if next(reader, None) != ['date', 'label', 'value']:
        raise RecordParseError(1, 'header', 'expected date,label,value')
    for number, row in enumerate(reader, start=2):
        if len(row) != 3:
            raise RecordParseError(number, 'row', 'expected exactly three fields')
        observed_on = parse_date(row[0], number)
        label = row[1].strip()
        if not label:
            raise RecordParseError(number, 'label', 'expected a nonempty label')
        value = parse_value(row[2], number)
        if value is not None:
            candidate.append(LabelledObservation(observed_on, label, value))
    return tuple(candidate)


class LabelledSeries:
    def __init__(self):
        self._data = ()

    @property
    def data(self):
        return self._data

    def load(self, text):
        candidate = read_labelled(text)
        self._data = candidate


def snapshot(records):
    return tuple((item.observed_on, item.label, item.value) for item in records)


if __name__ == '__main__':
    valid = ('date,label,value\n2026-04-01, north ,1.25\n'
             '2026-04-02,south,.\n2026-04-03,east,-3\n')
    invalid = 'date,label,value\n2026-05-01,west,8\n2026-05-02, ,9\n'
    retry = 'date,label,value\n2026-06-01,center,0\n'
    series = LabelledSeries()
    assert series.load(valid) is None
    old = series.data
    references = tuple(old)
    expected = ((date(2026, 4, 1), 'north', Decimal('1.25')),
                (date(2026, 4, 3), 'east', Decimal('-3')))
    assert snapshot(old) == expected
    print('published:', [(item.label, str(item.value)) for item in old])
    try:
        series.load(invalid)
    except RecordParseError as error:
        assert (error.record_number, error.field) == (3, 'label')
        assert series.data is old and snapshot(series.data) == expected
        assert all(current is prior for current, prior in zip(series.data, references))
        print('rejected:', error.record_number, error.field, 'old tuple retained')
    else:
        raise AssertionError('empty-label replacement unexpectedly succeeded')
    assert series.load(retry) is None
    assert series.data is not old
    assert snapshot(series.data) == ((date(2026, 6, 1), 'center', Decimal('0')),)
    assert snapshot(old) == expected
    print('retry:', [(item.label, str(item.value)) for item in series.data])
