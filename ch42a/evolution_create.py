# evolution_create.py
import shelve

from evolution_models import Badge


if __name__ == '__main__':
    with shelve.open('evolution', flag='n') as records:
        records['badge:ada'] = Badge('Ada')
        print(records['badge:ada'].describe())
