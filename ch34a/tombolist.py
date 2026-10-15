# tombolist.py
import random

from tombola import Tombola


@Tombola.register
class TomboList(list):
    def pick(self):
        if not self:
            raise LookupError('pick from empty TomboList')
        position = random.randrange(len(self))
        return self.pop(position)

    def load(self, iterable):
        self.extend(iterable)

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))
