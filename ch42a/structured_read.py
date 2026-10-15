# structured_read.py
import shelve

import structured_records


if __name__ == '__main__':
    with shelve.open('structured', flag='r') as records:
        person = records['person:ada']
        manager = records['person:mina']
        other = structured_records.Person('person:other', {'first': 'Mina', 'last': 'Patel'})
        print(person.record_id, person.lastName(), person.name, person.jobs, person.pay)
        print(manager.record_id, manager.lastName(), manager.jobs, manager.pay)
        print(person.giveRaise(0.10), person.pay)
        print(manager.giveRaise(0.0), manager.pay)
        print(other.jobs, person.jobs is other.jobs)
