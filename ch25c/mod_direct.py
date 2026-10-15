# mod_direct.py
from functools import total_ordering


@total_ordering
class Mod:
    def __init__(self, value, modulus):
        if type(value) is not int or type(modulus) is not int:
            raise TypeError('value and modulus must be built-in ints')
        if modulus <= 0:
            raise ValueError('modulus must be positive')
        self._value = value % modulus
        self._modulus = modulus

    @property
    def value(self):
        return self._value

    @property
    def modulus(self):
        return self._modulus

    def __repr__(self):
        return f'Mod({self.value}, {self.modulus})'

    def __int__(self):
        return self.value

    def __neg__(self):
        return Mod(-self.value, self.modulus)

    def __eq__(self, other):
        if type(self) is not Mod or type(other) is not Mod:
            return NotImplemented
        return (self.value, self.modulus) == (other.value, other.modulus)

    def __hash__(self):
        return hash((self.value, self.modulus))

    def is_congruent(self, integer):
        if type(integer) is not int:
            raise TypeError('congruence input must be a built-in int')
        return integer % self.modulus == self.value

    def __lt__(self, other):
        if type(self) is not Mod or type(other) is not Mod:
            return NotImplemented
        if self.modulus != other.modulus:
            raise ValueError('moduli must match')
        return self.value < other.value

    def __pow__(self, exponent, modulo=None):
        if modulo is not None or type(exponent) is not int:
            return NotImplemented
        if exponent < 0:
            raise ValueError('exponent must be nonnegative')
        return Mod(pow(self.value, exponent, self.modulus), self.modulus)

    def __add__(self, other):

        if type(other) is Mod:
            if self.modulus != other.modulus:
                raise ValueError('moduli must match')
            value = other.value
        elif type(other) is int:
            value = other
        else:
            return NotImplemented
        return Mod(self.value + value, self.modulus)

    def __radd__(self, other):

        if type(other) is Mod:
            if self.modulus != other.modulus:
                raise ValueError('moduli must match')
            value = other.value
        elif type(other) is int:
            value = other
        else:
            return NotImplemented
        return Mod(value + self.value, self.modulus)

    def __sub__(self, other):

        if type(other) is Mod:
            if self.modulus != other.modulus:
                raise ValueError('moduli must match')
            value = other.value
        elif type(other) is int:
            value = other
        else:
            return NotImplemented
        return Mod(self.value - value, self.modulus)

    def __rsub__(self, other):

        if type(other) is Mod:
            if self.modulus != other.modulus:
                raise ValueError('moduli must match')
            value = other.value
        elif type(other) is int:
            value = other
        else:
            return NotImplemented
        return Mod(value - self.value, self.modulus)

    def __mul__(self, other):

        if type(other) is Mod:
            if self.modulus != other.modulus:
                raise ValueError('moduli must match')
            value = other.value
        elif type(other) is int:
            value = other
        else:
            return NotImplemented
        return Mod(self.value * value, self.modulus)

    def __rmul__(self, other):

        if type(other) is Mod:
            if self.modulus != other.modulus:
                raise ValueError('moduli must match')
            value = other.value
        elif type(other) is int:
            value = other
        else:
            return NotImplemented
        return Mod(value * self.value, self.modulus)
