# csv_records.py
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation


class RecordParseError(ValueError):
    def __init__(self, record_number, field, reason):
        super().__init__(f'record {record_number} {field}: {reason}')
        self.record_number = record_number
        self.field = field
        self.reason = reason


class Observation:
    def __init__(self, observed_on, value):
        self.observed_on = observed_on
        self.value = value


def parse_date(text, record_number):
    try:
        return datetime.strptime(text.strip(), '%Y-%m-%d').date()
    except ValueError as error:
        raise RecordParseError(record_number, 'date', 'expected a valid date') from error


def parse_value(text, record_number):
    stripped = text.strip()
    if stripped == '.':
        return None
    try:
        value = Decimal(stripped)
    except InvalidOperation as error:
        raise RecordParseError(record_number, 'value', 'expected decimal or .') from error
    if not value.is_finite():
        raise RecordParseError(record_number, 'value', 'expected finite decimal')
    return value


def read_observations(path):
    candidate = []
    with open(path, newline='', encoding='utf-8') as source:
        reader = csv.reader(source, strict=True)
        if next(reader, None) != ['date', 'value']:
            raise RecordParseError(1, 'header', 'expected date,value')
        for record_number, row in enumerate(reader, start=2):
            if len(row) != 2:
                raise RecordParseError(record_number, 'row', 'expected exactly two fields')
            observed_on = parse_date(row[0], record_number)
            value = parse_value(row[1], record_number)
            if value is not None:
                candidate.append(Observation(observed_on, value))
    return tuple(candidate)


class ObservationSeries:
    def __init__(self):
        self._data = ()

    @property
    def data(self):
        return self._data

    def load(self, path):
        candidate = read_observations(path)
        self._data = candidate
