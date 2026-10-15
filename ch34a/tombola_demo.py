# tombola_demo.py
from bingo import BingoCage
from lotto import LotteryBlower
from tombola import Tombola
from tombolist import TomboList


def drain_sorted(device):
    drawn = []
    while True:
        try:
            drawn.append(device.pick())
        except LookupError:
            return tuple(sorted(drawn))


if __name__ == '__main__':
    class MissingLoad(Tombola):
        def pick(self):
            raise LookupError('no items')

    try:
        MissingLoad()
    except TypeError as error:
        print('incomplete real subclass:', type(error).__name__)

    for device_type in (BingoCage, LotteryBlower, TomboList):
        device = device_type([3, 1, 3])
        print(device_type.__name__, 'snapshot:', device.inspect())
        print(device_type.__name__, 'loaded:', device.loaded())
        print(device_type.__name__, 'draws:', drain_sorted(device))
        print(device_type.__name__, 'loaded after draw:', device.loaded())
        try:
            device.pick()
        except LookupError as error:
            print(device_type.__name__, 'exhaustion:', type(error).__name__)
    print('registered:', isinstance(TomboList(), Tombola), issubclass(TomboList, Tombola), Tombola in TomboList.__mro__)
