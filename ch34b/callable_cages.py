# callable_cages.py
from bingo import BingoCage


class DiscardingBingoCage(BingoCage):
    def __call__(self):
        self.pick()


class CallableBingoCage(BingoCage):
    def __call__(self):
        return self.pick()
