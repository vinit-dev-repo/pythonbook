# record_client.py
from person import Department, Manager, Person


if __name__ == "__main__":
    ada = Person("Ada Lovelace", "engineer", 50_000)
    mina = Manager("Mina Patel", 100_000)
    print(mina.lastName())
    mina.giveRaise(0.10)
    print(mina.job)
    print(mina.pay)
    print(mina)

    department_ada = Person("Ada Lovelace", "engineer", 50_000)
    department_mina = Manager("Mina Patel", 100_000)
    department = Department(department_ada, department_mina, department_ada)
    print(department.giveRaises(0.10))
    print(department_ada.pay)
    print(department_mina.pay)

    first = Person("First", pay=10_000)
    blocked = Person("Blocked", pay=10**12)
    later = Person("Later", pay=10_000)
    batch = Department(first, blocked, later)
    try:
        batch.giveRaises(0.10)
    except ValueError as error:
        print(error)
    print(first.pay, blocked.pay, later.pay)
