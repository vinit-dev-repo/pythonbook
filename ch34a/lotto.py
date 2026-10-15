# lotto.py
import random

from tombola import Tombola


class LotteryBlower(Tombola):
    def __init__(self, balls=()):
        self._balls = list(balls)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        if not self._balls:
            raise LookupError('pick from empty LotteryBlower')
        position = random.randrange(len(self._balls))
        return self._balls.pop(position)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))
