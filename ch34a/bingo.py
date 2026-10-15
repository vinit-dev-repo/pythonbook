# bingo.py
import random

from tombola import Tombola


class BingoCage(Tombola):
    def __init__(self, items=()):
        self._items = []
        self.load(items)

    def load(self, iterable):
        self._items.extend(iterable)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError as error:
            raise LookupError('pick from empty BingoCage') from error
