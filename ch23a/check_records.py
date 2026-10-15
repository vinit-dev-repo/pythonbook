# check_records.py
from person import Department, MAX_PAY, Manager, Person


def expect_error(error_type, operation):
    try:
        operation()
    except error_type:
        return
    if isinstance(error_type, tuple):
        expected = " or ".join(error.__name__ for error in error_type)
    else:
        expected = error_type.__name__
    raise AssertionError(f"expected {expected}")


if __name__ == "__main__":
    expect_error(TypeError, lambda: Person(3))
    expect_error(ValueError, lambda: Person("   "))
    expect_error(TypeError, lambda: Person("A", pay=True))
    expect_error(ValueError, lambda: Person("A", pay=MAX_PAY + 1))

    person = Person("Ada Lovelace", pay=100)
    assert person.lastName() == "Lovelace"
    assert person.giveRaise(0.015) is None
    assert person.pay == 101
    before = person.pay
    for bad_rate in (True, float("nan"), float("inf"), -0.01, 1.01):
        expect_error((TypeError, ValueError), lambda value=bad_rate: person.giveRaise(value))
        assert person.pay == before

    at_limit = Person("Limit", pay=MAX_PAY)
    expect_error(ValueError, lambda: at_limit.giveRaise(0.10))
    assert at_limit.pay == MAX_PAY

    manager = Manager("Mina Patel", 100_000)
    assert manager.job == "manager"
    assert manager.lastName() == "Patel"
    manager.giveRaise(0.10)
    assert manager.pay == 120_000
    expect_error(ValueError, lambda: Manager("Mina", 100, bonus=0.95).giveRaise(0.10))

    ada = Person("Ada", pay=50_000)
    department = Department(ada, manager, ada)
    assert department.giveRaises(0.10) is None
    assert ada.pay == 60_500
    assert manager.pay == 144_000

    first = Person("First", pay=10_000)
    blocked = Person("Blocked", pay=MAX_PAY)
    later = Person("Later", pay=10_000)
    expect_error(ValueError, lambda: Department(first, blocked, later).giveRaises(0.10))
    assert (first.pay, blocked.pay, later.pay) == (11_000, MAX_PAY, 10_000)
    print("record checks passed")
