# tombola_ops_demo.py
from bingo import BingoCage
from bingoaddable import AddableBingoCage
from callable_cages import CallableBingoCage, DiscardingBingoCage
from lotto import LotteryBlower
from tombolist import TomboList


def collect_calls(cage):
    values = []
    while True:
        try:
            values.append(cage())
        except LookupError:
            return tuple(sorted(values))


def broken_batch():
    yield 9
    raise RuntimeError('broken batch')


if __name__ == '__main__':
    discarded = DiscardingBingoCage([7])
    returned = CallableBingoCage([7])
    print('discarded singleton:', discarded(), discarded.inspect())
    print('returned singleton:', returned(), returned.inspect())
    print('duplicates:', collect_calls(CallableBingoCage([2, 1, 1])))
    for label, cage in (('discarded empty', DiscardingBingoCage()), ('returned empty', CallableBingoCage())):
        try:
            cage()
        except LookupError as error:
            print(label + ':', type(error).__name__)

    left = AddableBingoCage([2, 1])
    right = TomboList([3, 2])
    old_snapshot = left.inspect()
    combined = left + right
    print('plus:', combined is left, combined.inspect(), left.inspect(), right.inspect())
    print('direct list refusal:', left.__add__([4]) is NotImplemented)
    try:
        left + [4]
    except TypeError as error:
        print('expression list refusal:', type(error).__name__)
    try:
        [4] + left
    except TypeError as error:
        print('reverse refusal:', type(error).__name__)

    alias = left
    left += (value for value in (4, 4))
    print('iadd alias:', left is alias, old_snapshot, left.inspect())
    left += left
    print('self iadd:', left.inspect())
    try:
        left += 5
    except TypeError as error:
        print('scalar no change:', type(error).__name__, left is alias, left.inspect())
    partial = AddableBingoCage([1])
    partial_alias = partial
    try:
        partial += broken_batch()
    except RuntimeError as error:
        print('partial failure:', type(error).__name__, partial is partial_alias, partial.inspect())
