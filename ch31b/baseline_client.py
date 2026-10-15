# baseline_client.py
from record_models import Manager, Person


if __name__ == '__main__':
    ada = Person('Ada Lovelace', 'engineer', 50_000)
    mina = Manager('Mina Patel', 100_000)
    print(ada)
    print(mina)
    print(mina.lastName(), mina.job, mina.bonus)
