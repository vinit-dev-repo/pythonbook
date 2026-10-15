# structured_checks.py
from structured_records import Manager, Person


def expect_error(error_type, operation):
    try:
        operation()
    except error_type:
        return
    raise AssertionError(f'expected {error_type.__name__}')


if __name__ == '__main__':
    first = Person('person:first', {'first': 'First', 'last': 'One'})
    second = Person('person:second', {'first': 'Second', 'last': 'Two'})
    first.jobs.append('one-job')
    assert second.jobs == []

    caller_name = {'first': 'Ada', 'last': 'Lovelace'}
    caller_jobs = ['engineer']
    copied = Person('person:ada', caller_name, caller_jobs, pay=100)
    caller_name['first'] = 'Changed'
    caller_jobs.append('writer')
    assert copied.name == {'first': 'Ada', 'last': 'Lovelace'}
    assert copied.jobs == ['engineer']
    copied.giveRaise(0.015)
    assert copied.pay == 101
    before = copied.pay
    expect_error(TypeError, lambda: copied.giveRaise(True))
    expect_error(ValueError, lambda: copied.giveRaise(1.01))
    assert copied.pay == before
    expect_error(TypeError, lambda: Person('bad', {'first': 'Ada', 'last': 'Lovelace'}, pay=True))
    expect_error(ValueError, lambda: Person('bad', {'first': 'Ada', 'last': 'Lovelace'}, pay=10**12 + 1))
    at_limit = Person('person:limit', {'first': 'Limit', 'last': 'Case'}, pay=10**12)
    expect_error(ValueError, lambda: at_limit.giveRaise(0.10))
    assert at_limit.pay == 10**12

    manager_jobs = ['lead']
    manager = Manager(
        'person:mina', {'first': 'Mina', 'last': 'Patel'},
        manager_jobs, pay=100_000,
    )
    assert manager_jobs == ['lead']
    manager.giveRaise(0.10)
    assert manager.pay == 120_000 and manager.jobs == ['lead', 'manager']
    default_manager = Manager('person:new', {'first': 'New', 'last': 'Manager'})
    default_manager.jobs.append('solo')
    assert second.jobs == [] and manager.jobs == ['lead', 'manager']
    assert manager_jobs == ['lead']
    expect_error(TypeError, lambda: Person(3, {'first': 'Ada', 'last': 'Lovelace'}))
    expect_error(ValueError, lambda: Person(' ', {'first': 'Ada', 'last': 'Lovelace'}))
    expect_error(TypeError, lambda: Person('bad', ['Ada']))
    expect_error(TypeError, lambda: Person('bad', {'first': 'Ada'}))
    expect_error(TypeError, lambda: Person('bad', {'first': 'Ada', 'last': 3}))
    expect_error(ValueError, lambda: Person('bad', {'first': ' ', 'last': 'Lovelace'}))
    expect_error(TypeError, lambda: Person('bad', {'first': 'Ada', 'last': 'Lovelace'}, 'engineer'))
    expect_error(TypeError, lambda: Person('bad', {'first': 'Ada', 'last': 'Lovelace'}, [3]))
    expect_error(ValueError, lambda: Person('bad', {'first': 'Ada', 'last': 'Lovelace'}, [' ']))
    print('structured checks passed')
