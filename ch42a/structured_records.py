# structured_records.py
from display_tools import AttrDisplay
from record_models import _validate_pay, _validate_rate


def _text(value, label):
    if type(value) is not str:
        raise TypeError(f'{label} must be a built-in string')
    value = value.strip()
    if not value:
        raise ValueError(f'{label} must not be empty')
    return value


def _name(value):
    if type(value) is not dict or set(value) != {'first', 'last'}:
        raise TypeError('name must be a first/last dictionary')
    return {'first': _text(value['first'], 'first'), 'last': _text(value['last'], 'last')}


def _jobs(value):
    if value is None:
        return []
    if type(value) is not list:
        raise TypeError('jobs must be a list or None')
    return [_text(job, 'job') for job in value]


class Person(AttrDisplay):
    def __init__(self, record_id, name, jobs=None, pay=0):
        self.record_id = _text(record_id, 'record id')
        self.name = _name(name)
        self.jobs = _jobs(jobs)
        self.pay = _validate_pay(pay)

    def lastName(self):
        return self.name['last']

    def giveRaise(self, rate):
        rate = _validate_rate(rate)
        candidate = int(self.pay * (1 + rate))
        _validate_pay(candidate)
        self.pay = candidate


class Manager(Person):
    def __init__(self, record_id, name, jobs=None, pay=0, bonus=0.10):
        self.bonus = _validate_rate(bonus, 'bonus')
        super().__init__(record_id, name, jobs, pay)
        if 'manager' not in self.jobs:
            self.jobs.append('manager')

    def giveRaise(self, rate):
        rate = _validate_rate(rate)
        adjusted = rate + self.bonus
        _validate_rate(adjusted, 'combined rate')
        super().giveRaise(adjusted)
