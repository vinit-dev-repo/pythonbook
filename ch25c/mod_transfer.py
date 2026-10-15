# mod_transfer.py
from modular import Mod


if __name__ == '__main__':
    a = Mod(5, 7)
    alias = a
    keys = {a: 'old key'}
    old_hash = hash(a)
    a += 4
    assert a == Mod(2, 7) and a is not alias
    assert alias == Mod(5, 7) and hash(alias) == old_hash
    assert keys[Mod(12, 7)] == 'old key'
    assert alias.is_congruent(12) and alias != 12
    assert 9 - alias == Mod(4, 7)
    print('after +=:', a, alias, keys[Mod(12, 7)])
    before_power = a
    a **= 3
    assert a == Mod(1, 7) and a is not before_power
    assert before_power == Mod(2, 7)
    print('after **=:', a, 'earlier result:', before_power)
    before_failure = a
    try:
        a += Mod(1, 3)
    except ValueError:
        assert a is before_failure and a == Mod(1, 7)
        assert alias == Mod(5, 7) and hash(alias) == old_hash
        assert keys[Mod(12, 7)] == 'old key'
        print('rejected modulus:', a, keys[Mod(12, 7)])
    else:
        raise AssertionError('incompatible modulus unexpectedly succeeded')
    print('congruence/equality/reversed:', alias.is_congruent(12), alias == 12, 9 - alias)
