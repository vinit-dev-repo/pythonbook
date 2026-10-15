# view_client.py
from record_models import Manager
from record_view import RecordView


if __name__ == '__main__':
    target = Manager('Mina Patel', 100_000)
    view = RecordView(target)
    saved = view.giveRaise
    print(saved.__self__ is target)
    view.pay = 999
    print(view.pay, target.pay)
    print(saved(0.10))
    print(view.pay, target.pay)
    print(view)
