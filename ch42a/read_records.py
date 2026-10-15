# read_records.py
import shelve

import record_models


if __name__ == '__main__':
    with shelve.open('records', flag='r') as records:
        mina = records['person:mina']
        print('reopened', mina.pay, mina.lastName(), repr(mina))
