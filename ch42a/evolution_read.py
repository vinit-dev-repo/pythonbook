# evolution_read.py
import shelve

import evolution_models


if __name__ == '__main__':
    with shelve.open('evolution', flag='r') as records:
        badge = records['badge:ada']
        print(badge.describe(), hasattr(badge, 'level'))
