# value_demo.py
from mod_direct import Mod


if __name__ == '__main__':
    values = [Mod(number, 3) for number in (-1, 2, 5)]
    print('residues:', [int(value) for value in values])
    value = values[0]
    print('value/int/negative:', repr(value), int(value), -value)
    print('congruence/equality:', value.is_congruent(5), value == 5)
    saved = {value: 'saved'}
    print('equivalent key:', saved[Mod(5, 3)], hash(value) == hash(Mod(5, 3)))
    print('different modulus:', value == Mod(2, 4))
