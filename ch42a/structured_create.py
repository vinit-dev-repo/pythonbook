# structured_create.py
import shelve

from structured_records import Manager, Person


if __name__ == '__main__':
    name = {'first': 'Ada', 'last': 'Lovelace'}
    jobs = ['engineer']
    person = Person('person:ada', name, jobs, pay=50_000)
    manager = Manager('person:mina', {'first': 'Mina', 'last': 'Patel'}, ['lead'], pay=100_000)
    name['first'] = 'Changed'
    jobs.append('writer')
    with shelve.open('structured', flag='n') as records:
        records[person.record_id] = person
        records[manager.record_id] = manager
        print(*sorted(records))
        print(person.record_id, person.name, person.jobs, person.pay)
