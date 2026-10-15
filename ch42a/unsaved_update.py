# unsaved_update.py
import shelve


if __name__ == '__main__':
    with shelve.open('records', flag='w') as records:
        mina = records['person:mina']
        mina.giveRaise(0.10)
        print('memory', mina.pay)
