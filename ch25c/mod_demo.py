# mod_demo.py
from mod_direct import Mod


class RightParticipant:
    def __radd__(self, left):
        return 'right-hand accepted'


if __name__ == '__main__':
    a, b = Mod(2, 5), Mod(4, 5)
    print('forward:', a + b, a - b, a * b)
    print('reflected:', 9 + a, 9 - a, 9 * a)
    print('ordering:', a < b, a <= Mod(7, 5), b > a, b >= a)
    print('power:', Mod(2, 3) ** 3, Mod(2, 3) ** int(Mod(3, 3)))
    print('direct refusal:', a.__add__([]) is NotImplemented)
    print('reflected participation:', a + RightParticipant())
    alias = a
    keys = {a: 'original'}
    a += 4
    assert a is not alias and a == Mod(1, 5)
    assert alias == Mod(2, 5) and keys[Mod(7, 5)] == 'original'
    print('rebound/retained:', a, alias, keys[Mod(7, 5)])
