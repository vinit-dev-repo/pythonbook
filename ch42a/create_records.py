# create_records.py
import shelve

from record_models import Manager, Person


SHELF_NAME = 'records'
ADA_ID = 'person:ada'
MINA_ID = 'person:mina'


if __name__ == '__main__':
    with shelve.open(SHELF_NAME, flag='c') as records:
        if records:
            raise RuntimeError('refusing to replace a nonempty shelf')
        records[ADA_ID] = Person('Ada Lovelace', 'engineer', 50_000)
        records[MINA_ID] = Manager('Mina Patel', 100_000)
        print(*sorted(records))
