# operator_demo.py
from attribute_policy import Public
from operator_policy import (
    CheckedReadingList,
    DeniedAddReadingList,
    DeniedIterReadingList,
    DirectAdd,
)
from reading_list import ReadingList


def show_type(label, operation):
    try:
        operation()
    except TypeError as error:
        print(f'{label}: {type(error).__name__}')


if __name__ == '__main__':
    plain = Public('summary', '__str__', '__repr__', '__add__', '__getitem__', '__call__', '__iter__')(ReadingList)(['A', 'B'])
    print('plain direct add:', plain.__add__(['C']).summary())
    print('plain direct lookups:', plain.__getitem__(0), plain.__call__('> '), list(plain.__iter__()))
    print('plain repr masked:', type(plain).__repr__ is object.__repr__, repr(object.__getattribute__(plain, '_Controlled__target')))
    show_type('plain implicit add', lambda: plain + ['C'])
    show_type('plain implicit index', lambda: plain[0])
    show_type('plain implicit call', lambda: plain('> '))
    show_type('plain implicit iter', lambda: iter(plain))

    checked = CheckedReadingList(['A', 'B'])
    result = checked + ['C']
    print('checked results:', str(checked), checked[1], checked('> '), result.summary(), type(result).__name__)
    first, second = iter(checked), iter(checked)
    print('iterators first steps:', next(first), next(second), next(first))
    try:
        next(first)
    except StopIteration:
        print('old iterator exhausted: StopIteration')
    print('old iterator again:', list(first))
    print('fresh iterator:', list(iter(checked)))
    print('nested pairs:', [(outer, inner) for outer in checked for inner in checked])

    denied_add = DeniedAddReadingList(['A', 'B'])
    show_type('denied explicit add', lambda: denied_add.__add__(['C']))
    show_type('denied implicit add', lambda: denied_add + ['C'])
    denied_iter = DeniedIterReadingList(['A', 'B'])
    show_type('denied iteration', lambda: iter(denied_iter))

    direct = DirectAdd(['A', 'B'])
    print('direct explicit add:', direct.__add__(['C']).summary())
    print('direct implicit add:', (direct + ['C']).summary())
