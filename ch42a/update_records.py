# update_records.py
import shelve


if __name__ == '__main__':
    with shelve.open('records', flag='w') as records:
        mina = records['person:mina']
        mina.giveRaise(0.10)
        records['person:mina'] = mina
        print('saved', mina.pay, *sorted(records))
