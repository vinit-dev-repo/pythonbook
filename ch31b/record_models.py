# record_models.py
import math

from display_tools import AttrDisplay


MAX_PAY = 10**12


def _validate_text(value, label, allow_none=False):
    if value is None and allow_none:
        return None
    if type(value) is not str:
        raise TypeError(f'{label} must be a built-in string')
    value = value.strip()
    if not value:
        raise ValueError(f'{label} must not be empty')
    return value


def _validate_pay(pay):
    if type(pay) is not int:
        raise TypeError('pay must be a built-in integer')
    if not 0 <= pay <= MAX_PAY:
        raise ValueError('pay is outside the allowed range')
    return pay


def _validate_rate(rate, label='rate'):
    if type(rate) not in (int, float):
        raise TypeError(f'{label} must be a built-in int or float')
    if type(rate) is float and not math.isfinite(rate):
        raise ValueError(f'{label} must be finite')
    if not 0 <= rate <= 1:
        raise ValueError(f'{label} must be from 0 through 1')
    return rate


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = _validate_text(name, 'name')
        self.job = _validate_text(job, 'job', allow_none=True)
        self.pay = _validate_pay(pay)

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, rate):
        rate = _validate_rate(rate)
        candidate = int(self.pay * (1 + rate))
        _validate_pay(candidate)
        self.pay = candidate


class Manager(Person):
    def __init__(self, name, pay=0, bonus=0.10):
        self.bonus = _validate_rate(bonus, 'bonus')
        super().__init__(name, 'manager', pay)

    def giveRaise(self, rate):
        rate = _validate_rate(rate)
        adjusted = rate + self.bonus
        _validate_rate(adjusted, 'combined rate')
        super().giveRaise(adjusted)


class Department:
    def __init__(self, *members):
        for member in members:
            if not isinstance(member, Person):
                raise TypeError('members must be Person or Manager instances')
        self.members = list(members)

    def giveRaises(self, rate):
        rate = _validate_rate(rate)
        for member in self.members:
            member.giveRaise(rate)


if __name__ == '__main__':
    sample = Manager('Self Check', 100)
    sample.giveRaise(0.10)
    assert sample.pay == 120
    print('evolved record self-check passed')
