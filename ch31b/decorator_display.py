# decorator_display.py
from display_tools import captured_display
from record_models import Manager, Person


if __name__ == '__main__':
    captured_display(Person)
    ada = Person('Ada Lovelace', 'engineer', 50_000)
    mina = Manager('Mina Patel', 100_000)
    print(ada)
    print(mina)
