# csv_demo.py
from datetime import date
from decimal import Decimal

from csv_records import ObservationSeries, RecordParseError


def values(records):
    return tuple((item.observed_on.isoformat(), str(item.value)) for item in records)


if __name__ == '__main__':
    series = ObservationSeries()
    assert series.load('observations.csv') is None
    old_data = series.data
    old_records = tuple(old_data)
    expected = (('2026-01-02', '0.1000000000000000000000000001'),
                ('2026-01-04', '-2.50'), ('2026-01-04', '0'))
    assert type(old_data) is tuple and values(old_data) == expected
    assert type(old_data[0].observed_on) is date
    assert type(old_data[0].value) is Decimal
    assert old_data[0].value == Decimal('0.1000000000000000000000000001')
    print('published:', values(old_data))
    try:
        series.load('malformed.csv')
    except RecordParseError as error:
        assert error.record_number == 3 and error.field == 'value'
        assert series.data is old_data
        assert values(series.data) == expected
        assert all(current is prior for current, prior in zip(series.data, old_records))
        print('rejected:', error.record_number, error.field, 'old tuple retained')
    else:
        raise AssertionError('malformed replacement unexpectedly succeeded')
    assert series.load('replacement.csv') is None
    assert series.data is not old_data
    assert values(series.data) == (('2026-02-01', '4.25'),)
    assert values(old_data) == expected
    print('replacement:', values(series.data))
    print('saved old records:', len(old_data))
