# bingoaddable.py
from callable_cages import CallableBingoCage
from tombola import Tombola


class AddableBingoCage(CallableBingoCage):
    def __add__(self, other):
        if not isinstance(other, Tombola):
            return NotImplemented
        return AddableBingoCage(self.inspect() + other.inspect())

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            incoming = other.inspect()
        else:
            incoming = iter(other)
        self.load(incoming)
        return self
