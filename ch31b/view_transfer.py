# view_transfer.py
from record_models import Manager, Person
from record_view import RecordView


if __name__ == '__main__':
    target = Manager('Noor Khan', 20_000)
    colleague = Person('Ada Lovelace', pay=50_000)
    view = RecordView(target)
    saved = view.giveRaise
    view.name = 'Desk'
    view.pay = -1
    print(view.name, view.pay, target.pay, colleague.pay)
    print(saved(0.05))
    print(view.name, view.pay, target.pay)
    print(view)
    del view.pay
    print(view.pay, view.name)
    print(saved.__self__ is target, saved.__func__ is Manager.giveRaise)
    assert colleague.pay == 50_000
